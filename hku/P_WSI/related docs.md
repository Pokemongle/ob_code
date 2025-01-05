# Annex1-Background
## Terminology 术语
CRC, Colorectal cancer  结直肠癌
WSI, Whole-slide histopathology images 全片组织病理学图像
histopathology 组织病理学
MIL Multi Instance Learning 多实例学习

---
## Background背景
CRC 在香港发病率高死亡率高，早期诊断很重要但是人工耗时耗力，人手短缺。因此需要可靠的 CRC 组织病理图像分析的计算机辅助决策支持系统，具有巨大的商业潜力。

人工/计算机辅助的工作流对比
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202412061637840.png)

WSI 的生成和存储
	WSI 是通过全切片扫描仪生成的，通常以多分辨率金字塔结构存储
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202412061656979.png)
	因为 WSI 通常很大，GPU 内存不够用，因此需要切割成小片，分别分析然后总结，称为 MIL（多实例学习）

---

# Annex 2-Methodology
## Task1_Whole slide image pre-processing and test-time normalization

`ssh -N -f -L localhost:8888:localhost:8888 zyxiong@research25.saas.hku.hk`

---
p_wsi 工程文件目录
```
project_root/
│
├── datasets/
│   ├── dataset1/
│   │   ├── train/
│   │   ├── val/
│   │   └── test/
│   ├── dataset2/
│   │   ├── train/
│   │   ├── val/
│   │   └── test/
│   └── ...
│
├── models/
│   ├── model_name1/
│   │   ├── checkpoint_epoch_1.pth
│   │   ├── checkpoint_epoch_2.pth
│   │   └── ...
│   ├── model_name2/
│   └── ...
│
├── results/
│   ├── model1/
│   │   ├── dataset1/
│   │   │   	├── fold_1_metrics.json
│   │   │   	├── fold_2_metrics.json
│   │   │   	└── ...
│   │   ├── dataset2/
│   │   │   	├── fold_1_metrics.json
│   │   │   	├── fold_2_metrics.json
│   │   │   	└── ...
│   │   └── ...
│   ├── model2/
│   │   ├── dataset1/
│   │   │   	├── fold_1_metrics.json
│   │   │   	├── fold_2_metrics.json
│   │   │   	└── ...
│   │   ├── dataset2/
│   │   │   	├── fold_1_metrics.json
│   │   │   	├── fold_2_metrics.json
│   │   │   	└── ...
│   │   └── ...
│   └── ...
└── scripts/
    ├── train.py
    ├── test.py
    └── utils.py

```