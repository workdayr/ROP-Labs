/* ctf03.c — CTF-03: Shellcode escondido (compilar con -z execstack) */
#include <stdio.h>

extern char *gets(char *s);

int main(void) {
    char buf[256];
    printf("Escribe: ");
    fflush(stdout);
    gets(buf);
    return 0;
}
