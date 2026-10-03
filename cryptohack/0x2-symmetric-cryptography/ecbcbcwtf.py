import json

import requests


def request_api(endpoint: str) -> dict:
    BASE_URL = "http://aes.cryptohack.org/ecbcbcwtf"
    r = requests.get(f"{BASE_URL}/{endpoint}")

    if r.status_code != 200:
        print(
            "[-] Error: "
            + f"\nStatus code: {r.status_code}"
            + f"\nRaw Response: \n{r.text}"
        )
        return {}
    data = r.json()

    return data


def xor_bytes(b1, b2):
    """XOR two byte strings byte-by-byte."""
    return bytes(a ^ b for a, b in zip(b1, b2))


BLOCK_LENGTH = 32  # 16 bytes = 32 hex characters

data = request_api("/encrypt_flag")
ciphertext = data.get("ciphertext")
print(f"[*] Requesting encrypted flag: \n\n{json.dumps(data, indent=4)}")


ciphertext_blocks = [
    ciphertext[i : i + BLOCK_LENGTH] for i in range(0, len(ciphertext), BLOCK_LENGTH)
]
# print(ciphertext_blocks)
iv = ciphertext_blocks[0]  # IV = first 16 bytes
ciphertext_blocks = ciphertext_blocks[1:]  # Remaining blocks are the cipher flag

print(f"Extracted IV (hash): {iv}")
print(f"Extracted ciphertext blocks: {ciphertext_blocks}")

ecb_decrypted_blocks = []
for b in ciphertext_blocks:
    data = request_api(f"/decrypt/{b}/")
    print(f"\n[*] Requesting decrypted flag: {b} \n\n{json.dumps(data, indent=4)}")
    decryped_block = data.get("plaintext")
    ecb_decrypted_blocks.append(decryped_block)

print(f"\n[*] Decrypted blocks (hash): {ecb_decrypted_blocks}")
plaintext = b"".join(
    xor_bytes(bytes.fromhex(decrypted_block), bytes.fromhex(previous_block))
    for decrypted_block, previous_block in zip(
        ecb_decrypted_blocks, [iv, *ciphertext_blocks[:-1]]
    )
)
print(plaintext.decode("utf-8"))
