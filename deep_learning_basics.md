# Deep Learning Basics

---

## 1. Neural Network
- A model inspired by the human brain made of connected neurons
- Learns patterns from data by adjusting weights during training
- Used in image recognition, speech recognition, and fraud detection

---

## 2. Layers

### Input Layer
- First layer that receives raw data
- Number of neurons equals number of input features
- No computation, only passes data forward

### Hidden Layer
- Middle layers where actual learning happens
- Extracts patterns like edges, shapes, and features
- More hidden layers means deeper and smarter network

### Output Layer
- Final layer that gives the prediction
- Binary classification has 1 neuron, multi-class has N neurons
- Produces final result like cat or dog, spam or not spam

---

## 3. Activation Functions

### ReLU
- Returns x if positive, returns 0 if negative
- Most widely used activation function in deep learning
- Used in hidden layers of CNNs and deep networks

### Sigmoid
- Outputs values between 0 and 1
- Converts numbers into probabilities
- Used in output layer for binary classification

### Tanh
- Outputs values between -1 and 1
- Better than Sigmoid for hidden layers
- Used in RNNs and NLP tasks

### Softmax
- Converts scores into probabilities that sum to 1
- Each output is the probability of belonging to a class
- Used in output layer for multi-class classification

---

## 4. Training Concepts

### Epoch
- One complete pass through the entire training dataset
- Too few epochs causes underfitting
- Common values are 10, 50, 100

### Batch Size
- Number of samples processed before updating weights
- Small batch is more accurate, large batch is faster
- Common values are 16, 32, 64, 128

### Learning Rate
- Controls how much weights are updated each step
- Too high overshoots, too low learns very slowly
- Common values are 0.001 and 0.0001

### Loss Function
- Measures how wrong the model predictions are
- Goal of training is to minimize the loss
- Types: MSE for regression, Cross-Entropy for classification

### Optimizer
- Algorithm that updates weights to minimize loss
- Adam is the most popular optimizer
- Others include SGD, RMSprop, Adagrad

### Gradient Descent
- Core algorithm used to train neural networks
- Calculates gradient and updates weights to reduce loss
- Types: Batch, Stochastic, Mini-batch gradient descent

---
