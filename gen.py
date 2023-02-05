import os

s = "@echo off\necho Compiling...\ng++ -std=c++17 "
for (root, dirs, files) in os.walk("."):
    # print(root)
    # print(dirs)
    # print('--------------------------------')
    for file in files:
        if "test" in root:
            continue
        if ".cpp" in file or ".c" in file:
            print(f"{root}\{file}")
            s += f"{root}\{file} "

s += "-pthread -lws2_32 -lwinmm -fpermissive -w -o headless\necho Done.\npause"
with open("./compile.bat", "w") as f:
    f.write(s)
