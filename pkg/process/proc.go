package process

import "sync"

type ProcessState int

const (
	New ProcessState = iota
	Ready
	Running
	Waiting
	Terminated
)

type ProcessControlBlock struct {
	PID         int
	Name        string
	State       ProcessState
	Description string
	Context     map[string]interface{}
}

// Process 구조체는 유저의 요청을 처리하는 실제 프로세스를 정의합니다.
type Process struct {
	pcb *ProcessControlBlock
	mu  sync.Mutex
}

// 실제 프로세스의 syscall에 해당하는 메서드들
type Syscall interface {
	CallAgent() error
	CallTool() error
}
