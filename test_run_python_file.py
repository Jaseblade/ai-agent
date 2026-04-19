from functions.run_python_file import run_python_file


print(
    "Result for 'main.py' file:",
    f"\n{run_python_file("calculator", "main.py")}",
)

print(
    "Result for 'main.py' with arguments file:",
    f"\n{run_python_file("calculator", "main.py", ["3 + 5"])}",
)

print(
    "Result for 'tests.py' file:",
    f"\n{run_python_file("calculator", "tests.py")}",
)

print(
    "Result for '../main.py' file:",
    f"\n{run_python_file("calculator", "../main.py")}",
)

print(
    "Result for 'nonexistent.py' file:",
    f"\n{run_python_file("calculator", "nonexistent.py")}",
)

print(
    "Result for 'lorem.txt' file:",
    f"\n{run_python_file("calculator", "lorem.txt",)}",
)
