package core

import "pkg/process"

type Core struct{}

func (c *Core) Fetch() *process.Process
func (c *Core) Decide(proc *process.Process) *process.Process
