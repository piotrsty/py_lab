from pathlib import Path


#path = Path("package1")
#print(path.exists())
#path = Path("emails")
#print(path.mkdir())
#print(path.rmdir())

path = Path()
for file in path.glob('*.py'):
    print(file)