from .manager import DeviceManager


class AgentDevice:

    def __init__(
        self,
        device_manager: DeviceManager
    ) -> None:
        self.device_manager = device_manager

    async def call(self, agent_id: str) -> None:
        return self.device_manager.to_content(
            type="agent",
            role="user",
        )