#!/usr/bin/env python3
from base64 import *
import random
import codecs
e = 'x1FtPcm9gAtLVXFmCkINH7INJd6/aFI/M6SlYjh6T+iqnN97SfdfClZC9Ms3fDfyQhIeq1oP'

seed = 1547167075
flag = b64decode(e)
print(len(flag))
random.seed(seed)
e1 = flag[:len(flag)//2]
e2 = flag[len(e1):]
flag1 = ''
for c in e1:
    t = random.randrange(256)
    flag1 += chr(c ^ t)
print(len(flag1))
print(flag1)


with codecs.open('common.txt',"r",encoding='utf-8',errors='ignore') as fdata:
    f = fdata.read()
f = f.split('\n')


for i in f:
    i = i.encode('utf-8')
    seed2 = int.from_bytes(i,'little')
    random.seed(seed2)
    flag2 = ''
    for i in e2:
        ch = chr(i ^random.randrange(256))
        flag2 += ch
    if ch == '}':
        print(flag2)


