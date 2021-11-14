


if __name__ == "__main__":
    encrypt = UnbreakableEncryption()
    key1, key2 = encrypt.encrypt("Han Zaw Nyine")
    text = encrypt.decrypt(key1,key2)
    print(text)