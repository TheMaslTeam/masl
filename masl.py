import argparse
import os
parser = argparse.ArgumentParser(description='Masl interpreter.')
parser.add_argument("filename")
args = parser.parse_args()
print("masl - v1.0 stable")
print("masl stands for 'Minimalistic and Simple programming Language'")
print("Copyright Masl Team 2025 | Licensed with MIT")
import masl_ast as ast
import masl_run as runner
file = args.filename[9:]
if os.path.exists(file):
    with open(file, "r") as f:
        print(runner.run(ast.parse(f.read())))
