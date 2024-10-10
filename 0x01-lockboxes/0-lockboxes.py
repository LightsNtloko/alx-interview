def canUnlockAll(boxes):
    n = len(boxes)
    opened_boxes = set([0])
    stack = [0]

    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key not in opened_boxes and key < n:
                opened_boxes.add(key)
                stack.append(key)

    return len(opened_boxes) == n
