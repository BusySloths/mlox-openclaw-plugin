# mlox-openclaw-plugin

OpenClaw external plugin for MLOX

## Overview

This is an external plugin for [MLOX](https://github.com/BusySloths/mlox) that provides OpenClaw service installation and management capabilities. OpenClaw is a personal AI assistant you run on your own devices.

## Features

- Automatic installation of Node.js (v22+) via nvm
- OpenClaw CLI installation from npm
- Gateway service management (start/stop/status)
- Streamlit UI for configuration and monitoring
- Support for multiple install channels (latest, beta, dev)

## Installation

Install the plugin in the same Python environment as MLOX:

```bash
pip install mlox-openclaw-plugin
```

Or install from source:

```bash
git clone https://github.com/BusySloths/mlox-openclaw-plugin.git
cd mlox-openclaw-plugin
pip install -e .
```

## Usage

Once installed, the plugin will be automatically discovered by MLOX through Python entry points. The OpenClaw service will be available in MLOX's service catalog.

### Configuration

During setup, you can configure:

- **Install Channel**: Choose from `latest`, `beta`, or `dev` npm dist-tags

### After Installation

After the service is installed, run the onboarding wizard on the target server:

```bash
openclaw onboard --install-daemon
```

This completes the interactive setup for channels and credentials.

## Requirements

- Python >= 3.10
- busysloths-mlox >= 0.1.0
- Target server must support:
  - apt package manager (for system dependencies)
  - Node.js 22+ (automatically installed via nvm)

## Service Details

- **Service ID**: `openclaw-native`
- **Default Port**: 18789 (gateway)
- **Resource Requirements**:
  - CPUs: 2.0
  - RAM: 4.0 GB
  - Disk: 5.0 GB

## Links

- [OpenClaw Project](https://openclaw.ai)
- [OpenClaw Documentation](https://docs.openclaw.ai)
- [OpenClaw Releases](https://github.com/openclaw/openclaw/releases)
- [MLOX Documentation](https://busysloths.github.io/mlox/)

## License

MIT
