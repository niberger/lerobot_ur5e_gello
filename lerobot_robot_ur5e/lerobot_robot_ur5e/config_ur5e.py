"""Configuration dataclass for the UR5e robot plugin.

Defines UR5EConfig with robot IP.
"""

from dataclasses import dataclass, field
from lerobot.cameras.configs import ColorMode, Cv2Rotation
from lerobot.cameras import CameraConfig
from lerobot.robots import RobotConfig

@RobotConfig.register_subclass("ur5e")
@dataclass
class UR5EConfig(RobotConfig):
    ip: str
    cameras: dict[str, CameraConfig]
