from Crypto.Util.strxor import strxor
pt = b"Long ago, the four nations lived together in harmony ..."
ct = bytes.fromhex("200e0d13461a055b4e592b0054543902462d1000042b045f1c407f18581b56194c150c13030f0a5110593606111c3e1f5e305e174571431e")
print(strxor(pt, ct))
#result: b'lactf{b4by_h1t_m3_0ne_m0r3_t1m3}lactf{b4by_h1t_m3_0ne_m0'