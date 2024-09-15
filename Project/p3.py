import numpy as np

inputs = [1,2,3,2.5]
weights = [0.2,0.8,-0.5,1.0]
bias = 2

output = np.dot(weights, inputs) + bias

print(output)

# Here it is important to note that weights would come before the inputs while in the funtion np.dot(), here it isnt that big an issue but when we have multiple weights in form of a matrix then it can result in errors.

weights_matrix = [[0.2, 0.8, -0.5, 1.0],
                  [0.5, -0.91, 0.26, -0.5],
                  [-0.26, -0.27, 0.17, 0.87]]

biases = [2,3,0.5]

output_of_matrix = np.dot(weights_matrix, inputs) + biases

print(output_of_matrix)