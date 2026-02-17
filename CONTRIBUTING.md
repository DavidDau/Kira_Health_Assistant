# 🤝 Contributing to Kira Health Assistant

Thank you for your interest in contributing to Kira Health Assistant! This document provides guidelines for contributing to the project.

## 🌟 Ways to Contribute

1. **Bug Reports**: Report issues or bugs you encounter
2. **Feature Requests**: Suggest new features or improvements
3. **Code Contributions**: Submit pull requests with fixes or enhancements
4. **Documentation**: Improve documentation, guides, or examples
5. **Dataset Expansion**: Suggest or contribute medical datasets
6. **Testing**: Help test the model and report findings

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- Basic understanding of:
  - Python programming
  - Machine Learning/NLP
  - Hugging Face ecosystem
  - Git workflow

### Setup Development Environment

1. **Fork the repository**

   ```bash
   # Click the "Fork" button on GitHub
   ```

2. **Clone your fork**

   ```bash
   git clone https://github.com/YOUR_USERNAME/Kira_Health_Assistant.git
   cd Kira_Health_Assistant
   ```

3. **Create a virtual environment**

   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Linux/Mac
   python -m venv venv
   source venv/bin/activate
   ```

4. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Verify setup**

   ```bash
   python setup_check.py
   ```

6. **Create a new branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bugfix-name
   ```

## 📝 Contribution Guidelines

### Code Style

- Follow PEP 8 style guide
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Comment complex logic
- Keep functions focused and modular

### Commit Messages

Use clear, descriptive commit messages:

```
feat: Add support for Gemma-2B model
fix: Correct ROUGE score calculation
docs: Update README with new examples
refactor: Improve data preprocessing pipeline
test: Add unit tests for inference module
```

### Pull Request Process

1. **Update your fork**

   ```bash
   git fetch upstream
   git merge upstream/main
   ```

2. **Make your changes**
   - Write clean, tested code
   - Update documentation if needed
   - Add comments for clarity

3. **Test your changes**
   - Run existing tests
   - Add new tests if applicable
   - Verify the notebook runs end-to-end

4. **Commit and push**

   ```bash
   git add .
   git commit -m "feat: your descriptive message"
   git push origin feature/your-feature-name
   ```

5. **Create Pull Request**
   - Go to your fork on GitHub
   - Click "New Pull Request"
   - Describe your changes clearly
   - Reference any related issues

### PR Description Template

```markdown
## Description

Brief description of what this PR does.

## Type of Change

- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Code refactoring

## Testing

Describe how you tested your changes.

## Related Issues

Closes #123

## Checklist

- [ ] Code follows project style guidelines
- [ ] Comments added for complex logic
- [ ] Documentation updated
- [ ] Tests added/updated
- [ ] All tests pass
- [ ] No breaking changes
```

## 🐛 Reporting Bugs

### Before Reporting

1. Check if the bug has already been reported
2. Verify you're using the latest version
3. Test on Google Colab to rule out local issues

### Bug Report Template

```markdown
**Describe the bug**
Clear description of the bug.

**To Reproduce**
Steps to reproduce:

1. Go to '...'
2. Run '...'
3. See error

**Expected behavior**
What you expected to happen.

**Screenshots/Logs**
Add error messages or screenshots.

**Environment**

- OS: [e.g., Windows 11, Ubuntu 20.04]
- Python version: [e.g., 3.10]
- GPU: [e.g., T4, None]
- Colab or Local: [e.g., Google Colab]

**Additional context**
Any other relevant information.
```

## 💡 Feature Requests

### Feature Request Template

```markdown
**Feature Description**
Clear description of the proposed feature.

**Use Case**
Why is this feature needed? What problem does it solve?

**Proposed Solution**
How would you implement this feature?

**Alternatives Considered**
Other approaches you've thought about.

**Additional Context**
Any other relevant information, examples, or references.
```

## 🎯 Priority Areas for Contribution

### High Priority

1. **Model Improvements**
   - Support for additional base models (Gemma, Phi, etc.)
   - Improved prompt templates
   - Better handling of long contexts

2. **Dataset Enhancement**
   - Additional medical datasets integration
   - Data quality improvements
   - Multi-language support

3. **Evaluation**
   - More comprehensive metrics
   - Medical accuracy benchmarks
   - Bias and safety testing

### Medium Priority

4. **UI/UX**
   - Enhanced Gradio interface
   - Conversation history
   - Response citations

5. **Documentation**
   - Video tutorials
   - Use case examples
   - Troubleshooting guide

6. **Performance**
   - Inference optimization
   - Memory efficiency improvements
   - Faster training strategies

### Future Ideas

7. **Advanced Features**
   - RAG (Retrieval-Augmented Generation)
   - Multi-modal support (medical images)
   - Integration with medical databases
   - API endpoint

## 🔒 Medical Content Guidelines

**IMPORTANT**: All medical content must include appropriate disclaimers:

### When Adding Medical Information

- ✅ Educational content is welcome
- ✅ Citations from reputable sources
- ✅ Clear, accurate explanations
- ❌ No medical advice or diagnosis
- ❌ No unverified claims
- ❌ No dangerous information

### Medical Disclaimer Template

Always include this in documentation:

```
⚠️ DISCLAIMER: This is for educational purposes only.
Not a substitute for professional medical advice.
Consult healthcare professionals for medical decisions.
```

## 🧪 Testing Guidelines

### What to Test

1. **Data Loading**: Verify dataset loads correctly
2. **Preprocessing**: Check formatting and tokenization
3. **Training**: Ensure training completes without errors
4. **Inference**: Test model generates valid responses
5. **UI**: Verify Gradio interface works properly

### How to Test

```bash
# Run setup verification
python setup_check.py

# Test inference (after training)
python inference.py --question "What is diabetes?"

# Test in Colab
# Run entire notebook from top to bottom
```

## 📚 Resources

### Learning Resources

- [Hugging Face Transformers](https://huggingface.co/docs/transformers)
- [PEFT Documentation](https://huggingface.co/docs/peft)
- [LoRA Paper](https://arxiv.org/abs/2106.09685)
- [Medical NLP Resources](https://github.com/topics/medical-nlp)

### Project-Specific

- [Project README](README.md)
- [Configuration Guide](config.py)
- [Demo Video Guide](DEMO_VIDEO_GUIDE.md)

## 💬 Communication

### Questions?

- Open a GitHub Discussion
- Create an issue with the "question" label
- Check existing issues and discussions first

### Need Help?

- Review the README and documentation
- Check the troubleshooting section
- Ask in GitHub Discussions

## 🎖️ Recognition

Contributors will be:

- Listed in the project README
- Acknowledged in release notes
- Credited in relevant documentation

## 📄 License

By contributing, you agree that your contributions will be licensed under the same MIT License that covers the project. See [LICENSE](LICENSE) for details.

## ✅ Code of Conduct

### Our Standards

- Be respectful and inclusive
- Accept constructive feedback
- Focus on what's best for the project
- Show empathy towards others
- No harassment or trolling

### Enforcement

Violations may result in:

1. Warning
2. Temporary ban
3. Permanent ban

Report violations to [maintainer email/contact].

---

## 🙏 Thank You!

Every contribution, no matter how small, helps improve Kira Health Assistant. We appreciate your time and effort in making this project better!

**Happy Contributing! 🚀**
