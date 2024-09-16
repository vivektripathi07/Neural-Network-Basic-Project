import numpy as np

inputs = [[1.0, 2.0, 3.0, 2.5],
          [2.0, 5.0, -1.0, 2.0],
          [-1.5, 2.7, 3.3, -0.8]]

weights_matrix = [[0.2, 0.8, -0.5, 1.0],
                  [0.5, -0.91, 0.26, -0.5],
                  [-0.26, -0.27, 0.17, 0.87]]

biases = [2,3,0.5]

weights_matrix2 = [[0.1, -0.14, 0.5],
                  [-0.5, 0.12, -0.33],
                  [-0.44, 0.73, -0.13]]

biases2 = [-1, 2, -0.5]

layer1_output = np.dot(inputs, np.array(weights_matrix).T) + biases
print("Layer 1 output : \n", layer1_output)

layer2_output = np.dot(layer1_output, np.array(weights_matrix2).T ) + biases2
print("Layer 2 output : \n", layer2_output, "\n\n")


# Now we'll look into Object Layer

X = [[1.0, 2.0, 3.0, 2.5],
    [2.0, 5.0, -1.0, 2.0],
    [-1.5, 2.7, 3.3, -0.8]] # Using X is a standard in machine learning for denoting the input data.


class Layer_Dense:
    def __init__(self, n_inputs,n_neuron ):
        self.weight = 0.10 * np.random.rand(n_inputs, n_neuron)
        self.bias = np.zeros((1,n_neuron))

    def forward(self, inputs) : 
        self.output = np.dot(inputs, self.weight) + self.bias

layer1 = Layer_Dense(4,5)
layer2 = Layer_Dense(5,2)

layer1.forward(X)
layer2.forward(layer1.output)

print(layer2.output)