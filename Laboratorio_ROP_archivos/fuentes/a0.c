/* a0.c — Ejercicio A0 — primer binario */
#include <stdio.h>
#include <stdlib.h>

/* gcc moderno no declara gets(); lo declaramos a mano */
extern char *gets(char *s);

int main(void) {
    char buf[64];
    printf("Escribe: ");
    fflush(stdout);
    gets(buf);
    printf("Lei: %s\n", buf);
    return 0;
}
