from pwn import xor


def xor(str1: bytes, str2: bytes) -> bytes:
    return bytes(a ^ b for a, b in zip(str1, str2))


# KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
# KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
# KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
# FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf

# Basically we can simply latest expression to
# FLAG ^ (KEY1) ^ (KEY3 ^ KEY2) = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf
# FLAG ^ a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313 ^ c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf
# and then using Commutative propoerty
# FLAG = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313 ^ c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1 ˆ 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf

k1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
k2_xor_k3 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
xor_all_result = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")
flag = xor(xor(k1, k2_xor_k3), xor_all_result)
print(flag.decode())
