import uuid
import typing as t
from pydantic import BaseModel, Field


class RegisterDevice(BaseModel):
    id: str = Field(
        default_factory=lambda: "dev_" + str(uuid.uuid4()),
        description="디바이스의 고유 식별자입니다."
    )
    name: str = Field(
        description="디바이스의 이름입니다."
    )
    description: str = Field(
        description="디바이스의 설명입니다."
    )
    fn: t.Callable[..., t.Awaitable] = Field(
        description="디바이스가 수행하는 비동기 함수입니다."
    )

class SQLResponse(BaseModel):
    """ SQL 쿼리의 결과를 나타냅니다.
    
    """
    dialect: str = Field(
        description="SQL 방언 (예: 'sqlite', 'postgresql' 등)"
    )
    rows: t.List[t.Dict[str, t.Any]] = Field(
        description="쿼리 결과의 행들입니다."
    )

class Part(BaseModel):
    """ 모든 데이터가 해당 형태로 표현됩니다.
    
    """
    text: str | None = Field(
        default=None,
        description="부분의 실제 텍스트 내용입니다."
    )
    is_thought: bool | None = Field(
        default=False,
        description="이 부분이 사고(thought)를 나타내는지 여부입니다."
    )
    sql_response: SQLResponse | None = Field(
        default=None,
        description="SQL 쿼리의 결과입니다."
    )

    @classmethod
    def from_text(cls, *, text: str) -> "Part":
        return cls(text=text)
    
    @classmethod
    def from_sql_response(cls, *, dialect: str, rows: t.List[t.Dict[str, t.Any]]) -> "Part":
        sql_response = SQLResponse(
            dialect=dialect,
            rows=rows
        )
        return cls(sql_response=sql_response)

class Content(BaseModel):
    parts: t.List[Part] = Field(
        description="내용의 부분들입니다."
    )
    type: t.Literal["agent", "memory", "tool"] = Field(
        description="내용의 출처 (어떤 device에서 비롯되었는지) 나타냅니다."
    )
    role: t.Literal["user", "system", "assistant"] | None = Field(
        default=None,
        description=""" 해당 내용이 'agent' 인 경우에만 사용됩니다. """
    )
