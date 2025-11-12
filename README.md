# 🧠 A novel deep learning identifier for promoters and their strength using heterogeneous features

Promoters, which are short (50–1500 base-pair) in DNA regions, have emerged to play a critical role in the regulation of gene transcription. Numerous dangerous diseases, likewise cancer, cardiovascular, and inflammatory bowel diseases, are caused by genetic variations in promoters. Consequently, the correct identification and characterization of promoters are significant for the discovery of drugs. However, experimental approaches to recognizing promoters and their strengths are challenging in terms of cost, time, and resources. Therefore, computational techniques are highly desirable for the correct characterization of promoters from unannotated genomic data. Here, we designed a powerful bi-layer deep-learning based predictor named “PROCABLES“, which discriminates DNA samples as promoters in the first-phase and strong or weak promoters in the second-phase respectively. The proposed method utilizes five distinct features, such as word2vec, k-spaced nucleotide pairs, trinucleotide propensity-based features, trinucleotide composition, and electron–ion interaction pseudopotentials, to extract the hidden patterns from the DNA sequence. Afterwards, a stacked framework is formed by integrating a convolutional neural network (CNN) with bidirectional long-short-term memory (LSTM) using multi-view attributes to train the proposed model. The PROCABLES model achieved an accuracy of 0.971 and 0.920 and the MCC 0.940 and 0.840 for the first and second-layer using the ten-fold cross-validation test, respectively. The predicted results anticipate that the proposed PROCABLES protocol outperformed the advanced computational predictors targeting promoters and their types. In summary, this research will provide useful hints for the recognition of large-scale promoters in particular and other DNA problems in general.

---

## 📘 Overview

[Give a detailed description of your project. Explain its motivation, the problem it solves, and its overall approach.]

This project implements a system for **[briefly describe key functionality or goal]**.  
It combines **[technologies, models, or methods used]** to achieve **[expected outcome or result]**.

---

## 🏗️ System Architecture

The architecture of the system is shown below:

<p align="center">
  <img src="Architecture.PNG" alt="System Architecture" width="750"/>
</p>

**Figure:** Overall architecture of the proposed system.

[Optionally, add a short explanation of what each component in the figure represents.]

---

## 🚀 Features

- ✅ [Feature 1: Short explanation]  
- ✅ [Feature 2: Short explanation]  
- ✅ [Feature 3: Short explanation]  
- ✅ [Feature 4: Short explanation]  

---

## 🧠 Methodology

[Describe your approach in more technical detail — e.g., models used, algorithms, or workflow.]

Example outline:
1. **Data preprocessing:** [describe steps]
2. **Model design:** [describe model layers, architecture, etc.]
3. **Training process:** [epochs, loss function, optimizer, etc.]
4. **Evaluation:** [metrics, datasets used, etc.]

---

## ⚙️ Installation

Follow these steps to set up the environment and run the project:

```bash
# 1️⃣ Clone the repository
git clone https://github.com/[username]/[repo-name].git
cd [repo-name]

# 2️⃣ Create and activate a virtual environment (optional)
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)

# 3️⃣ Install dependencies
pip install -r requirements.txt
