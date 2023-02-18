## pwn/bot
1. with ghidra, we can read the binary file's machine code and find out that the `cat flag.txt` is at 0x40129a

2. we have want to find out where is return address of main function (rip), so that we can overwrite 0x40129a on it.

  first way is using solve1.py, it can attach the process to gdb and let us check rip
  * `tmux`
  * on the right window `c` to continue
  * `info frame`
  then we can see the solution

  the second way is using makejunk.py, then 
  ```
  gdb ./bot
  b main 
  c
  info frame
  ```
  the result is ...706161616f61, be aware that linux is little endian
  the string is aoaaapaa...

3. use solve2.py to verify my solution
we can see the `HI` in our screen

4. connect to remote server with solve3.py
then we got the answer!
