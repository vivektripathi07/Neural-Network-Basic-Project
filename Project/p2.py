input = [1, 2, 3]
weights = [.2, .8, -.5]
bias =  2

output = 0

for i in range(3):
    output += input[i]*weights[i]

output += bias

print(output)

# So what are inputs here? , the instructer answers this question as :
# Input can the values of input layer and the output we are getting would act as input to a single neuron in the hidden layer which may have the weights we have given and the bais we have taken.

input1 = [1, 2, 3, 2.5]
weights1 = [.2, .8, -.5, 1.0]
bias1 =  2

output1 = 0

for i in range(4):
    output1 += input1[i]*weights1[i]

output1 += bias1

print(output1)

# This example have conveys the fact that input can not only be from the input layer (lets say sensors) but also from a hidden layer to another hidden layer neuron or an output neuron.
# The calculations remains the same but the scope of the function changes.

#In p1 we modelled a single neuron using three inputs then in p2 we modelled a single neuron using four inputs.
#But now we will model three neurons using the four inputs, for the we'll need three weigth-sets and three biases.

input_for_new_model = [1, 2, 3, 2.5]

weight1_for_new_model = [.2, .8, -.5, 1.0]
weight2_for_new_model = [.5, -.91, .26, -.5]
weight3_for_new_model = [-.26, -.27, .17, 0.87]

bias1_for_new_model = 2
bias2_for_new_model = 3
bias3_for_new_model = 0.5

def ForOutput(arr1, arr2):
    out = 0;
    for i in range(4):
        out += arr1[i] * arr2[i]

    return out


output1_for_new_model = ForOutput(input_for_new_model, weight1_for_new_model) + bias1_for_new_model
output2_for_new_model = ForOutput(input_for_new_model, weight2_for_new_model) + bias2_for_new_model
output3_for_new_model = ForOutput(input_for_new_model, weight3_for_new_model) + bias3_for_new_model

print(output1_for_new_model)
print(output2_for_new_model)
print(output3_for_new_model)




    





