# OpenClaw Plugin Examples

This document provides examples of how to use the mlox-openclaw-plugin.

## Installation

### From PyPI (when published)

```bash
pip install mlox-openclaw-plugin
```

### From Source

```bash
git clone https://github.com/BusySloths/mlox-openclaw-plugin.git
cd mlox-openclaw-plugin
pip install -e .
```

## Verifying Installation

After installation, verify the plugin is discoverable:

```python
from importlib import metadata as importlib_metadata

# Check for the plugin
eps = importlib_metadata.entry_points()
for ep in eps.select(group='mlox.service_plugins'):
    if ep.name == 'openclaw-native':
        print(f"✓ Found plugin: {ep.name}")
        provider = ep.load()
        config = provider()
        print(f"  Service: {config.name}")
        print(f"  Version: {config.version}")
```

## Using with MLOX

Once installed, the plugin is automatically available in MLOX. The OpenClaw service will appear in the service catalog.

### Via MLOX CLI

List available services (OpenClaw should appear):

```bash
mlox service list
```

Install OpenClaw service:

```bash
mlox service install openclaw-native
```

### Via MLOX API

```python
from mlox.config import load_all_service_configs

# Load all service configs (including plugins)
configs = load_all_service_configs()

# Find OpenClaw
openclaw_config = None
for config in configs:
    if config.id == 'openclaw-native':
        openclaw_config = config
        break

if openclaw_config:
    print(f"Found OpenClaw: {openclaw_config.name}")
    print(f"Description: {openclaw_config.description_short}")
    print(f"Requirements: {openclaw_config.requirements}")
```

## Configuration Options

During setup, you can configure:

- **Install Channel**: Choose from:
  - `latest` - Latest stable release
  - `beta` - Beta releases
  - `dev` - Development builds

## Post-Installation Setup

After the service is installed on the target server, complete the setup:

```bash
# SSH into the target server
ssh user@server

# Run the OpenClaw onboarding wizard
openclaw onboard --install-daemon
```

This will guide you through:
- Channel configuration
- Credential setup
- Integration configuration

## Service Management

### Check Service Status

```python
from mlox.infra import Infrastructure
from mlox.config import load_service_config_by_id

# Load the service configuration
config = load_service_config_by_id('openclaw-native')

# Create infrastructure connection
infra = Infrastructure(...)  # Initialize with your infrastructure

# Get service instance
service = config.instantiate_service({
    '${MLOX_AUTO_PORT_GATEWAY}': '18789',
    '${OPENCLAW_INSTALL_CHANNEL}': 'latest',
    '${MLOX_USER_HOME}': '/home/user',
    '${MLOX_STACKS_PATH}': '/path/to/stacks',
})

# Check status
status = service.check(infra.connection)
print(f"Service status: {status['status']}")
```

### Access Service URLs

After installation, the service exposes:

- **Gateway URL**: `http://<host>:18789` (default)
  - Gateway control plane for OpenClaw
  - Multi-channel integrations

## Links

- [OpenClaw Project](https://openclaw.ai)
- [OpenClaw Documentation](https://docs.openclaw.ai)
- [OpenClaw GitHub](https://github.com/openclaw/openclaw)
- [MLOX Documentation](https://busysloths.github.io/mlox/)
