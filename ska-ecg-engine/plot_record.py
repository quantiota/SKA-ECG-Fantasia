#!/usr/bin/env python3
"""Figures for one record and one scale (as Starter-Kit/scripts/plot_record.py of SKA-ECG-Heart-Rate-Variability).

    results/<id>/figures/ska_<id>_cdot_cos_scale<s>.png      entropy H and P = exp(-|ΔH/H|) on the step index
    results/<id>/figures/bands3d_<id>_cdot_cos_scale<s>.png  the steps in the learner's space (z, ż, P)

Colour = the transition between two successive waves (P→Q, Q→R, R→S, S→T, T→P).

    python plot_record.py f1y01 25
"""
import pathlib
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

HERE = pathlib.Path(__file__).resolve().parent
VAL = HERE.parent / "ecg-data-validation"
sys.path.insert(0, str(VAL))
from fantasia_chain import read_header                            # noqa: E402
NAMES = ["P→Q", "Q→R", "R→S", "S→T", "T→P"]
COLORS = ["#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#3987e5"]


def main():
    rid, scale = sys.argv[1], float(sys.argv[2])
    d = pd.read_csv(HERE / "results" / rid / f"ska_{rid}_runs.csv", dtype={"record_id": str})
    d = d[(d.input == "cdot_cos") & (d.scale == scale)].sort_values("event_index")
    d = d[np.isfinite(d.zdot)]
    d["tr"] = d.transition.str.replace("-", "→")
    info = read_header(VAL / "data" / f"{rid}.hea")["info"]
    out = HERE / "results" / rid / "figures"
    out.mkdir(parents=True, exist_ok=True)
    title = f"Record {rid} (Fantasia, {info['sex']}, {info['age']}, supine rest), input Re ċ, scale {scale:g}"

    fig, ax = plt.subplots(2, 1, figsize=(12, 7), sharex=True)
    for name, color in zip(NAMES, COLORS):
        m = d.tr == name
        ax[0].scatter(d.event_index[m], d.entropy[m], s=2, color=color, label=name)
        ax[1].scatter(d.event_index[m], d.P[m], s=2, color=color)
    ax[0].set_ylabel("entropy H")
    ax[1].set_ylabel("P = exp(−|ΔH/H|)")
    ax[1].set_xlabel("step")
    ax[0].legend(markerscale=5, ncol=5, loc="upper right", fontsize=8)
    ax[0].set_title(title)
    f1 = out / f"ska_{rid}_cdot_cos_scale{scale:g}.png"
    fig.savefig(f1, dpi=140, bbox_inches="tight"); plt.close(fig)

    fig = plt.figure(figsize=(9, 8))
    ax = fig.add_subplot(projection="3d")
    for name, color in zip(NAMES, COLORS):
        m = d.tr == name
        ax.scatter(d.knowledge[m], d.zdot[m], d.P[m], s=3, color=color, label=name, edgecolors="none")
    ax.set_xlabel("z = ‖Z‖"); ax.set_ylabel("ż (1/s)"); ax.set_zlabel("P")
    ax.legend(markerscale=4, fontsize=8)
    ax.set_title(title)
    f2 = out / f"bands3d_{rid}_cdot_cos_scale{scale:g}.png"
    fig.savefig(f2, dpi=140, bbox_inches="tight"); plt.close(fig)
    print(f"[png]    {f1}\n[png]    {f2}")


if __name__ == "__main__":
    main()
