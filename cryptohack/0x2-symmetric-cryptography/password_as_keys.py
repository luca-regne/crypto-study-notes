import hashlib
import json
import requests
from Crypto.Cipher import AES


def request_api(endpoint: str) -> dict:
    BASE_URL = "http://aes.cryptohack.org/passwords_as_keys"
    r = requests.get(f"{BASE_URL}/{endpoint}")

    return r.json()


if __name__ == "__main__":
    enc_data = request_api("/encrypt_flag")
    ciphertext_hash = enc_data.get("ciphertext")
    ciphertext = bytes.fromhex(ciphertext_hash)
    print(f"[*] Requesting encrypted flag: \n{json.dumps(enc_data, indent=4)}")

    # /usr/share/dict/words from
    r = requests.get(
        "https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words"
    )
    for w in r.text.split("\n"):
        # print(w)
        key = hashlib.md5(w.encode()).digest()

        try:
            cipher = AES.new(key, AES.MODE_ECB)
            decrypted = cipher.decrypt(ciphertext)
            candidate = decrypted.decode()
        except Exception:
            continue

        if not candidate.startswith("crypto{"):
            continue

        print(f"Decrypted Flag: {candidate} \nPassword: {w}")

        dec_data = request_api(f"/decrypt/{ciphertext.hex()}/{key.hex()}")
        print(f"[*] Confirming password:  \n{json.dumps(dec_data, indent=4)}")
        hex_flag = dec_data.get("plaintext")
        flag = bytearray.fromhex(hex_flag).decode()
        if flag == candidate:
            print(f"Flag verified remotely: {flag}")
        break
