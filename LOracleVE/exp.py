from pwn import *
import libnum
from Crypto.Util.number import *
import math

p = remote('edu-ctf.zoolab.org', 20000)

cflag = 0
n = 143478849721328647366796911317725983054855395296689849876355890490977050877093615453463907857688818222940306623114121603052359629389224881416760794497488308298634922765593669975308852960521414077388041660169581895295559651229956692632096543860973583128797426555854713074086760619798915777231115935781932644167 
e = 65537
c = 67153106998122890542103543974604486279543330843819610485820928904913732092354739912925915959785458003556019130659381977912671905611435652711312050194641410735084380385732769305116630376418477270947866157447749260206143295733278735083815603511030962303982996228607119970855046702209638269077596053207030437021

def decrypt(x):
    p.recvuntil('> ')
    p.sendline('2')
    p.recvuntil('c = ')
    p.sendline(str(x))
    p.recvuntil('m = ')
    return int(p.recvuntil('\n',drop=True))

def enc(x):
    return pow(x,e,n)
"""
def main():
    a = enc(2)
    b = enc(3)

    ca = decrypt(a)
    cb = decrypt(b)
    print ca
    print cb
    for i in xrange(100):
        tmp = cb + n*i
        if tmp % 3 == 0:
            ca = tmp
            dx = math.log(ca,3)
            print dx
"""



def main():
    c2 = pow(c,2,n)
    part1 = 81055037145724201485673632772568076401103709583674153721946531252824980118690557130774998445631293408100882490941542342880000648278658387268245646959453032199847257281984144928856837671776492000291945624919434678014923574534032625608230056095152354229450812494136246387466907500405096931872921786700900471781
    print part1
    
    for i in range(28680,65537):
        print i 
        _d = ( i * (n + 1) + 1 ) / e
        d_h = _d >> (5 + size(n)//2 ) <<(5 + size(n)//2)
        print size(_d)
        # m^2e mod n
        
        part2 = pow(c2,d_h,n)

        
        
        complete = (part1 * part2) % n
        m = libnum.nroot(complete , 2) 
        print libnum.n2s(m)

if __name__ == '__main__':
    main()


