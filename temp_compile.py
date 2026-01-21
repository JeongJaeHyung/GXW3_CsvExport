import py_compile
import glob

files = glob.glob("action/**/*.py", recursive=True) + glob.glob("module/**/*.py", recursive=True)

for file in files:
    try:
        py_compile.compile(file, doraise=True)
        print(f"Successfully compiled {file}")
    except py_compile.PyCompileError as e:
        print(f"Error compiling {file}: {e}")
