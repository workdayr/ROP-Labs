/* ctf06.c — CTF-06: setup() + win() en una cadena */
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

extern char *gets(char *s);

int fd_global;

void setup(int fd) {
    fd_global = open("flag.txt", O_RDONLY);
    if (fd_global < 0) { puts("no flag"); return; }
    printf("[setup] fd_global = %d\n", fd_global);
}

void win(int fd, int n) {
    char buf[256];
    int r = read(fd_global, buf, n);
    if (r <= 0) { puts("read failed"); return; }
    write(1, buf, r);
}

int main(void) {
    char buf[64];
    printf("Escribe: ");
    fflush(stdout);
    gets(buf);
    return 0;
}
