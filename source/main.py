import sys, functools

USAGE = """Usage: misoperate.py stringToEncryptToMultiplicandsInAsm
Note that all characters in the string must be in ASCII form. Furthermore, the length of the input string must be of exactly sixty-four."""
STR_LEN = 64
CHUNK_CHARS = 4
ASM = """global      _start

section     .text

_start:
    mov     ebx,        0   ; The iterator index. Function calls do
                            ; not clobber this register in the Linux
                            ; ABI.
    sub     rsp,        4
    
.loop:
    mov     eax,        [factorArr+4*rbx]
    inc     ebx ; Get the next index
    
    ; Changing this instruction to `mul dword [factorArr+4*rbx]` 
    ; is the correction to make.
    mul     byte [factorArr+4*rbx]
    mov     [rsp],      rax ; Store the product in the stack.
    
    mov     edi,        1 ; File descriptor for standard output.
    mov     rsi,        rsp ; Pointer to source data.
    mov     edx,        4 ; Length of source data.
    mov     eax,        1 ; System call code for writing to a file.
    syscall ; Print product as ASCII characters
    
    inc     ebx ; Every iteration uses two subsequent indices.
    cmp     ebx,        32
    jnz     .loop
    
    mov     dword [rsp],      10
    mov     edi,        1
    mov     rsi,        rsp
    mov     edx,        4
    mov     eax,        1
    syscall ; Print a new line.
    
    add     rsp,        4
    xor     rdi,        rdi
    mov     rax,        60
    syscall

section .data

factorArr:
"""

def main(string) -> None:
    octoIter = (string[CHUNK_CHARS*i: CHUNK_CHARS*(i+1)] 
        for i in range(STR_LEN//CHUNK_CHARS))
    dwordDefinitionList = []
    for octuplet in octoIter:
        product = sum( ord(a)<<(8*i) for i, a in enumerate(octuplet) )
        root = int(product**0.5)
        factor_list = []
        factor = 2
        while factor < root:
            if product % factor == 0:
                factor_list.append(factor)
                product //= factor
                factor = 2
            else:
                factor += 1
        if product > 1:
            factor_list.append(product)
        
        print('Factors for the substring "' + octuplet + '":', factor_list)
        factorA = str(functools.reduce(lambda x, y: x*y, factor_list[:-1]))
        factorB = str(factor_list[-1])
        print('The two largest factors are', factorA, 'and', factorB)
        dwordDefinitionList.append('dd ' + factorA + ', ' + factorB)
    f = open('HACKME.asm', 'w')
    f.write(ASM + '\n'.join(dwordDefinitionList))
    f.close()
    return

if len(sys.argv) == 2 and len(sys.argv[1]) == STR_LEN:
    main(sys.argv[1])
else:
    print(USAGE)