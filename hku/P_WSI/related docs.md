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

我想要使用这个方法来进行k-fold：方案2：使用验证集调整超参数目的：这种方法的目的是选出一个在验证集上表现最好的模型，然后使用更多的数据来进一步训练这个模型，以提高其在测试集上的性能。过程： 将数据集分为训练集、验证集和测试集。对于每个模型，使用训练集进行训练，并在验证集上评估性能。根据验证集上的性能选择最好的模型。使用训练集和验证集的合并数据集来重新训练选定的模型。在测试集上评估最终模型的性能。
One-Click Segmentation: Automatic segmentation of colorectal cancer regions in whole slide images. The segmentation results of the affected regions are displayed in different colors for easy visualization, as shown in Figure 12 below.

One-Click Tumor Classification: Automatic classification of tumor regions within patches of colorectal cancer whole slide images. The system traverses the WSI from top-left to bottom-right, compiles individual patch classifications of the WSI. The classification results of the patches are displayed in 

One-Click Survival Prediction: Automatically provide a comprehensive prediction of the colorectal cancer patients' survival chances of 2 or 5 years based on the tumor's features as observed in the whole slide image. The system can provide a prognosis that reflects the overall behavior of the tumor, aiding in the determination of treatment strategies and patient counseling.

删除的文件在 `~/.local/share`

patch gcn 环境配置
1. 第二，docs/requirements，`conda env update -n patchgcn --file docs/requirements.yaml`
之后需要 `conda install "setuptools <65" ` 和 `pip install numpy=1.19.1` 为第2步做准备
`conda env create -n patchgcn -f docs/requirements.yaml`
3. 首先，创建一个 patchgcn 的空环境。安装 pytorch cuda 至少为11.1，因为使用了 GTX3090  https://pytorch.org/get-started/previous-versions/ `conda install pytorch==1.8.0 torchvision==0.9.0 torchaudio==0.8.0 cudatoolkit=11.1 -c pytorch -c conda-forge ` 不行就用``
`pip install torch==1.8.0+cu111 torchvision==0.9.0+cu111 torchaudio==0.8.0 -f https://download.pytorch.org/whl/torch_stable.html
`
4. 安装 geometric 的依赖包 https://data.pyg.org/whl/torch-1.8.0%2Bcu111.html
5. 安装 torch_geometric `pip install torch_geometric`
6. 安装 lifelines 和 sksurv ，搜索 conda lifelines 和 conda sksurv，里面有下载指令，用 conda 安装成功了不行就 `pip install scikit-survival`
```
跑patchgcn项目
CUDA_VISIBLE_DEVICES=1 python main.py --which_splits 5foldcv --split_dir tcga_coad --mode path --model_type amil
```
`export LD_LIBRARY_PATH="/home/zyxiong/anaconda3/lib/"`

查看 jupyter kernel `jupyter kernelspec list` 
删除一个 jupyter kernel `jupyter kernelspec remove myenv`
添加一个 kernel 
`conda install ipykernel`
`python -m ipykernel install --user --name your_environment_name --display-name "Desired Kernel Name"`

```
export PATH=/usr/local/anaconda3/envs/patchgcn/bin:$PATH

export CPATH=/usr/local/anaconda3/envs/patchgcn/include:$CPATH

export LD_LIBRARY_PATH=/usr/local/anaconda3/envs/patchgcn/lib:$LD_LIBRARY_PATH

export DYLD_LIBRARY_PATH=/usr/local/anaconda3/envs/patchgcn/lib64:$DYLD_LIBRARY_PATH

```

```
# original CLAM
python create_patches_fp.py --source /home/zyxiong/Documents/COAD_WSI --save_dir /home/zyxiong/Documents/COAD_patches_origin --patch_size 256 --seg --patch --stitch 

# use CONCH
export CONCH_CKPT_PATH=/home/zyxiong/Programs/CONCH/checkpoints/conch/pytorch_model.bin

CUDA_VISIBLE_DEVICES=1 python extract_features_fp.py --data_h5_dir /home/zyxiong/Documents/COAD_patches_origin --data_slide_dir /home/zyxiong/Documents/COAD_WSI --csv_path /home/zyxiong/Documents/COAD_patches_origin/process_list_autogen.csv --feat_dir /home/zyxiong/Documents/COAD_patches_origin --batch_size 512 --slide_ext .svs --model_name "conch_v1"
```