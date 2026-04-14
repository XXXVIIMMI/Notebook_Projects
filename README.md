
# 🧠 Notebook Projects
### Deep Learning & Computer Vision — PyTorch Notebook Series

A personal collection of deep learning and computer vision experiments written in **Jupyter Notebook style**, using **PyTorch**. Each notebook is self-contained, beginner-friendly, and heavily commented so the code explains itself.

---

## 📁 Project Structure

```
Notebook_Projects/
│
├── src/
│   ├── Notebook/               ← All .ipynb notebooks live here
│   │   ├── 01_CNN_MNIST.ipynb
│   │   ├── 02_CNN_ISIC.ipynb
│   │   └── ...                 ← More notebooks coming
│   │
│   ├── data/                   ← Datasets auto-download here
│   └── app/                    ← Any inference apps or demos
│
├── README.md
├── LICENSE
└── .gitignore
```

---

## 📓 Notebooks

| # | Notebook | Topic | Dataset | Status |
|---|----------|-------|---------|--------|
| 01 | `01_CNN_MNIST.ipynb` | CNN Image Classification | MNIST | ✅ Done |
| 02 | `02_CNN_ISIC.ipynb` | CNN Skin Disease Detection | ISIC | ✅ Done |
| 03 | *(coming soon)* | Transfer Learning | ImageNet | 🔄 Planned |
| 04 | *(coming soon)* | Object Detection | COCO | 🔄 Planned |
| 05 | *(coming soon)* | Image Segmentation | VOC | 🔄 Planned |

---

## ⚙️ Environment Setup

Choose **one** of the three methods below depending on where you run the notebooks.

---

### 🐍 Option 1 — Conda (Local Setup, Recommended)

> Best for running notebooks on your own machine with GPU support.

**Step 1 — Install Miniconda** (skip if already installed)

Download from: https://docs.conda.io/en/latest/miniconda.html

**Step 2 — Create the environment**

```bash
conda create -n notebook-projects python=3.10 -y
```

**Step 3 — Activate it**

```bash
conda activate notebook-projects
```

**Step 4 — Install PyTorch**

For **GPU (CUDA 11.8)**:
```bash
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia -y
```

For **CPU only**:
```bash
conda install pytorch torchvision torchaudio cpuonly -c pytorch -y
```

**Step 5 — Install remaining packages**

```bash
pip install jupyter notebook matplotlib scikit-learn pandas pillow tqdm
```

**Step 6 — Register the environment as a Jupyter kernel**

```bash
pip install ipykernel
python -m ipykernel install --user --name notebook-projects --display-name "PyTorch (notebook-projects)"
```

**Step 7 — Launch Jupyter**

```bash
jupyter notebook
```

Then open any `.ipynb` file from `src/Notebook/`.

---

**Quick verify** — run this inside a notebook cell to confirm everything works:

```python
import torch
print("PyTorch version :", torch.__version__)
print("CUDA available  :", torch.cuda.is_available())
print("Device          :", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "CPU")
```

---

### ☁️ Option 2 — Google Colab

> Zero setup. Just open the notebook in your browser. GPU is free.

**Step 1 — Upload the notebook**

Go to [colab.research.google.com](https://colab.research.google.com) → `File` → `Upload notebook` → pick any `.ipynb` from `src/Notebook/`

**Step 2 — Enable GPU**

`Runtime` → `Change runtime type` → Hardware accelerator → **T4 GPU** → Save

**Step 3 — Install any missing packages** (add this at the top of the notebook)

```python
# Run this cell first in Colab
!pip install torchvision --quiet
```

**Step 4 — Mount Google Drive** (optional, to save/load data)

```python
from google.colab import drive
drive.mount('/content/drive')
```

Everything else in the notebook runs as-is. PyTorch comes pre-installed in Colab.

---

### 💻 Option 3 — VS Code + Colab Kernel (Best of Both Worlds)

> Write and edit notebooks in VS Code, but run them on Colab's free GPU.

**Step 1 — Install the Jupyter extension in VS Code**

Open VS Code → Extensions (`Ctrl+Shift+X`) → search `Jupyter` → Install

**Step 2 — Install the Colab extension**

Search `Google Colab` in extensions → Install **"Colab"** by Google

Or install from terminal:
```bash
code --install-extension ms-toolsai.jupyter
```

**Step 3 — Connect VS Code to Colab runtime**

1. Open any `.ipynb` file in VS Code
2. Click **"Select Kernel"** (top right of the notebook)
3. Choose **"Existing Jupyter Server"**
4. Open [colab.research.google.com](https://colab.research.google.com), create a new notebook
5. Go to `Runtime` → `Connect to a local runtime` — **OR** use the Colab URL directly

**Alternative (easier) — use Colab's built-in VS Code:**

1. Open your notebook in Colab
2. `Tools` → `Command Palette` → type `Open in VS Code`
3. Colab launches a VS Code server in the browser with GPU already connected ✅

**Step 4 — Confirm GPU inside VS Code**

```python
import torch
print(torch.cuda.is_available())   # should print True
```

---

## 🔧 Requirements Summary

```
python        >= 3.10
torch         >= 2.0
torchvision   >= 0.15
torchaudio    >= 2.0
jupyter       >= 1.0
matplotlib    >= 3.7
scikit-learn  >= 1.2
pandas        >= 2.0
pillow        >= 9.0
tqdm          >= 4.65
```

---

## 📌 Tips

- All datasets **auto-download** on first run — no manual setup needed
- Each notebook has a `DEVICE` cell at the top — it auto-selects GPU if available
- Notebooks are ordered by difficulty — start from `01_` if you're new to PyTorch
- The `src/data/` folder is in `.gitignore` so datasets won't be pushed to GitHub

---

## 🗺️ Roadmap

- [x] CNN from scratch (MNIST)
- [x] CNN for medical image classification (ISIC skin disease)
- [ ] Transfer Learning with ResNet / EfficientNet
- [ ] Object Detection with YOLO
- [ ] Image Segmentation with U-Net
- [ ] Generative models (VAE / GAN)
- [ ] Vision Transformer (ViT)

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

<p align="center">Built with ❤️ using PyTorch</p>