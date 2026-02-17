# 🔧 Troubleshooting Guide

Common issues and solutions for Kira Health Assistant.

## 📋 Table of Contents

- [Installation Issues](#installation-issues)
- [Training Issues](#training-issues)
- [Memory Issues](#memory-issues)
- [Model Loading Issues](#model-loading-issues)
- [Inference Issues](#inference-issues)
- [Gradio Interface Issues](#gradio-interface-issues)
- [General Tips](#general-tips)

---

## Installation Issues

### Issue: `pip install` fails with dependency conflicts

**Solution 1**: Use a clean virtual environment

```bash
# Create new virtual environment
python -m venv kira_env
source kira_env/bin/activate  # Linux/Mac
# or
kira_env\Scripts\activate  # Windows

# Install requirements
pip install --upgrade pip
pip install -r requirements.txt
```

**Solution 2**: Install packages one by one

```bash
pip install torch --index-url https://download.pytorch.org/whl/cu118
pip install transformers datasets accelerate
pip install peft bitsandbytes trl
pip install gradio evaluate rouge-score
```

### Issue: `bitsandbytes` installation fails on Windows

**Solution**: Use pre-built wheels

```bash
pip install bitsandbytes-windows
# or use WSL (Windows Subsystem for Linux)
```

### Issue: `sentencepiece` not found

**Solution**:

```bash
pip install sentencepiece protobuf
```

---

## Training Issues

### Issue: Training is extremely slow

**Symptoms**: Training takes hours per epoch

**Solutions**:

1. **Use Google Colab with GPU**
   - Select Runtime → Change runtime type → T4 GPU
   - Verify GPU: `!nvidia-smi`

2. **Reduce dataset size**

   ```python
   config.MAX_SAMPLES = 1000  # Instead of 3000
   ```

3. **Increase batch size** (if memory allows)
   ```python
   config.BATCH_SIZE = 8
   config.GRADIENT_ACCUMULATION_STEPS = 2
   ```

### Issue: `CUDA out of memory` error

**Solutions**:

1. **Reduce batch size**

   ```python
   config.BATCH_SIZE = 2
   config.GRADIENT_ACCUMULATION_STEPS = 8
   ```

2. **Reduce sequence length**

   ```python
   config.MAX_LENGTH = 256  # Instead of 512
   ```

3. **Enable gradient checkpointing**

   ```python
   model.gradient_checkpointing_enable()
   ```

4. **Clear GPU cache**
   ```python
   import torch
   torch.cuda.empty_cache()
   ```

### Issue: Training loss not decreasing

**Possible causes and solutions**:

1. **Learning rate too high/low**

   ```python
   # Try these values
   config.LEARNING_RATE = 1e-4  # Lower
   config.LEARNING_RATE = 5e-4  # Higher
   ```

2. **Insufficient training data**
   - Increase MAX_SAMPLES
   - Check data quality
   - Verify data formatting

3. **Model initialization issue**
   - Restart kernel and reload model
   - Check if LoRA modules are attached correctly

### Issue: Model outputs gibberish after training

**Solutions**:

1. **Check training loss** - should decrease over epochs
2. **Verify data formatting** - check prompt templates
3. **Try lower learning rate** - might be overfitting
4. **Increase warmup steps**
   ```python
   config.WARMUP_STEPS = 200
   ```

---

## Memory Issues

### Issue: Kernel crashes during training

**Solutions**:

1. **On Colab**: Upgrade to Colab Pro (more RAM)
2. **Reduce memory usage**:

   ```python
   config.MAX_SAMPLES = 1500
   config.BATCH_SIZE = 2
   config.MAX_LENGTH = 256
   ```

3. **Clear outputs regularly**
   - Cell → All Output → Clear

4. **Use gradient accumulation**
   ```python
   config.GRADIENT_ACCUMULATION_STEPS = 8
   ```

### Issue: RAM usage keeps increasing

**Solution**: Restart kernel periodically

```python
# In Colab
from IPython.display import clear_output
import gc

gc.collect()
torch.cuda.empty_cache()
clear_output()
```

---

## Model Loading Issues

### Issue: Cannot load model - file not found

**Solution**: Check paths

```python
import os
print(os.listdir("./"))  # Check current directory
print(os.path.exists("./kira_final_model"))  # Verify path
```

### Issue: `SafetensorsError` when loading model

**Solutions**:

1. **Install/update safetensors**

   ```bash
   pip install --upgrade safetensors
   ```

2. **Load with PyTorch format**
   ```python
   model = AutoModelForCausalLM.from_pretrained(
       model_path,
       use_safetensors=False
   )
   ```

### Issue: Model architecture mismatch

**Solution**: Ensure base model matches training

```python
# Use same model for inference as training
BASE_MODEL = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
```

---

## Inference Issues

### Issue: Inference is very slow

**Solutions**:

1. **Move model to GPU**

   ```python
   model = model.to("cuda")
   inputs = inputs.to("cuda")
   ```

2. **Reduce generation length**

   ```python
   max_new_tokens=200  # Instead of 400
   ```

3. **Disable sampling for faster (deterministic) output**
   ```python
   do_sample=False
   ```

### Issue: Model generates repetitive text

**Solutions**:

1. **Increase repetition penalty**

   ```python
   repetition_penalty=1.3  # Instead of 1.1
   ```

2. **Adjust sampling parameters**

   ```python
   temperature=0.8
   top_p=0.95
   top_k=50
   ```

3. **Use nucleus sampling**
   ```python
   do_sample=True
   top_p=0.9
   ```

### Issue: Responses are too short

**Solutions**:

1. **Increase max tokens**

   ```python
   max_new_tokens=600
   ```

2. **Adjust stopping criteria**
   ```python
   # Remove early stopping
   model.config.max_length = 1024
   ```

### Issue: Responses are off-topic

**Solutions**:

1. **Improve prompt formatting**

   ```python
   prompt = f"<|system|>You are a medical assistant.</|system|><|user|>{question}</|user|><|assistant|>"
   ```

2. **Lower temperature for more focused responses**

   ```python
   temperature=0.5
   ```

3. **Check if model is properly fine-tuned**

---

## Gradio Interface Issues

### Issue: Gradio interface won't launch

**Solutions**:

1. **Check if port is available**

   ```python
   demo.launch(server_port=7861)  # Try different port
   ```

2. **Disable sharing temporarily**

   ```python
   demo.launch(share=False)
   ```

3. **Check firewall settings**

### Issue: "Module not found: gradio"

**Solution**:

```bash
pip install gradio==4.13.0
```

### Issue: Interface loads but doesn't respond

**Solutions**:

1. **Verify model is loaded**

   ```python
   print(model.device)  # Should show cuda or cpu
   ```

2. **Check function signature**

   ```python
   def chat_with_kira(message: str) -> str:
       # Must return string
       return response
   ```

3. **Add error handling**
   ```python
   try:
       response = generate_response(message)
   except Exception as e:
       response = f"Error: {str(e)}"
   return response
   ```

---

## General Tips

### Best Practices

1. **Save your work frequently**
   - Save model checkpoints
   - Export notebook regularly
   - Use version control (Git)

2. **Monitor resources**

   ```python
   # Check GPU memory
   if torch.cuda.is_available():
       print(f"Allocated: {torch.cuda.memory_allocated()/1e9:.2f} GB")
       print(f"Cached: {torch.cuda.memory_reserved()/1e9:.2f} GB")
   ```

3. **Use logging**

   ```python
   import logging
   logging.basicConfig(level=logging.INFO)
   logger = logging.getLogger(__name__)
   logger.info("Starting training...")
   ```

4. **Test incrementally**
   - Test with small dataset first
   - Verify each step works before proceeding
   - Save intermediate results

### Debugging Checklist

When something goes wrong:

- [ ] Check error message carefully
- [ ] Verify all dependencies are installed
- [ ] Restart kernel/runtime
- [ ] Clear outputs and cache
- [ ] Check GPU is available (if expected)
- [ ] Verify file paths are correct
- [ ] Test with smaller dataset
- [ ] Check for version compatibility
- [ ] Review recent code changes
- [ ] Search error message online

### Getting Help

If you're still stuck:

1. **Check existing issues** on GitHub
2. **Review documentation** thoroughly
3. **Create a minimal reproducible example**
4. **Ask in GitHub Discussions** with:
   - Error message
   - Steps to reproduce
   - Environment details
   - What you've already tried

### Useful Commands

```bash
# Check Python version
python --version

# Check installed packages
pip list | grep -E "torch|transformers|peft|gradio"

# Check CUDA version (if using GPU)
python -c "import torch; print(torch.version.cuda)"

# Check GPU availability
python -c "import torch; print(torch.cuda.is_available())"

# Clear pip cache
pip cache purge

# Reinstall package
pip uninstall package_name
pip install package_name
```

### Environment Variables

Sometimes setting these helps:

```bash
# For better error messages
export TRANSFORMERS_VERBOSITY=debug

# For CUDA issues
export CUDA_VISIBLE_DEVICES=0

# For memory issues
export PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb=512
```

---

## Platform-Specific Issues

### Google Colab

**Issue**: Session disconnects frequently

- **Solution**: Keep browser tab active, run `%%javascript` cell to prevent idle disconnect

**Issue**: Runtime upgrade required

- **Solution**: Runtime → Factory reset runtime, then reinstall packages

### Windows

**Issue**: Path issues with backslashes

- **Solution**: Use forward slashes or raw strings: `r"C:\path\to\file"`

**Issue**: `bitsandbytes` not working

- **Solution**: Use WSL or install Windows-compatible wheels

### Mac M1/M2

**Issue**: `torch` not using GPU

- **Solution**: Install MPS-enabled PyTorch:
  ```bash
  pip install torch torchvision torchaudio
  ```

---

## Still Having Issues?

1. **Run setup check**:

   ```bash
   python setup_check.py
   ```

2. **Check system requirements**:
   - Python 3.8+
   - 16GB+ RAM recommended
   - GPU with 10GB+ VRAM (for training)
   - Stable internet connection

3. **Try Google Colab**:
   - Often easiest environment
   - Free GPU access
   - Pre-configured

4. **Open an issue**:
   - Include error messages
   - Describe what you tried
   - Provide environment details

---

**Remember**: Most issues can be solved by:

1. Restarting the kernel
2. Clearing cache
3. Reducing batch size/dataset size
4. Checking paths and file existence

Good luck! 🍀
