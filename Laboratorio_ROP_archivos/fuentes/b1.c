/* b1.c — Ejercicio B1: ret2win 64-bit */
#include <stdio.h>
#include <stdlib.h>

extern char *gets(char *s);

void win(void) {
    FILE *f = fopen("flag.txt", "r");
    if (!f) { puts("no hay flag"); exit(1); }
    char buf[128];
    fgets(buf, sizeof(buf), f);
    printf("FLAG: %s\n", buf);
    fclose(f);
}

int main(void) {
    char buf[64];
    printf("Escribe: ");
    fflush(stdout);
    gets(buf);
    return 0;
}
