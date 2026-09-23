#!/usr/bin/env python3
# A0: verificacion de entorno (no exploit)
from pwn import process
io = process("./bin/a0")
io.sendline(b"hola")
print(io.recvall(timeout=2).decode())
