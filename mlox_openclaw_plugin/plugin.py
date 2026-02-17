"""OpenClaw external plugin for MLOX."""

from mlox.config import BuildConfig, ServiceConfig


def _build_config(config_id: str, path: str, class_name: str) -> ServiceConfig:
    """Build a ServiceConfig for OpenClaw."""
    cfg = ServiceConfig(
        id=config_id,
        name="OpenClaw",
        version="latest",
        maintainer="MLOX Contributors",
        description="OpenClaw is a personal AI assistant you run on your own devices. It provides a gateway control plane and multi-channel integrations. This native service installs the OpenClaw CLI and runs the gateway on a VPS.",
        description_short="OpenClaw is a personal AI assistant you run on your own devices.",
        links={
            "project": "https://openclaw.ai",
            "documentation": "https://docs.openclaw.ai",
            "changelog": "https://github.com/openclaw/openclaw/releases",
        },
        build=BuildConfig(
            class_name=class_name,
            params={
                "name": config_id,
                "template": "${MLOX_STACKS_PATH}/openclaw/mlox.openclaw.native.yaml",
                "target_path": "${MLOX_USER_HOME}/openclaw",
                "port": "${MLOX_AUTO_PORT_GATEWAY}",
                "install_channel": "${OPENCLAW_INSTALL_CHANNEL}",
            },
        ),
        groups={
            "service": {},
            "assistant": {},
            "backend": {"native": {}},
        },
        ui={
            "setup": "mlox_openclaw_plugin.ui.setup",
            "settings": "mlox_openclaw_plugin.ui.settings",
        },
        requirements={
            "cpus": 2.0,
            "ram_gb": 4.0,
            "disk_gb": 5.0,
        },
        ports={
            "gateway": 18789,
        },
    )
    cfg.path = path
    return cfg


def service_plugin() -> ServiceConfig:
    """Entry point for the OpenClaw service plugin."""
    return _build_config(
        config_id="openclaw-native",
        path="external/mlox.openclaw.native.yaml",
        class_name="mlox_openclaw_plugin.native.OpenClawNativeService",
    )
