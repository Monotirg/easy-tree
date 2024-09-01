from __future__ import annotations

import os

from typing import List, Iterator
from dataclasses import dataclass


@dataclass
class NodeFile:
    name: str
    path: str


@dataclass
class NodeDir:
    name: str
    path: str
    files: List[NodeFile]
    dirs: List[NodeDir]


class Tree:
    def __init__(self, root: str) -> None:
        path = os.path.normpath(root)
        name = os.path.basename(root)
        self.prefix = os.path.dirname(root)
        self.root = NodeDir(name, path, [], [])
        self.mapper = {path: self.root}
        
    @classmethod
    def load_dir(cls, root: str) -> Tree:
        tree = cls(root)
        
        for path in tree._iter_files():
            if os.path.isfile(path):
                tree._add_file(path)
            else:
                tree._add_dir(path)
        
        return tree
 
    def _iter_files(self) -> Iterator[str]:
        for path, dirs, files in os.walk(self.root.path):
            for file in files:
                yield os.path.join(path, file)

            if not (files or dirs):
                yield path

    def _add_file(self, path: str) -> None:
        subdir = os.path.dirname(path)
        self._add_dir(subdir)
            
        subdir_node = self.mapper[subdir]
        subdir_node.files.append(NodeFile(
            name=os.path.basename(path),
            path=path
        ))

    def _add_dir(self, path: str) -> None:
        subdirs = []

        while path not in self.mapper:
            subdirs.append(os.path.join(self.prefix, path))
            path = os.path.dirname(path)
            
        start = self.mapper[path]

        for subdir in subdirs:
            subdir_node = NodeDir(
                name=os.path.basename(subdir),
                path=subdir,
                files=[],
                dirs=[]
            )
            self.mapper[subdir] = subdir_node
            start.dirs.append(subdir_node)
            start = subdir_node 
    
    def __show(self, node_dir, indent) -> None:
        print(" " * indent + node_dir.name)
        indent += 4 

        for file in node_dir.files:
            print(" " * indent + file.name)
        
        for dir in node_dir.dirs:
            self.__show(dir, indent)

    def show(self) -> None:
        self.__show(self.root, 0) 
