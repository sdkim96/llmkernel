import typing as t

from .agent import AgentDevice
from .tool import ToolDevice
from .memory import MemoryDevice

from .._types.device import (
    Content,
    RegisterDevice
)



class DeviceManager:
    def __init__(
        self,
        devices: t.Dict[str, RegisterDevice],
    ) -> None:
        self.__devices = devices

        self.agents = AgentDevice(self)
        self.tools = ToolDevice(self)
        self.memories = MemoryDevice(self)


    def register(
        self,
        device: RegisterDevice
    ) -> bool:
        result = True
        if device.id in self.__devices:
            result = False
        else:
            self.__devices[device.id] = device
        return result


    def to_content(
        self, 
        *, 
        type: t.Literal["agent", "memory", "tool"],
        role: t.Literal["user", "system", "assistant"] | None = None
    ) -> Content:
        return Content(
            type=type,
            role=role,
            parts=[],
        )
