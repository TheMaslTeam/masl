def parse(code):
    ast = []
    lines = code.split("\n")
    for line in lines:
        l = line.split(" ")
        if not l:
            continue
        if l[0] == "var":
            if l[2] != "=":
                print("Syntax error: assign operator needs to be at 3 offset")
                exit()
            to_define = ""
            for i, f in enumerate(l):
                if i >= 3:
                    to_define += str(f+" ")
            type = to_define.split("|")[0]
            to = to_define.split("|", 1)[1]
            if type == "ls":
                dict = to.split(",")
                data = []
                for i, n in enumerate(dict):
                    type_elem = n.split("-")[0]
                    if type_elem == "int":
                        data.append(int(n.split("-", 1)[1]))
                    elif type_elem == "str":
                        data.append(str(n.split("-", 1)[1].split("'", 1)[0]))
                    elif type_elem == "float":
                        data.append(float(n.split("-", 1)[1]))
                ast.append({"node_type": "assign", "data": data, "name": l[1]})
            elif type == "str":
                ast.append({"node_type": "assign", "data": str(to.split("'", 1)[0]), "name": l[1]})
            elif type == "int":
                ast.append({"node_type": "assign", "data": int(to), "name": l[1]})
            elif type == "float":
                ast.append({"node_type": "assign", "data": float(to), "name": l[1]})
        elif l[0] == "printvar":
            ast.append({"node_type": "var_print", "which": l[1]})
        elif l[0] == "printr":
            ast.append({"node_type": "print_raw", "which": line.split(" ", 1)[1]})
    return ast
