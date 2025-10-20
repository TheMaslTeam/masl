def run(parsed):
    vars = {}
    result = ""
    for node in parsed:
        if node["node_type"] == "assign":
            vars[node["name"]] = node["data"]
            result += f"[debug] :: {node['name']} = {node['data']}\n"
        elif node["node_type"] == "print_raw":
            result += f"[debug] :: print '{node['which']}'\n"
            print(node['which'])
        elif node["node_type"] == "var_print":
            result += f"[debug] :: print var {node['which']}\n"
            print(vars[node["which"]])
    return result
