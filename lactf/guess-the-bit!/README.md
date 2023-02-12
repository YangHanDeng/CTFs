## guess-the-bit!

According to `chall.py` , if bit=0, it will send c^2, and if bit=1, it will send 6*c^2

Notice that 6 doesn't have an integer square root, so we can take advantage of it.

Our plan is find square root of the received value c'
```
if isqrt(c')*isqrt(c') == c
then bit=0
else bit=1
```

flag: lactf{sm4ll_pla1nt3xt_sp4ac3s_ar3n't_al4ways_e4sy}
