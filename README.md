# Tree Directory Structure Viewer

This project provides a simple Python implementation to visualize a directory tree structure, starting from a given root folder. It maps the folder structure into objects, representing directories and files

## Features

- **Tree Representation**: Constructs a tree structure using `NodeDir` (directories) and `NodeFile` (files).
- **Readable Tree Display**: Prints the directory contents in a hierarchical format.
- **Efficient Lookup**: Uses a dictionary to map directories for fast access.

## Project Structure

### `NodeFile`
Represents a file in the directory structure.
```python
@dataclass
class NodeFile:
    name: str
    path: str
```

### `NodeDir`
Represents a directory in the directory structure.

```python
@dataclass
class NodeDir:
    name: str
    path: str
    files: List[NodeFile]
    dirs: List[NodeDir]
```

### `Tree`
Manages the construction and display of the directory tree.

```python
class Tree:
    def __init__(self, root: str) -> None
    def load_dir(cls, root: str) -> Tree
    def show(self) -> None
```

## Example Usage
```python
from easy_tree import Tree

# Load the directory tree
tree = Tree.load_dir("/path/to/root/directory")

# Get the root of tree (NodeDir)
root = tree.root

# Display the tree
tree.show()
```

## License
[MIT license](https://github.com/Monotirg/easy-tree/blob/main/LICENSE)
