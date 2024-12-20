import numpy as np
example_input = [1, .2, .1, .05, .2]
example_weights = [.2, .12, .4, .6, .90]

input_vector = np.array(example_input)
weights = np.array(example_weights)
bias_weight = .2
activation_level = np.dot(input_vector, weights) + (bias_weight * 1)
threshold = 0.5
if activation_level >= threshold:
    perceptron_output = 1
else:
    perceptron_output = 0
perceptron_output


expected_output = 0
new_weights = []
for i, x in enumerate(example_input):
    new_weights.append(weights[i] + (expected_output - perceptron_output) * x)
weights = np.array(new_weights)





sample_data = [[0, 0],
  [0, 1],
  [1, 0],
  [1, 1]]
expected_results = [0,
 1,
 1,
 1]
from random import random
import numpy as np
weights = np.random.random(2)/1000
bias_weight = np.random.random() / 1000
activation_threshold = 0.5

for idx, sample in enumerate(sample_data):
    input_vector = np.array(sample)
    weights = np.array(weights)
    activation_level = np.dot(input_vector, weights) + (bias_weight * 1)
    if activation_level > activation_threshold:
        perceptron_output = 1
    else:
        perceptron_output = 0
    print('Predicted {}'.format(perceptron_output))
    print('Expected: {}'.format(expected_results[idx]))
    print()






