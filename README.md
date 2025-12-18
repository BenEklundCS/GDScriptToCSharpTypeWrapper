# GDScript → C# Type Wrapper

A CLI tool that generates a C# *wrapper node* for a Godot GDScript (`.gd`) class, enabling C# code to read and write exported GDScript fields through Godot’s dynamic property system (`Get` / `Set`).

The generated wrapper is intended to be attached to a scene and configured in the editor alongside the original GDScript-driven node.

---

## Overview

Given a GDScript file, the tool:

- Reads the script source
- Detects the script’s parent type via `extends`
- Identifies exported fields (`@export`)
- Generates a C# wrapper class that:
  - Inherits from `Node`
  - Exposes an exported `WrappedNode` reference of the original parent type
  - Mirrors exported GDScript fields as C# properties
  - Forwards all property access to the wrapped instance via `Get` and `Set`

The wrapper does **not** replace the original GDScript. It acts as a typed façade over the same runtime object.

---

## Usage

```
python GDScriptToCSharpTypeWrapper.py path/to/MyScript.gd --classname MyWrapper
```

---

## Generated Structure

The generated C# class follows this structure:

- `Node`-derived wrapper
- `[Export] WrappedNode` field pointing to the GDScript instance
- One C# property per exported GDScript field
- Property getters and setters delegate directly to `WrappedNode.Get(...)` and `WrappedNode.Set(...)`

Example excerpt:

```csharp
public partial class PlayerWrapper : Node
{
    [Export] public CharacterBody3D WrappedNode;

    [Export] public float speed
    {
        get => (float)WrappedNode.Get("speed");
        set => WrappedNode.Set("speed", value);
    }
}
