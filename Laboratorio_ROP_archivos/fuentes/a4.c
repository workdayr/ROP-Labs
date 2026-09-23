/* a4.c — Ejercicio A4: ret2shellcode (compilar con -z execstack) */
#include <stdio.h>

extern char *gets(char *s);

int main(void) {
    char buf[256];
    printf("Escribe: ");
    fflush(stdout);
    gets(buf);
    return 0;
}
