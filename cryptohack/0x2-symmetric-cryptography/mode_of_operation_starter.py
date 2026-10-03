import json

import requests


def request_api(endpoint: str) -> dict:
    BASE_URL = "http://aes.cryptohack.org/block_cipher_starter"
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


data = request_api("/encrypt_flag")
ciphertext = data.get("ciphertext")
print(f"[*] Requesting encrypted flag: \n{json.dumps(data, indent=4)}")


data = request_api(f"/decrypt/{ciphertext}")
print(f"[*] Requesting decrypted flag: \n{json.dumps(data, indent=4)}")
hex_flag = data.get("plaintext")
flag = bytearray.fromhex(hex_flag).decode()

print(f"Flag: {flag}")
