from .manager import DeviceManager


class MemoryDevice:

    def __init__(
        self,
        device_manager: DeviceManager
    ) -> None:
        self.device_manager = device_manager

    async def read(self, pid: str) -> None:
        pass

    async def write(self, pid: str) -> None:
        pass