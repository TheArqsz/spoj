import struct
def printfloat(f):
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])
    
n = int(input())
for i in range(n):
    p_f  = printfloat(float(input())).strip('0x').ljust(8, '0')
    list_p_f = [p_f[i] + p_f[i+1] + ' ' for i in range(0, len(p_f)-1,2)]
    final = ''
    for chars in list_p_f:
        if chars.strip() == '00':
            final += '0 '
        else:
            final += chars
    print(final.strip())