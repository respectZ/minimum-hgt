@echo off
echo Compiling...
g++ -std=c++17 .\main.cpp .\enet\callbacks.c .\enet\compress.c .\enet\host.c .\enet\list.c .\enet\packet.c .\enet\peer.c .\enet\protocol.c .\enet\unix.c .\enet\win32.c -pthread -lws2_32 -lwinmm -fpermissive -w -o headless
echo Done.
pause