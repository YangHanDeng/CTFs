##rev/universal
1. assume that the string is lactf{...}, so bytes[0]=66, bytes[1]=61 ... and so on.
2. in the code, ^0xff can be ignored because it does nothing to the result
3. another thing interesting is that every statement follows the pattern: `b1 ^ b2*7 ^ ~b3+13 = b4`
4. just brute force the rest of the bytes based on assumption in 1.

lactf{1_d0nt_see_3_b1ll10n_s0lv3s_y3t}