import enum
import typing as t

from pydantic import BaseModel, Field

class SyscallType(enum.Enum):
    CALL_AGENT = "call_agent"
    CALL_TOOL = "call_tool"
    READ = "read"
    WRITE = "write"
    EXIT = "exit"


class CPUDecision(BaseModel):
    
    type: SyscallType = Field(
        ...,
        description="CPU 가 수행할 시스템 콜의 유형",
    )
    device_id: str = Field(
        ...,
        description="시스템 콜과 관련된 장치의 고유 식별자",
    )
    device_kwargs: dict = Field(
        default_factory=dict,
        description="시스템 콜에 전달될 추가 매개변수",
    )
    thoughts: t.List[str] = Field(
        ...,
        description="CPU 가 시스템 콜을 수행하기 전에 기록한 생각",
    )