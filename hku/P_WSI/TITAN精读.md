TITAN(Transformer-based pathology Image and Text Alignment Network)
# Abstract
- SSL+视觉语言对齐
- 不需要 finetune 和 label，可以提取通用的 slide 表示和生成相应的病理报告
- tasks
	- linear probing
		- 少量数据训练一个线性分类器比如 `nn.Linear`，不调整预训练模型的参数，评估的模型在下游任务上的迁移能力
		- 比如 TITAN 用的数据没有提到结直肠癌，增加一个线性分类器，不调整预训练模型的参数，只训练这个分类器，看在结直肠癌数据上的分类准确率如何
	- few-shot & zero-shot classification 
		- 少量样本下训练模型进行分类任务
		- 没有样本数据来训练模型，例如 CLIP 计算图像-文本相似度来进行分类
	- rare cancer retrieval 
	- cross-modal retrieval 
	- pathology report generation

# Introduction
- 传统方法：
	- 提取 patch 特征进行下游任务
	- 需要从头开始训练，处理大规模 WSI 数据耗时
- 已有的 slide-level foundation model 
	- vision-only，没有结合 pathological reports
	- 训练样本少（相对于 patch-level 的 model 来说），泛化能力低
	- 需要 finetune，对新任务的迁移能力不足
- 提出的 foundation model
	- 直接从整个 WSI 提取特征不依赖单独的 patch
	- 处理任意大小的 WSI

# Overview 
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202505281548864.png)


# Results 
## data
- private dataset Mass-340K
	- 335645 WSIs for TITANv (stage1)
		- 20 organs
		- 90.9% H&E, 9.1% IHC
		- 70.0% tumor, 30.0% non-tumor
		![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202505281428862.png)
	- 182862 medical reports 
		

## Scaling self-supervised learning from histology patches to whole slide images
3-stage pretrain:
- Stage 1: Vision-only Unimodal Pretraining
	- data: 335645 WSIs 
	- method
		- 传统的 ViT：输入原始图像切割出来的 patch
		- TITANv 的slide encoder 使用 patch encoder 预先提取的 patch 特征并且保留原始的 patch 2D 分布位置，加入位置编码
		- iBOT (Image BERT) 框架，mask 部分图像并让模型预测，进行视觉自监督预训练
	- challenges
		- token 长且多样（>10^4 at slide-level, while 196-256 at patch level）。WSI 图像比较大，每张大小差异大，所以patch多数量级差距大
		- 