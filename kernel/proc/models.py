import enum
import typing as t

from pydantic import BaseModel, Field

class ProcessState(enum.Enum):
    NEW = 0
    READY = 1
    RUNNING = 2
    WAITING = 3
    TERMINATED = 4

class ProcessControlBlock(BaseModel):
    pid: str = Field(
        ...,
        description="Process 의 고유 식별자",
    )
    state: ProcessState = Field(
        ...,
        description="Process 의 현재 상태",
    )
    run_stack: t.List[str] = Field(
        default_factory=list,
        description="Process 의 실행 스택",
    )