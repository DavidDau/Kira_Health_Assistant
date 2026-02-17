# ⚡ Quick Start Guide

Get up and running with Kira Health Assistant in minutes!

## 🚀 Option 1: Google Colab (Recommended - Fastest Way)

### Step 1: Open in Colab

1. Click this badge: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/Kira_Health_Assistant/blob/main/kira_health_assistant.ipynb)
2. Sign in to your Google account

### Step 2: Enable GPU

1. Click **Runtime** → **Change runtime type**
2. Select **T4 GPU** under Hardware accelerator
3. Click **Save**

### Step 3: Run the Notebook

1. Click **Runtime** → **Run all**
2. Wait 20-30 minutes for training to complete
3. The Gradio interface will launch automatically!

### Step 4: Interact with Kira

1. Click the Gradio public link
2. Type your medical questions
3. Get instant responses!

**That's it!** ✅

---

## 💻 Option 2: Local Setup (For Advanced Users)

### Prerequisites

- Python 3.8 or higher
- 16GB+ RAM
- NVIDIA GPU with 10GB+ VRAM (optional but recommended)
- Git

### Step 1: Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Kira_Health_Assistant.git
cd Kira_Health_Assistant
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Verify Setup

```bash
python setup_check.py
```

### Step 5: Run Notebook

```bash
jupyter notebook kira_health_assistant.ipynb
```

Or use Jupyter Lab:

```bash
jupyter lab kira_health_assistant.ipynb
```

### Step 6: Train and Deploy

1. Run all cells in the notebook
2. Wait for training to complete
3. Gradio interface will launch locally
4. Open http://localhost:7860 in your browser

---

## 🎯 What Happens During Training

1. **Dataset Loading** (~1 min)
   - Downloads medical flashcard dataset
   - Samples 3,000 Q&A pairs
   - Shows data statistics

2. **Model Setup** (~2 min)
   - Loads TinyLlama base model
   - Applies 4-bit quantization
   - Configures LoRA adapters

3. **Training** (~15-20 min)
   - 3 epochs over training data
   - Real-time loss tracking
   - Automatic checkpointing

4. **Evaluation** (~2 min)
   - Calculates ROUGE scores
   - Tests on validation set
   - Compares base vs fine-tuned

5. **Deployment** (~1 min)
   - Launches Gradio interface
   - Generates shareable link
   - Ready for interaction!

**Total Time: ~25-30 minutes**

---

## 💡 Quick Commands Reference

### Run Inference Only (After Training)

```bash
# Interactive mode
python inference.py

# Single question
python inference.py --question "What are the symptoms of diabetes?"

# Custom settings
python inference.py --model_path ./kira_final_model --temperature 0.7
```

### Check System Requirements

```bash
python setup_check.py
```

### Test with Sample Questions

Open `TEST_QUESTIONS.md` for 70+ curated medical questions to test your model.

---

## 📱 Using the Gradio Interface

### Basic Usage

1. Type your question in the text box
2. Press Enter or click Submit
3. Wait a few seconds for response
4. Read Kira's answer

### Tips for Best Results

- ✅ Ask specific, clear questions
- ✅ Use medical terminology when appropriate
- ✅ One question at a time
- ❌ Avoid very long, complex questions
- ❌ Don't ask for personal medical advice

### Example Questions

```
"What are the symptoms of diabetes?"
"How does hypertension affect the heart?"
"What is the purpose of antibiotics?"
"Explain the difference between Type 1 and Type 2 diabetes."
```

---

## 🎓 Learning Path

### If you're new to LLMs:

1. Read the [README.md](README.md) for project overview
2. Run the Colab notebook step by step
3. Read comments in the code to understand each section
4. Experiment with [config.py](config.py) parameters

### If you want to improve the model:

1. Review [TEST_QUESTIONS.md](TEST_QUESTIONS.md)
2. Test current model performance
3. Adjust hyperparameters in [config.py](config.py)
4. Retrain and compare results
5. Document findings in experiment tracking

### If you encounter issues:

1. Check [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
2. Run `python setup_check.py`
3. Review error messages carefully
4. Search GitHub issues
5. Ask in GitHub Discussions

---

## 📊 Project Structure at a Glance

```
Kira_Health_Assistant/
│
├── 📓 kira_health_assistant.ipynb    # Main training notebook
├── 📋 README.md                       # Project documentation
├── ⚙️ config.py                       # Configuration settings
├── 🤖 inference.py                    # Run trained model
├── 📦 requirements.txt                # Dependencies
│
├── 📚 Documentation/
│   ├── DEMO_VIDEO_GUIDE.md           # How to create demo video
│   ├── TROUBLESHOOTING.md            # Common issues & solutions
│   ├── CONTRIBUTING.md               # Contribution guidelines
│   ├── TEST_QUESTIONS.md             # 70+ test questions
│   └── QUICK_START.md                # This file!
│
└── 🛠️ Utilities/
    ├── setup_check.py                # Verify installation
    ├── .gitignore                    # Git ignore rules
    └── LICENSE                       # MIT License
```

---

## ⚡ Speed Run (Minimal Steps)

**For experienced users who want to get started ASAP:**

```bash
# 1. Clone and setup
git clone https://github.com/YOUR_USERNAME/Kira_Health_Assistant.git
cd Kira_Health_Assistant
python -m venv venv && source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

# 2. Train (or use Colab)
jupyter notebook kira_health_assistant.ipynb
# Run all cells

# 3. Test
python inference.py --question "What is diabetes?"

# Done! 🎉
```

**Or just use Colab**: Click badge → Enable GPU → Run all → Chat with Kira in 25 minutes!

---

## 🎯 Success Checklist

After setup, you should be able to:

- [ ] Load the medical flashcards dataset
- [ ] See TinyLlama model loaded with LoRA
- [ ] Start training without errors
- [ ] See training loss decreasing
- [ ] Generate ROUGE scores on validation set
- [ ] Launch Gradio interface successfully
- [ ] Ask medical questions and get responses
- [ ] Compare base model vs fine-tuned responses
- [ ] See improvement in medical accuracy

If all checked ✅ - **Congratulations!** Your Kira Health Assistant is working perfectly! 🎊

---

## 🆘 Quick Help

### Training is slow?

➡️ Use Google Colab with T4 GPU (free)

### Out of memory?

➡️ Reduce `config.BATCH_SIZE = 2` and `config.MAX_SAMPLES = 1500`

### Model not loading?

➡️ Verify path: `print(os.listdir("./"))` and check model directory exists

### Gradio won't launch?

➡️ Try different port: `demo.launch(server_port=7861)`

### Other issues?

➡️ See [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

---

## 📞 Support

- 📖 Read the docs: [README.md](README.md)
- 🐛 Report bugs: [GitHub Issues](https://github.com/YOUR_USERNAME/Kira_Health_Assistant/issues)
- 💬 Ask questions: [GitHub Discussions](https://github.com/YOUR_USERNAME/Kira_Health_Assistant/discussions)
- 🎥 Watch demo: [Link to demo video]

---

## 🎉 Next Steps After Setup

1. **Test thoroughly**: Use questions from `TEST_QUESTIONS.md`
2. **Experiment**: Modify `config.py` and retrain
3. **Create demo video**: Follow `DEMO_VIDEO_GUIDE.md`
4. **Share your work**: Add screenshots and results to README
5. **Contribute**: See `CONTRIBUTING.md` for ways to help

---

**Happy training! Let's build something amazing! 🚀**

---

_Last updated: February 2026_
_Estimated time to first result: 25-30 minutes on Colab_
