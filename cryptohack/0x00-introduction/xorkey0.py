from pwn import xor

secret = bytes.fromhex(
    "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
)

for i in range(17):
    b = i.to_bytes(1, byteorder="big")
    dec = xor(secret, b).decode("utf-8")
    if dec.startswith("crypto{"):
        print(f"Byte Secret: {b}\nFlag: {dec}")
