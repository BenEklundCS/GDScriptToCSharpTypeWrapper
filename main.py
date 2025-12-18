import argparse

from utils import read, write
from csharp.field import field
from csharp.method import method
from csharp.c_class import c_class

verbose: bool = False


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="GDScriptToCSharpTypeWrapper",
        description=(
            "Generates a strongly-typed C# wrapper from a Godot GDScript (.gd) class. "
            "The generated wrapper enables C# code to load a provided GDScript instance (attached in editor)"
            "and access its exported properties and methods via Godot's Get, Set, and Call APIs."
        ),
        epilog="Author: Benjamin Eklund (2025)"
    )

    parser.add_argument('filename')
    parser.add_argument('--classname')

    args = parser.parse_args()

    classname = args.classname

    gdscript_tp_c_sharp_type_wrapper(args.filename, classname)


def gdscript_tp_c_sharp_type_wrapper(filename, classname=None) -> None:
    in_lines = read(filename)
    out_lines = []
    parent_class_name = None

    for line in in_lines:
        if "@export " in line:
            out_lines.append(field(line))
        if "func" in line:
            out_lines.append(method(line))
        if "extends" in line:
            parent_class_name = line.replace("extends", "").replace(" ", "")

    new_filename = filename.replace(".gd", ".cs")
    formatted = "\n".join(f"\t{line}" for line in out_lines)

    if not parent_class_name:
        raise Exception("No parent class found.")

    class_name = classname if classname else filename.replace(".gd", "")

    write(new_filename, c_class(class_name, parent_class_name, formatted))


if __name__ == '__main__':
    main()
