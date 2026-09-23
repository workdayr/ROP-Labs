/* b4.c — Ejercicio B4: win con dos argumentos */
#include <stdio.h>
#include <stdlib.h>

extern char *gets(char *s);

void win(int a, int b) {
    if (a != 0xdead || b != 0xbeef) { puts("args incorrectos"); exit(1); }
    FILE *f = fopen("flag.txt", "r");
    if (!f) { puts("no flag"); exit(1); }
    char buf[128];
    fgets(buf, sizeof(buf), f);
    printf("FLAG: %s\n", buf);
}

int main(void) {
    char buf[64];
    printf("Escribe: ");
    fflush(stdout);
    gets(buf);
    return 0;
}
