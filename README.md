# Sama Implementations Engineering Technical Excercise

At Sama our expertise lies in annotating training data for computer vision models. We excel in various areas, including image and 3D annotation applications, performance benchmarking metrics, and tools for seamless integration of customer data pipelines. Providing top-notch training data is deeply ingrained in our DNA, and we are committed to delivering exceptional services in this domain.

To learn more about Sama and our offerings, you can find detailed information on our website [here](https://www.samasource.com/). Our website provides comprehensive insights into our services, case studies, success stories, and the industries we serve.

## Note

We anticipate that the exercises should take about a couple hours. We are more interested in your approach than perfection.

## Exercise 1

Use the code snippet below as a starting point for your script. Your script will need to generate a cuboid with the following conditions:
1. Scale the length by factor of 10
2. Scale the width by factor of 20
3. Scale the height by factor of 30
4. Using a 3D library of your choice visualize both the unscaled cuboid and the scaled cuboid
5. Save a screenshot of the visualization into a folder called `q1-output`
6. In the `q1-output1` folder create a text or markdown file and list all the assumptions you made while solving this exercise. <br>

<b> Note: <br> </b>
You must pick a vertex as the reference point to scale from (do not use the center of the cuboid) 

```python
import numpy as np

point_arr = np.array([[20,0,0], [20,0,10], [0,0,0], [0,0,10], [20,10,0], [20,10,10], [0,10,0], [0,10,10]])
```

## Exercise 2 
Write a program in python that takes a json file (q2.json) as input. The json contains the annotations on some sample image data. Create a validation program that lists all the errors in the annotations.

### List of validations to perform
1. Quads and points should be grouped such that a group contains exactly one quad and one point
2. Verify that each quad shape has exactly four corners
3. Ensure that the corners of the quad shape are marked in clockwise order, starting from the top left corner. Ignore this check if any of the corners are marked as occluded
4. Only one triangle should be present
5. Triangles should not be grouped
6. Triangles and points should not have occlusion values <br>
<b>Note:</b> If you have any additional validations that you consider important, please feel free to add them.

## General instructions

Please clone this repository and share the response with abha2

Best of luck!
