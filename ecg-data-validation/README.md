# The Fantasia records

Source: [Fantasia Database](https://physionet.org/content/fantasia/1.0.0/), PhysioNet,
Open Data Commons Attribution License v1.0 — Iyengar N., Peng C.-K., Morin R., Goldberger A.L.,
Lipsitz L.A., "Age-related alterations in the fractal scaling of cardiac interbeat interval
dynamics", Am J Physiol 271:R1078–R1084 (1996), doi:10.1152/ajpregu.1996.271.4.R1078.

```
./fetch_data.sh                      # the records of records.txt -> data/ (not committed)
python fantasia_chain.py             # check: subject, rate, length, range of each record
python stream_fantasia.py --records f1y01 --max-steps 375000 --speed 20
```

| file | content |
|---|---|
| `records.txt` | the records used, in order (f2y02, sampled at 333 Hz, is left out) |
| `fetch_data.sh` | downloads the header and signal file of each record |
| `fantasia_chain.py` | reads a record (format 16 or 212) and gives its ECG in mV, at 250 Hz |
| `stream_fantasia.py` | streams the ECG into the QuestDB table `ecg_fantasia_steps`, at 250 Hz, the first 25 minutes of each record |
| `config.py` | QuestDB connection and stream settings |
