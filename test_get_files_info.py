from functions.get_files_info import get_files_info


print("Result for current directory:", f"\n{get_files_info("calculator", ".")}")
print()
print("Result for 'pkg' directory:", f"\n{get_files_info("calculator", "pkg")}")
print()
print("Result for '/bin' directory:", f"\n{get_files_info("calculator", "/bin")}")
print()
print("Result for '../' directory:", f"\n{get_files_info("calculator", "../")}")
