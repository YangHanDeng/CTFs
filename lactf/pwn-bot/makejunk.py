from pwn import *
import sys

junk = cyclic(200)
prefix = b"give me the flag\0"

sys.stdout.buffer.write(prefix + junk)
