# SKA ECG Fantasia

 [![arXiv](https://img.shields.io/badge/arXiv-2503.13942-b31b1b)](https://arxiv.org/abs/2503.13942)   [![arXiv](https://img.shields.io/badge/arXiv-2504.03214-b31b1b)](https://arxiv.org/abs/2504.03214)   [![Hugging Face](https://img.shields.io/badge/🤗%20Hugging%20Face-SKA-orange)](https://huggingface.co/quant-iota) [![Sponsor](https://img.shields.io/badge/Sponsor-quantiota-ea4aaa?logo=github-sponsors)](https://github.com/sponsors/quantiota)


**Structured Knowledge Accumulation (SKA) on the healthy heart at rest**

This project applies the SKA real-time learner to the resting ECG of healthy subjects who are not
athletes, from the PhysioNet [Fantasia Database](https://physionet.org/content/fantasia/1.0.0/)
(Iyengar et al., Am J Physiol 1996, [doi:10.1152/ajpregu.1996.271.4.R1078](https://doi.org/10.1152/ajpregu.1996.271.4.R1078); Open Data Commons Attribution License v1.0). It is the
reference at 250 Hz for [SKA-ECG-Athletes](https://github.com/quantiota/SKA-ECG-Athletes).

The method is the one of
[SKA-ECG-Heart-Rate-Variability](https://github.com/quantiota/SKA-ECG-Heart-Rate-Variability):
the five waves of each cardiac cycle, the same input, the same learner, the same 3D cube.

## Data

40 healthy subjects in sinus rhythm, 20 young (21–34 years) and 20 elderly (68–85 years), lay
supine for about 120 minutes while watching the movie *Fantasia*. The ECG was sampled at 250 Hz.
Record f2y02 was sampled at 333 Hz and is not used: 39 records. The run of each record is its first
3,500 steps (700 cycles), at scale 25.

## Folders

| folder | content |
|---|---|
| [`ecg-data-validation/`](ecg-data-validation/) | the Fantasia records: download, reader, stream into QuestDB |
| [`ska-ecg-engine/`](ska-ecg-engine/) | the results, the figures and the cube builder |
| [`vr-library/`](vr-library/) | the cubes |

The SKA real-time engine is proprietary and is not included in this repository.
