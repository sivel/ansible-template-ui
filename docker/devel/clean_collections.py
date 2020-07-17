#!/usr/bin/env python3

import os
import shutil

root = '/root/.ansible/collections/ansible_collections'

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
