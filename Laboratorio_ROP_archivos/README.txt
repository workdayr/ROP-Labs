Laboratorio_ROP_archivos.zip
====================================================================

Contenido companion de la guia "Laboratorio de Prácticas: Buffer Overflow
y ROP en Kali Linux (x86_64)". Este ZIP contiene las fuentes C de todos
los ejercicios y CTFs, los exploits pwntools resueltos de las Partes A y B
(las Partes C y D debes resolverlas tu), el script build.sh que compila
todo, y este README.

ESTRUCTURA
----------
  fuentes/        15 archivos .c (A0-A4, B1-B4, CTF-01..06)
  soluciones/       9 archivos .py (exploits pwntools de A y B)
  build.sh          script de compilacion
  README.txt        este archivo

USO
---
  1. Descomprime el ZIP dentro de ~/rop-lab/ :
       cd ~
       unzip Laboratorio_ROP_archivos.zip -d ~/rop-lab
       cd ~/rop-lab
  2. Compila todos los binarios:
       chmod +x build.sh
       ./build.sh
  3. Verifica mitigaciones de un binario:
       pwn checksec ./bin/a0
  4. Ejecuta una solucion (por ejemplo, A3):
       cd soluciones
       python3 a3_sol.py
  5. Para los CTFs, crea el flag.txt correspondiente:
       echo "FLAG{ctf1_alineacion_clasica}" > ../bin/flag.txt
       cd ../bin
       python3 ../soluciones/ctf01_sol.py  # (no incluido; ver Apendice A del PDF)

REQUISITOS
----------
  - Kali Linux 64-bit (o Debian/Ubuntu x86_64) actualizado
  - Paquetes: gdb build-essential gcc python3-pwntools python3-venv
              git curl wget socat ropgadget ropper
  - GEF instalado (ver Capitulo 2 del PDF)
  - Para exploits de la Parte B con libc hardcodeada: ajustar la base
    de libc con `ldd ./bin/b2` (ASLR off) y el offset del gadget
    `pop rdi; ret` con ROPgadget sobre tu libc.

AVISO DE USO RESPONSABLE
------------------------
Todas las tecnicas de este laboratorio se practican exclusivamente sobre
binarios que tu mismo compilas dentro de tu maquina virtual Kali Linux
aislada. Aplicar estas tecnicas contra sistemas de terceros -aunque sea
"solo para ver si funciona"- es ilegal y eticamente inaceptable. En
Mexico, el Codigo Penal Federal (articulos 211 bis y 211 ter) sanciona
el acceso no autorizado a sistemas informaticos; existen figuras
equivalentes en otros paises de America Latina.

La posesion de herramientas de explotacion no es delito; el acceso no
autorizado si lo es. Este ZIP y la guia asociada no te autorizan a usar
estas tecnicas fuera de tu VM.

Version: 2026.1
