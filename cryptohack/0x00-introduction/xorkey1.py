from pwn import xor

secret_bytes = bytes.fromhex(
    "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
)

flag_start = b"crypto{"

secret_key: list = []

for index, sb in enumerate(secret_bytes[: len(flag_start)]):
    for key_byte in range(256):
        candidate = sb ^ key_byte

        if candidate == flag_start[index]:
            print(
                f"position={index}, "
                f"cipher={sb:#04x}, "
                f"plaintext={chr(candidate)!r}, "
                f"key_byte={key_byte:#04x}"
            )
            secret_key.append(key_byte)
            break

print(f"Secret key: {bytes(secret_key).decode()}") # myXORke
flag = xor(secret_bytes, b"myXORkey") 
print(f"Flag: {flag.decode()}")
