from functions.get_file_content import get_file_content


print("Result for 'lorem.txt' file:", f"\n{get_file_content("calculator", "lorem.txt")}")
print()
print("Result for 'main.py' file:", f"\n{get_file_content("calculator", "main.py")}")
print()
print("Result for 'pkg/calculator.py' file:", f"\n{get_file_content("calculator", "pkg/calculator.py")}")
print()
print("Result for '/bin/cat' file:", f"\n{get_file_content("calculator", "/bin/cat")}")
print()
print("Result for 'pkg/does_not_exist.py' file:", f"\n{get_file_content("calculator", "pkg/does_not_exist.py")}")
