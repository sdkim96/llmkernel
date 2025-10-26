import typing as t

from .models import ProcessControlBlock, ProcessState
from ..core.kernel import Kernel
from .._types import Event

class Process:

    def __init__(
        self,
        kernel: Kernel,
        query: str,
        
    ) -> None:
        self.kernel = kernel
        self.query = query

    async def run(self) -> t.AsyncGenerator[Event, None]:
        _pcb = await self.kernel.start_process(pcb=self.pcb)
        while self.pcb.state != ProcessState.TERMINATED:
            decision = await self.kernel.call_cpu(pid=self.pcb.pid)
            if decision.type == "syscall":
                await self.kernel.syscall(
                    type=decision.syscall_type,
                    id=self.pcb.pid,
                    **decision.params,
                )
            yield Event(data=f"Process {self.pcb.pid} yielded control.")


    async def call_agent(
        self,
        *,
        agent_id: str,
    ) -> Event: 
        await self.kernel.syscall(
            type="call_agent", 
            id=agent_id
        )
    async def call_tool(
        self,
        *,
        tool_id: str,
    ) -> Event: 
        await self.kernel.syscall(
            type="call_tool", 
            id=tool_id
        )

    async def read(
        self, 
        *, 
        memory_id: str
    ) -> Event: 
        await self.kernel.syscall(
            type="read", 
            id=memory_id
        )


    async def write(
        self, 
        *, 
        memory_id: str, 
        data: str
    ) -> Event: 
        await self.kernel.syscall(
            type="write", 
            id=memory_id, 
            data=data
        )
