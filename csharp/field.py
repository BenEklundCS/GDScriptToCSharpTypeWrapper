from typing import List


def field(line: str):
    # filter out gd script comments, and then split on the =
    export_split = line.split("#")[0].split("=")

    # replace until we get the fieldname
    field_name = export_split[0] \
        .replace("@export", "") \
        .replace("var", "") \
        .replace(":", "") \
        .strip()

    # parse the export split object for the datatype
    obj = parse(export_split[1])
    data_type = obj[1]

    return f"""
    [Export] public {data_type} {field_name} {{
        get => ({data_type})WrappedNode.Get("{field_name}");
        set => WrappedNode.Set("{field_name}", value);
    }}
            """



def parse(s: str) -> List:
    s = s.strip()

    low = s.lower()

    if low == "true" or low == "false":
        return [low, "bool"]

    try:
        return [float(low), "float"]
    except:
        pass

    try:
        return [int(low), "int"]
    except:
        pass

    return [s, "string"]


"""
example:

player.gd
extends CharacterBody3D
@export var SPEED := 10


->

Player.cs

public partial class Player : CharacterBody3D {
 [Export] public int SPEED = 10;   
}
"""
