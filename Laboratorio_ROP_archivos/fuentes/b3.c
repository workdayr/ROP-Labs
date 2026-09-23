/* b3.c — Ejercicio B3: ret2win con argumento */
#include <stdio.h>
#include <stdlib.h>

extern char *gets(char *s);

void win(int code) {
    if (code != 0x1337) { puts("codigo incorrecto"); exit(1); }
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
