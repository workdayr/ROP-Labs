#!/bin/bash
# build.sh — Compila todos los binarios del laboratorio con flags inseguras.
# Uso:  ./build.sh   (debes estar en el directorio raiz del ZIP)
set -e

# Estructura esperada:
#   build.sh
#   fuentes/*.c
#   soluciones/*.py
# Este script crea bin/ y coloca ahi los binarios compilados.

ROOT="$(pwd)"
BIN="$ROOT/bin"
mkdir -p "$BIN"

# Flags estandar inseguras:
COMMON_FLAGS="-g -O0 -fno-stack-protector -no-pie"

echo "=== Compilando con flags: $COMMON_FLAGS (mas -z execstack donde aplique) ==="

# Binarios sin stack ejecutable (A0, A1, A2, A3, B1, B2, B3, B4, CTF-01, CTF-02, CTF-04, CTF-05, CTF-06):
for src in a0 a1 a2 a3 b1 b2 b3 b4 ctf01 ctf02 ctf04 ctf05 ctf06; do
    echo "  gcc $COMMON_FLAGS -o bin/$src fuentes/$src.c"
    gcc $COMMON_FLAGS -o "$BIN/$src" "fuentes/$src.c"
done

# Binarios con stack ejecutable (A4 y CTF-03):
for src in a4 ctf03; do
    echo "  gcc $COMMON_FLAGS -z execstack -o bin/$src fuentes/$src.c"
    gcc $COMMON_FLAGS -z execstack -o "$BIN/$src" "fuentes/$src.c"
done

echo "=== Compilacion completa. Binarios en $BIN ==="
echo ""
echo "Para verificar mitigaciones de cada binario:"
echo "  pwn checksec ./bin/a0"
echo "  pwn checksec ./bin/a4   # debe decir NX disabled"
