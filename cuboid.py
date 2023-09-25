import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image

# Create the output directory if it doesn't exist
output_dir = 'q1-output'
output_dir_text = 'q1-output1'
os.makedirs(output_dir, exist_ok=True)
os.makedirs(output_dir_text, exist_ok=True)

# Original cuboid vertices
point_arr = np.array([[20,0,0], [20,0,10], [0,0,0], [0,0,10], [20,10,0], [20,10,10], [0,10,0], [0,10,10]])

# Define the scaling factors
length_scale = 10
width_scale = 20
height_scale = 30

# Choose a vertex as the reference point for scaling
reference_vertex = point_arr[0]

# Scale the cuboid
scaled_point_arr = np.array([
    reference_vertex + length_scale * (point - reference_vertex) if idx % 2 == 0
    else reference_vertex + width_scale * (point - reference_vertex) if idx % 4 < 2
    else reference_vertex + height_scale * (point - reference_vertex)
    for idx, point in enumerate(point_arr)
])

# Prepare vertices for plotting
original_faces = [[point_arr[0], point_arr[1], point_arr[5], point_arr[4]],
                  [point_arr[2], point_arr[3], point_arr[7], point_arr[6]]]

scaled_faces = [[scaled_point_arr[0], scaled_point_arr[1], scaled_point_arr[5], scaled_point_arr[4]],
                [scaled_point_arr[2], scaled_point_arr[3], scaled_point_arr[7], scaled_point_arr[6]]]

# Visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the original cuboid
original_collection = Poly3DCollection(original_faces, alpha=0.25, color='b')
ax.add_collection3d(original_collection)

# Plot the scaled cuboid
scaled_collection = Poly3DCollection(scaled_faces, alpha=0.25, color='r')
ax.add_collection3d(scaled_collection)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_xlim([0, 600])
ax.set_ylim([0, 300])
ax.set_zlim([0, 900])

# Save the plot as an image
output_file_path = os.path.join(output_dir, 'cuboid_visualization.png')
plt.savefig(output_file_path)
plt.close(fig)

# Save the assumptions as text
output_file_path_text = os.path.join(output_dir_text)
plt.savefig(output_file_path_text)
plt.close(fig)

# Create a text file to list the assumptions
assumptions = """
Assumptions:
1. The given vertex at index 0 is chosen as the reference point for scaling.
2. Scaling is applied independently along each axis (x, y, z) based on the provided scaling factors.
3. The cuboid is assumed to have a certain orientation, and scaling is applied accordingly.
4. Visualization assumes a fixed orientation for the cuboid to show the effects of scaling clearly.
"""

with open(os.path.join(output_dir_text, 'assumptions.txt'), 'w') as file:
    file.write(assumptions)

print("assumptions saved successfully at:", output_file_path_text)
print("screenshot saved successfully at:", output_file_path)
