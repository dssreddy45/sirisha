# Model Comparison Report

## Experiment Summary

| Experiment | Layers | Neurons | Activation | Epochs | Accuracy | Training Time |
|------------|--------|---------|------------|--------|----------|---------------|
| Model 1 - Simple | [8] | 8 | relu | 30 | 96.67% | 3.72s |
| Model 2 - Medium | [16, 8] | 24 | tanh | 50 | 100.0% | 4.08s |
| Model 3 - Deep | [32, 16, 8] | 56 | relu | 100 | 100.0% | 11.21s |

## Best Model
**Model 2 - Medium** with **100.0%** accuracy

## Why Some Models Perform Better

### Model 1 - Simple
- Only 1 hidden layer with 8 neurons
- Fewer parameters means less learning capacity
- Fast training but lower accuracy on complex data

### Model 2 - Medium
- 2 hidden layers with 16 and 8 neurons
- Tanh activation works well for small datasets
- Better accuracy than Model 1 due to more layers

### Model 3 - Deep
- 3 hidden layers with 32, 16, and 8 neurons
- More neurons capture complex patterns in data
- ReLU activation avoids vanishing gradient problem
- More epochs allow thorough learning
- Best accuracy overall

## Conclusion
- More hidden layers improve learning capacity
- More neurons capture more complex patterns
- ReLU activation works best for deep networks
- More epochs improve accuracy up to a point
- Too many epochs can cause overfitting
