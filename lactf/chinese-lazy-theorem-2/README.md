## chinese-lazy-theorem-2
0. I read the proof of Chinese remainder theorm from this webpage: [https://www.math.cmu.edu/~mradclif/teaching/127S19/Notes/ChineseRemainderTheorem.pdf](https://www.math.cmu.edu/~mradclif/teaching/127S19/Notes/ChineseRemainderTheorem.pdf), the proof is clear and concise.

1. chinese remainder thm. for this question

    $$ x \equiv a1 \mod p $$

    $$ x \equiv a2 \mod q $$

    $$ N=p \times q $$

    $$ m1=N\div p=q $$

    $$ m2=N\div q=p $$

    $$ y1=modinv(m1\mod p, p) $$

    $$ y2=modinv(m2\mod q, q) $$

    $$ x0=(y1m1a1+y2m2a2)\%N $$

2. after we got x0, we can use ` x0 + iN for i=0~30 ` to guess the answer
