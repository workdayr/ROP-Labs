/* b2.c — Ejercicio B2: ret2libc estatico+ASLR off */
#include <stdio.h>

extern char *gets(char *s);

int main(void) {
    char buf[64];
    printf("Escribe: ");
    fflush(stdout);
    gets(buf);
    return 0;
}
