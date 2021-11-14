from django.shortcuts import render
from  django.http import HttpResponse
from secrets import token_bytes


# Create your views here.
def home(request):
    return render(request,'unbreakApp/master.html')
def index(request):
    return render(request,'unbreakApp/index.html',{'status':'can you decrypt'})

def encrypt(request):
    encryptText =  request.POST['encryptText']
    if encryptText != '':
        print(encryptText)
        unbreakable = unbreakableEncryption()
        key1,key2 = unbreakable.encrypt(encryptText)
        # encrypt(encryptText)
        print(key1,key2)
        return render(request, 'unbreakApp/index.html', {'encryptKey1': key1, 'encryptKey2': key2,'status':'encrypted your text'})
    else:
        return index(request)

def decrypt(request):
    decryptKey1 = request.POST['decryptKey1']
    decryptKey2 = request.POST['decryptKey2']
    if decryptKey1 != '' and decryptKey2 != '':
        print(decryptKey2,decryptKey1)
        unbreakable = unbreakableEncryption()
        decryptText= unbreakable.decrypt(int(decryptKey1),int(decryptKey2))
        return  render(request,'unbreakApp/index.html',{'decryptText':decryptText,'status':'Decrypted your text'})
    else:
        return  index(request)

class unbreakableEncryption:
    def random_key(self,length: int) -> int:
        # generate length random bytes
        tb: bytes = token_bytes(length)
        # convert those bytes into a bit string and return it
        return int.from_bytes(tb, "big")

    def encrypt(self,original: str) -> tuple[int, int]:
        original_bytes: bytes = original.encode()
        dummy: int = self.random_key(len(original_bytes))
        original_key: int = int.from_bytes(original_bytes, "big")
        encrypted: int = original_key ^ dummy  # XOR
        return dummy, encrypted


    def decrypt(self,key1: int, key2: int) -> str:
        decrypted: int = key1 ^ key2  # XOR
        temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")
        #print('aaa',temp.decode())
        return temp.decode()