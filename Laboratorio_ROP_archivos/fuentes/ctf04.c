/* ctf04.c — CTF-04: ret2libc sin "/bin/sh" en binario */
#include <stdio.h>

extern char *gets(char *s);

int main(void) {
    char buf[64];
    printf("Escribe: ");
    fflush(stdout);
    gets(buf);
    return 0;
}
