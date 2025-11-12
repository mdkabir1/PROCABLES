# 🧠 A Novel Deep Learning Identifier for Promoters and Their Strength Using Heterogeneous Features

---

## 📘 Overview

We developed an improved predictor **PROCABLES** (PROmoters Classification using CNN, BiLSTM, and LSTM modELS) with high efficacy for predicting promoters and their types using sequence information derived from **CKSNAP**, **PseEIIP**, **PSTNP**, **TNC**, and **Word2Vec** feature encoding approaches.

The developed architecture of the DL-based model consists of two stages:
1. **Stage 1:** Predicts promoters from DNA sequences.
2. **Stage 2:** If a sequence is predicted as a promoter, the model further classifies it into **strong** or **weak** promoter types.

Extensive experiments show that in both levels, the ensemble deep learning model (**CNN + BiLSTM**) produces the best results on the fused features.  
The schematic layout of the PROCABLES approach is depicted below (Fig. 2).

The contribution of this research work can be summarized as follows:

- 🧩 We designed an intelligent two-layer DL model that predicts the promoter region in the first stage and their functional types in the second stage.  
- 🧬 We captured DNA-encoded patterns using the **Word2Vec** algorithm.  
- 📊 We analyzed the visual impact of biological features using the **t-distributed stochastic neighbor embedding (t-SNE)** method.  
- 🚀 We enhanced the overall prediction performance of promoters and their functional types (weak vs. strong) across both datasets.

---

## 🏗️ System Architecture

Several fundamental deep models may experience overfitting and ensemble diversity problems when dealing with small sample sizes.  
These techniques can teach classifiers more pertinent high-level characteristics. Ensemble learning has emerged as a robust strategy across many domains, including cancer subtype classification, hyperspectral imaging, and protein interaction prediction.

Since bioinformatics data is often **heterogeneous**, feature fusion techniques help integrate diverse information sources, making the model more adaptable and biologically meaningful.  

**PROCABLES** is an ensemble-based method that integrates five feature extraction techniques — **CKSNAP**, **PseEIIP**, **PSTNP**, **TNC**, and **Word2Vec** — with **CNN**, **LSTM**, and **BiLSTM** layers.  
This combination enables the model to learn complex DNA representations effectively, even with limited data.

The PROCABLES model was implemented using:
- **Python 3.10.10**
- **TensorFlow 2.10.0**
- **Keras 2.10.0**

**Model Details:**
- **Promoter Identification:** 2 layers of CNN + BiLSTM + dense layer  
- **Promoter Strength Classification:** 1 layer of CNN + LSTM + dense layer  
- **Epochs:** 30  
- **Batch Size:** 128  
- **Learning Rate:** 0.1  
- Hyperparameters are detailed in **Supplementary Table S1**.

<p align="center">
  <img src="Architecture.PNG" alt="System Architecture" width="750"/>
</p>

**Figure 2.** Schematic architecture of the PROCABLES framework.

---

## 🔖 Publication

This work has been published in *Methods (Elsevier)*, Volume 230, October 2024, Pages 119–128.

📄 **Full reference:**
> Aqsa Amjad, Saeed Ahmed, Muhammad Kabir, Muhammad Arif, Tanvir Alam (2024).  
> *A novel deep learning identifier for promoters and their strength using heterogeneous features.*  
> **Methods**, Volume 230, 119–128.  
> [https://doi.org/10.1016/j.ymeth.2024.08.005](https://doi.org/10.1016/j.ymeth.2024.08.005)

You can access the published article on [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1046202324001853).

---

## ⚙️ Installation

Follow these steps to set up the environment and run the project:

```bash
# 1️⃣ Clone the repository
git clone https://github.com/mdkabir1/PROCABLES.git
cd PROCABLES

# 2️⃣ Create and activate a virtual environment (optional)
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)

# 3️⃣ Install dependencies
pip install -r requirements.txt
