from typing import Any, Dict
from framework.workflow.core.block import Block
from framework.workflow.core.block.input_output import Input, Output
from datetime import datetime
import pytz

class TimeBlock(Block):
    """获取指定时区或服务器本地时间的Block"""
    name = "time_block"

    inputs = {
        "timezone": Input(name="timezone", label="时区", data_type=str, description="指定时区")
    }

    outputs = {
        "current_time": Output(name="current_time", label="当前时间", data_type=str, description="当前时间")
    }

    def execute(self, **kwargs) -> Dict[str, Any]:
        timezone = kwargs.get("timezone", "UTC")
        try:
            tz = pytz.timezone(timezone)
        except pytz.UnknownTimeZoneError:
            tz = pytz.UTC

        current_time = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        return {"current_time": current_time}
