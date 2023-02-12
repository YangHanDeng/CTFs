## hill-easy

In the beginning of the code, it will generate an 20x20 matrix A

our strategy is to rebuild A based on first 10 trials and get the flag in last trial.

the following is how the program encode:
```
1. for every char c in string:
     append ord(c)-32 to array N
2. matrix multiplication AxN
3. turn the result into char
```
to send inputs, I utilized 2 characters:
1. " "(space): ord(" ")=32, 32-32=0
2. "!": ord("!")=33, 33-32=1

so if I send 20 spaces, but change the first space to "!", the response will be the first column of A in char string version

I did it on the rest of the 19 spaces as well, then I got 20 columns of A (10 trials * 2 input per trial)

The remaining part is trivial. I changed the A's char string into numpy array, and also changed the fakeflag2 into numpy array, did matrix multiplication, and sent the 2 results I got.

Then, I got the flag!

lactf{tHeY_SaiD_l!NaLg_wOuLD_bE_fUN_115}

