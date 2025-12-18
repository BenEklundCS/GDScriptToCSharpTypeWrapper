def method(line: str):
    return ""

    """
    TODO: Implement method to get param types and return types somehow hmm
    split = line.split("(")
    name = split[0].replace("func", "").strip()

    start_params = line.find("(")
    end_params = line.find(")")
    params = line[start_params + 1: end_params]

    print(name)

    return f"public {'override' if name.startswith('_') else ''} void {name}({params})"
    """
