def distribute_students(num_students):
    if num_students <= 60:
        num_classes = 2
    else:
        num_classes = num_students // 30 + 1

    class_size = num_students // num_classes
    remaining_students = num_students - class_size * num_classes

    # Distribute the students into classes
    allocation = {}
    for class_num in range(1, num_classes + 1):
        if remaining_students>0:
            allocation[f"Class {class_num}"] = class_size + 1
            remaining_students = remaining_students - 1
        else:
            allocation[f"Class {class_num}"] = class_size

    return f"Proposed Allocation: {num_classes} classes\n{allocation}"


# Example usage
num_students = 33
print(distribute_students(num_students))