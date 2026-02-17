# Development and Testing Guide

## Development Setup

### Prerequisites

- Python 3.10+
- pip and build tools
- Git

### Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/BusySloths/mlox-openclaw-plugin.git
   cd mlox-openclaw-plugin
   ```

2. Install in editable mode:
   ```bash
   pip install -e .
   ```

3. Verify installation:
   ```bash
   python3 -c "from importlib import metadata; print([ep for ep in metadata.entry_points().select(group='mlox.service_plugins') if ep.name == 'openclaw-native'])"
   ```

## Building the Package

### Build Distribution Files

```bash
# Install build tools
pip install build

# Build the package
python3 -m build
```

This creates:
- `dist/mlox_openclaw_plugin-0.1.0-py3-none-any.whl` - Wheel distribution
- `dist/mlox_openclaw_plugin-0.1.0.tar.gz` - Source distribution

### Verify the Build

```bash
# Check the wheel contents
python3 -c "import zipfile; z = zipfile.ZipFile('dist/mlox_openclaw_plugin-0.1.0-py3-none-any.whl'); print('\n'.join(z.namelist()))"

# Verify entry points
python3 -c "import zipfile; z = zipfile.ZipFile('dist/mlox_openclaw_plugin-0.1.0-py3-none-any.whl'); print(z.read('mlox_openclaw_plugin-0.1.0.dist-info/entry_points.txt').decode())"
```

## Testing

### Manual Plugin Testing

The repository includes a simple test script:

```bash
python3 test_plugin.py
```

This verifies:
- Entry point registration
- Plugin loading
- Configuration validation
- Service class availability

### Integration Testing with MLOX

1. Install the plugin:
   ```bash
   pip install -e .
   ```

2. Use MLOX to list services:
   ```bash
   mlox service list
   ```
   
   The `openclaw-native` service should appear in the list.

3. Check the service configuration:
   ```bash
   mlox service info openclaw-native
   ```

## Code Quality

### Syntax Check

```bash
python3 -m py_compile mlox_openclaw_plugin/*.py
```

### Type Checking (Optional)

If you have mypy installed:

```bash
pip install mypy
mypy mlox_openclaw_plugin/
```

## Publishing

### To Test PyPI

```bash
pip install twine
python3 -m build
twine upload --repository testpypi dist/*
```

### To Production PyPI

```bash
python3 -m build
twine upload dist/*
```

## Project Structure

```
mlox-openclaw-plugin/
├── mlox_openclaw_plugin/     # Main package
│   ├── __init__.py           # Package initialization
│   ├── plugin.py             # Entry point configuration
│   ├── native.py             # Service implementation
│   └── ui.py                 # Streamlit UI functions
├── pyproject.toml            # Project metadata and build config
├── README.md                 # User documentation
├── EXAMPLES.md               # Usage examples
├── DEVELOPMENT.md            # This file
└── LICENSE                   # MIT License

```

## Updating the Plugin

### Version Updates

1. Update version in `pyproject.toml`
2. Update version in `mlox_openclaw_plugin/__init__.py`
3. Build and test
4. Commit and tag:
   ```bash
   git commit -m "Bump version to X.Y.Z"
   git tag vX.Y.Z
   git push && git push --tags
   ```

### Node.js Version Updates

To update the Node.js version used by OpenClaw:

1. Edit `mlox_openclaw_plugin/native.py`
2. Update the constants:
   ```python
   NODEJS_VERSION = "vXX.Y.Z"  # New version
   NODEJS_MAJOR_MIN = XX       # Minimum major version
   ```

### Adding New Features

1. Make changes in the appropriate module
2. Update documentation (README.md, EXAMPLES.md)
3. Test locally
4. Run code review and security checks
5. Commit and publish

## Troubleshooting

### Plugin Not Discovered

If MLOX doesn't find the plugin:

1. Verify installation:
   ```bash
   pip list | grep mlox-openclaw
   ```

2. Check entry points:
   ```bash
   python3 -c "from importlib import metadata; print(list(metadata.entry_points().select(group='mlox.service_plugins')))"
   ```

3. Reinstall in editable mode:
   ```bash
   pip uninstall mlox-openclaw-plugin
   pip install -e .
   ```

### Import Errors

If you get import errors:

1. Ensure busysloths-mlox is installed:
   ```bash
   pip install busysloths-mlox
   ```

2. Check Python version (must be 3.10+):
   ```bash
   python3 --version
   ```

## Contributing

This plugin is maintained as part of the BusySloths organization. For contributions:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

MIT License - See LICENSE file for details
