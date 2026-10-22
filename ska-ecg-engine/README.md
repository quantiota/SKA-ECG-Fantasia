# SKA learning on the resting ECG of the Fantasia subjects — results

This folder holds the **results** of the SKA engine on the PhysioNet
[Fantasia Database](../ecg-data-validation/): the learner's output for every step, the figures and the
cubes. The method is that of
[SKA-ECG-Heart-Rate-Variability](https://github.com/quantiota/SKA-ECG-Heart-Rate-Variability/tree/main/ska-ecg-engine):
five waves per cardiac cycle (P, Q, R, S, T), one step per wave, input Re ċ (cosine), scale 25,
one loop of 3,500 steps, at 250 Hz. The ECG is streamed into QuestDB (`ecg_fantasia_steps`) and the
learner's output is stored in `ecg_fantasia_ska_results`. The engine code is not published.

| file | content |
|---|---|
| `results/<id>/ska_<id>_runs.csv` | the learner's output for every step |
| `results/<id>/figures/` | H and P on the step index; the steps in (z, ż, P) |
| `results/tau_H.csv` | τ_H and N_H of every record |
| `vr/` | three cubes per record (P, missing waves tagged, Δt) |
| `build_ecg_vr.py`, `ska_ecg_vr_template*.html` | the cube builder and its templates |
| `plot_record.py`, `tau_h.py` | the figures and τ_H / N_H, from the run CSVs |

τ_H = time for the learner to reach 90 % of its saturation on its slowest transition;
N_H = τ_H / T_c, in cardiac cycles.

| group | record | sex | age | scale | τ_H (min) | N_H (cycles) | figures | cube |
|---|---|---|---|---|---|---|---|---|
| young | f1y01 | F | 23 | 25 | 8.5 | 664 | [H, P](results/f1y01/figures/ska_f1y01_cdot_cos_scale25.png) · [3D](results/f1y01/figures/bands3d_f1y01_cdot_cos_scale25.png) | [cube](vr/ska_ecg_f1y01_scale25_vr.html) |
| young | f1y02 | F | 28 | 25 | 10.5 | 644 | [H, P](results/f1y02/figures/ska_f1y02_cdot_cos_scale25.png) · [3D](results/f1y02/figures/bands3d_f1y02_cdot_cos_scale25.png) | [cube](vr/ska_ecg_f1y02_scale25_vr.html) |
| young | f1y03 | M | 34 | 25 | 10.2 | 680 | [H, P](results/f1y03/figures/ska_f1y03_cdot_cos_scale25.png) · [3D](results/f1y03/figures/bands3d_f1y03_cdot_cos_scale25.png) | [cube](vr/ska_ecg_f1y03_scale25_vr.html) |
| young | f1y04 | M | 31 | 25 | 14.0 | 640 | [H, P](results/f1y04/figures/ska_f1y04_cdot_cos_scale25.png) · [3D](results/f1y04/figures/bands3d_f1y04_cdot_cos_scale25.png) | [cube](vr/ska_ecg_f1y04_scale25_vr.html) |
| young | f1y05 | M | 23 | 25 | 10.6 | 657 | [H, P](results/f1y05/figures/ska_f1y05_cdot_cos_scale25.png) · [3D](results/f1y05/figures/bands3d_f1y05_cdot_cos_scale25.png) | [cube](vr/ska_ecg_f1y05_scale25_vr.html) |
| young | f1y06 | M | 30 | 25 | 11.0 | 650 | [H, P](results/f1y06/figures/ska_f1y06_cdot_cos_scale25.png) · [3D](results/f1y06/figures/bands3d_f1y06_cdot_cos_scale25.png) | [cube](vr/ska_ecg_f1y06_scale25_vr.html) |
| young | f1y07 | M | 21 | 25 | 12.3 | 651 | [H, P](results/f1y07/figures/ska_f1y07_cdot_cos_scale25.png) · [3D](results/f1y07/figures/bands3d_f1y07_cdot_cos_scale25.png) | [cube](vr/ska_ecg_f1y07_scale25_vr.html) |
| young | f1y08 | F | 30 | 25 | 11.0 | 686 | [H, P](results/f1y08/figures/ska_f1y08_cdot_cos_scale25.png) · [3D](results/f1y08/figures/bands3d_f1y08_cdot_cos_scale25.png) | [cube](vr/ska_ecg_f1y08_scale25_vr.html) |
| young | f1y09 | F | 32 | 25 | 9.7 | 688 | [H, P](results/f1y09/figures/ska_f1y09_cdot_cos_scale25.png) · [3D](results/f1y09/figures/bands3d_f1y09_cdot_cos_scale25.png) | [cube](vr/ska_ecg_f1y09_scale25_vr.html) |
| young | f1y10 | F | 21 | 25 | 8.7 | 664 | [H, P](results/f1y10/figures/ska_f1y10_cdot_cos_scale25.png) · [3D](results/f1y10/figures/bands3d_f1y10_cdot_cos_scale25.png) | [cube](vr/ska_ecg_f1y10_scale25_vr.html) |
| young | f2y01 | F | 23 | 25 | 9.1 | 628 | [H, P](results/f2y01/figures/ska_f2y01_cdot_cos_scale25.png) · [3D](results/f2y01/figures/bands3d_f2y01_cdot_cos_scale25.png) | [cube](vr/ska_ecg_f2y01_scale25_vr.html) |
| young | f2y03 | F | 28 | 25 | 10.5 | 615 | [H, P](results/f2y03/figures/ska_f2y03_cdot_cos_scale25.png) · [3D](results/f2y03/figures/bands3d_f2y03_cdot_cos_scale25.png) | [cube](vr/ska_ecg_f2y03_scale25_vr.html) |
| young | f2y04 | F | 27 | 25 | 8.6 | 596 | [H, P](results/f2y04/figures/ska_f2y04_cdot_cos_scale25.png) · [3D](results/f2y04/figures/bands3d_f2y04_cdot_cos_scale25.png) | [cube](vr/ska_ecg_f2y04_scale25_vr.html) |
| young | f2y05 | F | 25 | 25 | 8.3 | 641 | [H, P](results/f2y05/figures/ska_f2y05_cdot_cos_scale25.png) · [3D](results/f2y05/figures/bands3d_f2y05_cdot_cos_scale25.png) | [cube](vr/ska_ecg_f2y05_scale25_vr.html) |
| young | f2y06 | M | 26 | 25 | 10.9 | 660 | [H, P](results/f2y06/figures/ska_f2y06_cdot_cos_scale25.png) · [3D](results/f2y06/figures/bands3d_f2y06_cdot_cos_scale25.png) | [cube](vr/ska_ecg_f2y06_scale25_vr.html) |
| young | f2y07 | M | 31 | 25 | 11.3 | 651 | [H, P](results/f2y07/figures/ska_f2y07_cdot_cos_scale25.png) · [3D](results/f2y07/figures/bands3d_f2y07_cdot_cos_scale25.png) | [cube](vr/ska_ecg_f2y07_scale25_vr.html) |
| young | f2y08 | M | 21 | 25 | 7.5 | 460 | [H, P](results/f2y08/figures/ska_f2y08_cdot_cos_scale25.png) · [3D](results/f2y08/figures/bands3d_f2y08_cdot_cos_scale25.png) | [cube](vr/ska_ecg_f2y08_scale25_vr.html) |
| young | f2y09 | F | 21 | 25 | 7.1 | 534 | [H, P](results/f2y09/figures/ska_f2y09_cdot_cos_scale25.png) · [3D](results/f2y09/figures/bands3d_f2y09_cdot_cos_scale25.png) | [cube](vr/ska_ecg_f2y09_scale25_vr.html) |
| young | f2y10 | M | 21 | 25 | 9.1 | 564 | [H, P](results/f2y10/figures/ska_f2y10_cdot_cos_scale25.png) · [3D](results/f2y10/figures/bands3d_f2y10_cdot_cos_scale25.png) | [cube](vr/ska_ecg_f2y10_scale25_vr.html) |
| elderly | f1o01 | F | 77 | 25 | 10.8 | 664 | [H, P](results/f1o01/figures/ska_f1o01_cdot_cos_scale25.png) · [3D](results/f1o01/figures/bands3d_f1o01_cdot_cos_scale25.png) | [cube](vr/ska_ecg_f1o01_scale25_vr.html) |
| elderly | f1o02 | F | 73 | 25 | 11.7 | 693 | [H, P](results/f1o02/figures/ska_f1o02_cdot_cos_scale25.png) · [3D](results/f1o02/figures/bands3d_f1o02_cdot_cos_scale25.png) | [cube](vr/ska_ecg_f1o02_scale25_vr.html) |
| elderly | f1o03 | M | 73 | 25 | 10.6 | 658 | [H, P](results/f1o03/figures/ska_f1o03_cdot_cos_scale25.png) · [3D](results/f1o03/figures/bands3d_f1o03_cdot_cos_scale25.png) | [cube](vr/ska_ecg_f1o03_scale25_vr.html) |
| elderly | f1o04 | M | 81 | 25 | 13.0 | 669 | [H, P](results/f1o04/figures/ska_f1o04_cdot_cos_scale25.png) · [3D](results/f1o04/figures/bands3d_f1o04_cdot_cos_scale25.png) | [cube](vr/ska_ecg_f1o04_scale25_vr.html) |
| elderly | f1o05 | M | 76 | 25 | 11.8 | 667 | [H, P](results/f1o05/figures/ska_f1o05_cdot_cos_scale25.png) · [3D](results/f1o05/figures/bands3d_f1o05_cdot_cos_scale25.png) | [cube](vr/ska_ecg_f1o05_scale25_vr.html) |
| elderly | f1o06 | F | 74 | 25 | 12.7 | 644 | [H, P](results/f1o06/figures/ska_f1o06_cdot_cos_scale25.png) · [3D](results/f1o06/figures/bands3d_f1o06_cdot_cos_scale25.png) | [cube](vr/ska_ecg_f1o06_scale25_vr.html) |
| elderly | f1o07 | M | 68 | 25 | 11.0 | 678 | [H, P](results/f1o07/figures/ska_f1o07_cdot_cos_scale25.png) · [3D](results/f1o07/figures/bands3d_f1o07_cdot_cos_scale25.png) | [cube](vr/ska_ecg_f1o07_scale25_vr.html) |
| elderly | f1o08 | F | 73 | 25 | 8.2 | 618 | [H, P](results/f1o08/figures/ska_f1o08_cdot_cos_scale25.png) · [3D](results/f1o08/figures/bands3d_f1o08_cdot_cos_scale25.png) | [cube](vr/ska_ecg_f1o08_scale25_vr.html) |
| elderly | f1o09 | M | 71 | 25 | 15.0 | 642 | [H, P](results/f1o09/figures/ska_f1o09_cdot_cos_scale25.png) · [3D](results/f1o09/figures/bands3d_f1o09_cdot_cos_scale25.png) | [cube](vr/ska_ecg_f1o09_scale25_vr.html) |
| elderly | f1o10 | F | 71 | 25 | 9.6 | 668 | [H, P](results/f1o10/figures/ska_f1o10_cdot_cos_scale25.png) · [3D](results/f1o10/figures/bands3d_f1o10_cdot_cos_scale25.png) | [cube](vr/ska_ecg_f1o10_scale25_vr.html) |
| elderly | f2o01 | F | 73 | 25 | 8.6 | 600 | [H, P](results/f2o01/figures/ska_f2o01_cdot_cos_scale25.png) · [3D](results/f2o01/figures/bands3d_f2o01_cdot_cos_scale25.png) | [cube](vr/ska_ecg_f2o01_scale25_vr.html) |
| elderly | f2o02 | F | 75 | 25 | 10.7 | 597 | [H, P](results/f2o02/figures/ska_f2o02_cdot_cos_scale25.png) · [3D](results/f2o02/figures/bands3d_f2o02_cdot_cos_scale25.png) | [cube](vr/ska_ecg_f2o02_scale25_vr.html) |
| elderly | f2o03 | F | 85 | 25 | 11.3 | 660 | [H, P](results/f2o03/figures/ska_f2o03_cdot_cos_scale25.png) · [3D](results/f2o03/figures/bands3d_f2o03_cdot_cos_scale25.png) | [cube](vr/ska_ecg_f2o03_scale25_vr.html) |
| elderly | f2o04 | F | 70 | 25 | 10.3 | 616 | [H, P](results/f2o04/figures/ska_f2o04_cdot_cos_scale25.png) · [3D](results/f2o04/figures/bands3d_f2o04_cdot_cos_scale25.png) | [cube](vr/ska_ecg_f2o04_scale25_vr.html) |
| elderly | f2o05 | M | 83 | 25 | 7.8 | 584 | [H, P](results/f2o05/figures/ska_f2o05_cdot_cos_scale25.png) · [3D](results/f2o05/figures/bands3d_f2o05_cdot_cos_scale25.png) | [cube](vr/ska_ecg_f2o05_scale25_vr.html) |
| elderly | f2o06 | M | 70 | 25 | 13.9 | 639 | [H, P](results/f2o06/figures/ska_f2o06_cdot_cos_scale25.png) · [3D](results/f2o06/figures/bands3d_f2o06_cdot_cos_scale25.png) | [cube](vr/ska_ecg_f2o06_scale25_vr.html) |
| elderly | f2o07 | M | 77 | 25 | 12.7 | 636 | [H, P](results/f2o07/figures/ska_f2o07_cdot_cos_scale25.png) · [3D](results/f2o07/figures/bands3d_f2o07_cdot_cos_scale25.png) | [cube](vr/ska_ecg_f2o07_scale25_vr.html) |
| elderly | f2o08 | M | 71 | 25 | 10.2 | 634 | [H, P](results/f2o08/figures/ska_f2o08_cdot_cos_scale25.png) · [3D](results/f2o08/figures/bands3d_f2o08_cdot_cos_scale25.png) | [cube](vr/ska_ecg_f2o08_scale25_vr.html) |
| elderly | f2o09 | M | 77 | 25 | 10.0 | 541 | [H, P](results/f2o09/figures/ska_f2o09_cdot_cos_scale25.png) · [3D](results/f2o09/figures/bands3d_f2o09_cdot_cos_scale25.png) | [cube](vr/ska_ecg_f2o09_scale25_vr.html) |
| elderly | f2o10 | F | 73 | 25 | 7.4 | 613 | [H, P](results/f2o10/figures/ska_f2o10_cdot_cos_scale25.png) · [3D](results/f2o10/figures/bands3d_f2o10_cdot_cos_scale25.png) | [cube](vr/ska_ecg_f2o10_scale25_vr.html) |
