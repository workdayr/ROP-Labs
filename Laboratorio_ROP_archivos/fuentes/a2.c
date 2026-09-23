/* a2.c — Ejercicio A2 — radiografía GDB */
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
