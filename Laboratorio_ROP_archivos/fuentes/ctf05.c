/* ctf05.c — CTF-05: Leak bajo ASLR */
#include <stdio.h>

extern char *gets(char *s);

int main(void) {
    char buf[64];
    puts("Escribe:");
    gets(buf);
    return 0;
}
