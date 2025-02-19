from dataclasses import dataclass

@dataclass
class TimeBlockConfig:
    """配置TimeBlock的类"""
    default_timezone: str = "UTC"  # 默认时区
