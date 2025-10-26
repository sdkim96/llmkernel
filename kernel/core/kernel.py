from ..device import DeviceManager
from .models import CPUDecision
from ..proc.models import ProcessControlBlock
from .._types import Event

class Kernel:

    def __init__(
        self,
        device_manager: DeviceManager,
        scheduler
    ) -> None:

        self.device_manager = device_manager
        self._pcbs: dict[str, ProcessControlBlock] = {}

    async def start_process(
        self,
    ) -> ProcessControlBlock: ...
    

    async def syscall(
        self,
        *,
        type: str,
        id: str,
        **kwargs,
    ) -> Event:

        if type == "call_agent":
            await self.device_manager.agent.call(agent_id=id)
        elif type == "call_tool":
            await self.device_manager.tool.call(tool_id=id)
        elif type == "read":
            await self.device_manager.memory.read(pid=id)
        elif type == "write":
            await self.device_manager.memory.write(pid=id)
        elif type == "exit":
            await self._terminate_process(pid=id)


    async def call_cpu(
        self,
        *,
        pid: str,
    ) -> CPUDecision: ...
    