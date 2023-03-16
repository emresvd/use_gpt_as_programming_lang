import ugptapl
import sys

path = sys.argv[-1]

with open(path, "r") as f:
    code = f.read()

u = ugptapl.UGPTapl(code)
u.translate_to_python_code()
u.run()
