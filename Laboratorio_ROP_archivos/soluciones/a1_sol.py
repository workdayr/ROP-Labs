#!/usr/bin/env python3
# A1: primer crash con 100 'A'
from pwn import process
io = process("./bin/a1")
io.sendline(b"A" * 100)
io.wait()
print("exit code:", io.returncode)  # esperado: -11 (SIGSEGV)
