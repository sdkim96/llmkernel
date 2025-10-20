from .models import CPUDecision
from ..proc.models import ProcessControlBlock
from .._types import Event

class Kernel:

    def __init__(
        self,
        interrupt_handler: InterruptHandler,
        device_manager: DeviceManager,
        memory_manager: MemoryManager,
    ) -> None:

        self.interrupt_handler = interrupt_handler
        self.device_manager = device_manager
        self.memory_manager = memory_manager
        
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
            self.device_manager.call_agent(agent_id=id)
        elif type == "call_tool":
            self.device_manager.call_tool(tool_id=id)
        elif type == "read":
            self.memory_manager.read(pid=id)
        elif type == "write":
            self.memory_manager.write(pid=id)
        elif type == "exit":
            self._terminate_process(pid=id)


    async def _call_cpu(
        self,
        *,
        pid: str,
    ) -> CPUDecision: ...
    