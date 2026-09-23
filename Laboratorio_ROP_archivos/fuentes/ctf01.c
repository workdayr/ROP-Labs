/* ctf01.c — CTF-01: Regreso a win */
#include <stdio.h>
#include <stdlib.h>

extern char *gets(char *s);

void win(void) {
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
