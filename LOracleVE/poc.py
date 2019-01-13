from Crypto.Util.number import *
import libnum

flag = 'flag{test}'
def enc(x):
    return pow(x,e,n)
def dec(y):
    return pow(y,d1,n)
def getKey():
    p = getPrime(512)
    q = getPrime(512)
    n = p*q
    phi = (p-1)*(q-1)
    e = 65537
    d = libnum.invmod(e,phi)
    return n, e, d, phi


flag = libnum.s2n('flag{haha}')
n, e, d, phi = getKey()
d1 = d & ((1 << ( 5 + size(n)//2)) - 1)
d_l = d & ((1 << (5+size(n)//2)) -1 )
print d
print '----------------------------------------------'
def main():
    prev = 0
    d_h = d >> (5 + size(n)// 2) << ( 5 + size(n) // 2)
    for i in range(65537):
        _d = (i*(n+1)+1)/e
        dh = _d >>(5+size(n)//2) << (5+size(n)//2)
        if dh == d_h:
            x = enc(flag)
            x2 = pow(x,2,n)
            part1 = dec(x2)
            part2 = pow(x2,dh,n)
            complete = part1*part2 % n
            plain = libnum.nroot(complete,2)
            print libnum.n2s(plain)
            print _d
            assert d_h + d_l == d
        prev = dh

if __name__ == '__main__':
    main()
