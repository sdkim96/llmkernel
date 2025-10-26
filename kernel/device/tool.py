from .manager import DeviceManager


class ToolDevice:

    def __init__(
        self,
        device_manager: DeviceManager
    ) -> None:
        self.device_manager = device_manager
        
    async def call(self, tool_id: str) -> None:
        pass