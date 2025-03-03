import pandas as np

class NueralNetwork:

    def init(self, inputSize=784, hiddenLayers=(512,512), outputSize=10):
        self.inputSize = inputSize
        self.hiddenLayers = hiddenLayers
        self.outputSize = outputSize
        self.weights = []
        self.biases = []

        self.weights.append(0.01 * np.random.randn(inputSize, hiddenLayers(0)))
        self.biases.append(np.zeros((1, hiddenLayers(0))))

        for i in range(len(hiddenLayers)-1):
            self.weights.append(0.01 * np.random.randn(hiddenLayers(i+1), hiddenLayers(i+1)))
            self.biases.append(np.zeros((1, hiddenLayers(i+1))))

    def foward(self, inputs):
        layers = [inputs]

        for i in range(len(self.weights)):
            layers.append(np.dot(layers(-1), self.weights(i)) + self.biases(i))

        return layers[-1]
