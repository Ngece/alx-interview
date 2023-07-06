#!/usr/bin/env python3

def canUnlockAll(boxes):
    if not boxes:
        return False

    num_boxes = len(boxes)
    visited = [False] * num_boxes
    visited[0] = True
    queue = [0]

    while queue:
        box = queue.pop(0)
        for key in boxes[box]:
            if key < num_boxes and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
