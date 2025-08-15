# Contributing to ETL Agent

Thank you for considering contributing to ETL Agent! We welcome all forms of contributions, including bug reports, feature requests, documentation improvements, and code contributions.

## 🛠 Development Setup

1. **Fork** the repository and clone it locally
2. Set up the development environment:
   ```bash
   conda env create -f environment.yaml
   conda activate etl-agent
   pip install -e .[dev]  # Install development dependencies
   ```
3. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```

## 🐛 Reporting Issues

When reporting issues, please include:
- A clear description of the problem
- Steps to reproduce the issue
- Expected vs. actual behavior
- Environment details (Python version, OS, etc.)

## ✨ Feature Requests

We love new ideas! Open an issue with:
- A clear description of the feature
- The problem it solves
- Any relevant examples or references

## 🧪 Testing

Run the test suite with:
```bash
pytest tests/
```

## 📝 Pull Requests

1. Create a new branch for your feature/fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Make your changes and ensure tests pass
3. Update documentation as needed
4. Submit a pull request with a clear description of changes

## 📜 Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use type hints for all functions
- Keep functions small and focused
- Add docstrings for all public functions

## 📄 License

By contributing, you agree that your contributions will be licensed under the project's [MIT License](LICENSE).
