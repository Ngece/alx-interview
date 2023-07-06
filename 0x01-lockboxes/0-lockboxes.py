def canUnlockAll(boxes):
    if not boxes:
        return False

    # Initialize variables
    num_boxes = len(boxes)
    visited = [False] * num_boxes
    visited[0] = True

    # Use a queue to perform breadth-first search
    queue = [0]

    # Explore the boxes using breadth-first search
    while queue:
        # Get the next box from the queue
        box = queue.pop(0)

        # Check each key in the current box
        for key in boxes[box]:
            # If the key corresponds to a valid box and it hasn't been visited
            if key < num_boxes and not visited[key]:
                visited[key] = True  # Mark the box as visited
                queue.append(key)  # Add the box to the queue for further exploration

    return all(visited)
