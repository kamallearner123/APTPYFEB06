import os

print(os.cwd())

os.chdir('..')
print(os.cwd())

for i in os.listdir():
    print(i)

# recursive walk
for file, dir in os.walk('.'):
    print(file, dir)