#!/usr/bin/env python3

import os
import shutil
import ansible_collections

root = ansible_collections.__path__[0]

for namespace in os.listdir(root):
    namespace = os.path.join(root, namespace)
    if not os.path.isdir(namespace):
        continue
    for collection in os.listdir(namespace):
        collection = os.path.join(namespace, collection)
        if not os.path.isdir(collection):
            continue
        for path in os.listdir(collection):
            path = os.path.join(collection, path)
            basename = os.path.basename(path)
            if basename != 'plugins':
                if os.path.isdir(path):
                    shutil.rmtree(path)
                else:
                    os.unlink(path)
            else:
                modules = os.path.join(path, 'modules')
                if os.path.isdir(modules):
                    shutil.rmtree(modules)
