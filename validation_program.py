import json

# Function definitions for validation
def validate_quads_and_points_grouping(annotation_data):
    errors = []

    for group in annotation_data["shape_groups"]:
        for shape in group["shapes"]:
            if shape["type"] == "polygon" and shape.get("tags", {}).get("Shape") == "Quad":
                if len(shape["key_locations"][0]["points"]) != 4:
                    errors.append(f'Quad in group {group["group_type"]} has an incorrect number of corners')

    return errors

def validate_quad_shape_corners(annotation_data):
    errors = []

    for group in annotation_data["shape_groups"]:
        for shape in group["shapes"]:
            if shape["type"] == "polygon":
                tags = shape.get("tags", {})
                if tags.get("Shape") == "Quad":
                    corners = shape["key_locations"][0]["points"]
                    if not is_clockwise_order(corners):
                        errors.append(f'Quad in group {group["group_type"]} has corners not in clockwise order')

    return errors


def is_clockwise_order(corners):
    total = 0
    for i in range(len(corners)):
        x1, y1 = corners[i]
        x2, y2 = corners[(i + 1) % len(corners)]
        total += (x2 - x1) * (y2 + y1)

    return total < 0

def validate_triangles(annotation_data):
    errors = []

    for group in annotation_data["shape_groups"]:
        for shape in group["shapes"]:
            if shape["type"] == "polygon":
                tags = shape.get("tags", {})
                if tags.get("Shape") == "Triangle":
                    errors.append(f'Triangle found in group {group.get("group_type", "None")}, which is not allowed')

    return errors


def validate_occlusion_values(annotation_data):
    errors = []

    for group in annotation_data["shape_groups"]:
        for shape in group["shapes"]:
            if "Occlusion" in shape["tags"]:
                errors.append(f'Occlusion values found in group {group["group_type"]}, which is not allowed')

    return errors

# Load the JSON data from the provided data
with open('q2.json') as f:
    annotations_data = json.load(f)

# Iterate through each annotation and perform validations
for task in annotations_data["tasks"]:
    annotation_data = task["answers"]["Annotation"]["layers"]["vector_tagging"]
    print(f"Validations for {task['data']['Name']} (Image URL: {task['data']['Image']})")

    validation_errors = []

    # Perform the specified validations
    validation_errors += validate_quads_and_points_grouping(annotation_data)
    validation_errors += validate_quad_shape_corners(annotation_data)
    validation_errors += validate_triangles(annotation_data)
    validation_errors += validate_occlusion_values(annotation_data)

    # Print any errors encountered during validations
    for error in validation_errors:
        print(f"  - {error}")

    if not validation_errors:
        print("No errors found.")
    print("\n")
