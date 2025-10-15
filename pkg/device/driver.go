package device

// driver는 실제로 IO 하드웨어 장치를 제어하는 역할을 고수준으로 추상화 합니다.
type Driver interface {
	Call() error
	Interrupt() error
}
