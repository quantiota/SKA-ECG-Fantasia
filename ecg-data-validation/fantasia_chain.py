"""Fantasia record reader — the data source for the Fantasia stream.

Turns Fantasia WFDB records (header + format-16 or format-212 binary) into a sequence of
samples for the ECG signal, at the native rate (250 Hz):

    sample k  =  the ECG at t = k / 250 s
    value     =  (adc - baseline) / gain     in mV, from the record header

Format 16: one 16-bit little-endian sample per signal, the signals interleaved (series f1).
Format 212: two 12-bit samples packed in 3 bytes, the signals interleaved (series f2).
Records are emitted one after another, each whole. Raw values only: no
resampling, no filtering, no beat detection, no scaling.
"""
from __future__ import annotations

import pathlib
import re

import numpy as np


def read_header(path):
    """Fantasia .hea -> fs, n, the signals (file, fmt, gain, baseline, name) and the
    comment line (age, sex)."""
    text = pathlib.Path(path).read_text().splitlines()
    lines = [l for l in text if l.strip() and not l.startswith('#')]
    _, nsig, fs, n = lines[0].split()[:4]
    signals = []
    for l in lines[1:1 + int(nsig)]:
        f = l.split()
        signals.append({'file': f[0], 'fmt': f[1], 'gain': float(f[2]), 'baseline': float(f[4]),
                        'name': f[-1]})
    comments = [l[1:].strip() for l in text if l.startswith('#')]
    m = re.search(r'Age:\s*(\S+)\s+Sex:\s*(\S+)', ' '.join(comments))
    age, sex = m.groups() if m else ('?', '?')
    return {'nsig': int(nsig), 'fs': float(fs), 'n': int(n), 'signals': signals,
            'info': {'age': age, 'sex': sex, 'comments': comments}}


def read_16(path, nsig):
    """Format 16 -> int array (samples, nsig)."""
    s = np.fromfile(path, dtype='<i2').astype(np.int32)
    return s[: s.size - s.size % nsig].reshape(-1, nsig)


def read_212(path, nsig):
    """Format 212 -> int array (samples, nsig)."""
    b = np.fromfile(path, dtype=np.uint8)
    b = b[: b.size - b.size % 3].reshape(-1, 3).astype(np.int32)
    s0 = b[:, 0] | ((b[:, 1] & 0x0F) << 8)
    s1 = b[:, 2] | ((b[:, 1] & 0xF0) << 4)
    s = np.column_stack([s0, s1]).ravel()
    s[s > 2047] -= 4096                                     # 12-bit two's complement
    return s[: s.size - s.size % nsig].reshape(-1, nsig)


READERS = {'16': read_16, '212': read_212}


def read_records(path):
    """records.txt -> [(Fantasia record name, record_id)], in order ('#' lines ignored)."""
    out = []
    for l in pathlib.Path(path).read_text().splitlines():
        if l.strip() and not l.startswith('#'):
            f = l.split()
            out.append((f[0], f[1]))
    return out


class FantasiaRecord:
    """One record, the ECG signal, whole."""

    def __init__(self, data_dir, path, record_id, channel):
        self.record_id = record_id
        hdr = read_header(pathlib.Path(data_dir) / f'{path}.hea')
        names = [s['name'] for s in hdr['signals']]
        if channel not in names:
            raise SystemExit(f'record {record_id} has no channel {channel!r}; has {names}')
        sig = hdr['signals'][names.index(channel)]
        if sig['fmt'] not in READERS:
            raise SystemExit(f'record {record_id}: format {sig["fmt"]} not supported')
        self.fs, self.gain, self.baseline = hdr['fs'], sig['gain'], sig['baseline']
        self.info = hdr['info']
        self.age = self.info['age']
        raw = READERS[sig['fmt']](pathlib.Path(data_dir) / sig['file'], hdr['nsig'])
        if len(raw) != hdr['n']:
            raise SystemExit(f'record {record_id}: header says {hdr["n"]:,} samples, '
                             f'file holds {len(raw):,}')
        self.adc = raw[:, names.index(channel)].astype(np.int64)

    @property
    def n(self):
        return int(self.adc.size)

    def value(self):
        """The samples in mV."""
        return (self.adc - self.baseline) / self.gain


class FantasiaChain:
    """Walks the listed records and yields one event per sample."""

    def __init__(self, data_dir, records, channel, max_steps=None):
        self.records = [FantasiaRecord(data_dir, p, rid, channel) for p, rid in records]
        self.max_steps = max_steps

    @property
    def total_steps(self):
        return sum(r.n for r in self.records)

    def events(self):
        step = 0
        for rec in self.records:
            v = rec.value()
            for k in range(rec.n):
                if self.max_steps is not None and step >= self.max_steps:
                    return
                yield {'step': step, 'record_id': rec.record_id, 'age_band': rec.age,
                       'sample_index': k, 'record_length': rec.n,
                       'adc': int(rec.adc[k]), 'value': float(v[k])}
                step += 1


if __name__ == '__main__':
    from config import ECG_CONFIG as C
    for p, rid in read_records(C['records']):
        r = FantasiaRecord(C['data_dir'], p, rid, C['channel'])
        v = r.value()
        print(f'{rid}  age {r.age}  {r.info["sex"]}  {r.fs:g} Hz  {r.n:,} samples ({r.n / r.fs / 60:.1f} min)  '
              f'{v.min():+.3f} .. {v.max():+.3f} mV')
