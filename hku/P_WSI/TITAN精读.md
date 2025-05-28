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


# Method
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
	![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202505281730399.png)
	- data: 335645 WSIs 
	- method
		- 传统的 ViT：输入原始图像切割出来的 patch
		- TITANv 的slide encoder 使用 patch encoder 预先提取的 patch 特征并且保留原始的 patch 2D 分布位置，加入位置编码
		- iBOT (Image BERT) 框架，mask 部分图像并让模型预测，进行视觉自监督预训练
	- challenges and solutions
		- token 长且多样（>10^4 at slide-level, while 196-256 at patch level）。WSI 图像比较大，每张大小差异大，所以patch多数量级差距大
			- WSI → 512×512px 20x patches
			- use CONCHv1.5
		- WSI 的 augmentation
			- randomly sample a 8192×8192px ROI for each epoch
			- randomly sample 2 global (14×14) and 10 local (6×6) crops from the ROI for iBOT
			- vertical and horizontal flipping
			- posterize feature augmentation
		- WSI 的 position encoding 
			- 2D ALiBi (attention with linear bias)
- Stage 2&3: 
	![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202505281752523.png)
	- data: 
		- 423,122 pairs of 8K×8K ROIs and captions
		- 182,862 pairs of WSIs and corresponding pathology reports
	- method
		- 使用 coca 策略将 PathChat 生成的 caption 和 ROI 对齐
		- pretrain TITANv 

# Results 
# Comparison with benchmark

| 模型       | 预训练策略      | patch-level encoder | 数据规模               |
| -------- | ---------- | ------------------- | ------------------ |
| TITAN    | 视觉-语言对齐    | 多分辨率                | (private)Mass-340K |
| PRISM    | WSI-报告对比学习 | 256×256, 20×        | 1.7×               |
| GigaPath | 掩蔽图像重建     | 256×256, 20×        | 0.49×              |
| CHIEF    | 监督对比学习     | 256×256,10×         | 0.18×              |
另外还和 meanpooling 对比

2 Classification tasks 
- ROI-level cancer subtyping
	- TCGA-UT-8K
	- 32 labels 
	- 25495 ROIs, each of 8192×8192px, 20×
- slide-level OncoTree code subtyping
	- TCGA-OT
	- 46 labels 
	- 11186 WSIs 
- 除了 CHIEF 其他模型预训练都没有使用 TCGA 数据集