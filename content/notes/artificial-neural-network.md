---
title: "Artificial Neural Network: The Building Block Nobody Explains Well"
description: "What a neural network actually is, how it learns, and why it's both simpler and stranger than the hype suggests."
date: 2024-03-01
tags: ["AI", "neural-networks", "explainer", "machine-learning"]
draft: false
---

![A diagram showing a simple neural network with input layer, hidden layer, and output layer connected by arrows](https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Colored_neural_network.svg/640px-Colored_neural_network.svg.png)
*Image credit: Wikimedia Commons*

## The Smallest Unit of the Marvel

Before transformers. Before attention. Before LLMs. There was the [Artificial Neural Network](https://en.wikipedia.org/wiki/Artificial_neural_network). The humble building block that started it all.

Back in 2013, when none of this was the talk of the town, neural networks were quietly fascinating. Not because they were powerful. They were not. Compared to today, they were weak. Slow. Limited.

But the idea was beautiful.

## What Is a Neural Network, Really?

A neural network is simple at its core. A bunch of numbers connected together in layers.

Here is the basic structure:

- **Input layer** – receives raw data. Pixels of an image. Words in a sentence. Sensor readings.
- **Hidden layers** – where the computation happens. One or many. Sometimes hundreds.
- **Output layer** – produces the final prediction. A category. A number. A sentence.

![Diagram of a neuron showing inputs, weights, sum, activation function, and output](https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/ArtificialNeuronModel_english.png/640px-ArtificialNeuronModel_english.png)
*Image credit: Wikimedia Commons*

Each connection between neurons has a [weight](https://en.wikipedia.org/wiki/Artificial_neuron#Weights). A number that gets multiplied with the input. Each neuron has a [bias](https://en.wikipedia.org/wiki/Bias_(artificial_neural_network)). Another number added at the end. Each neuron has an [activation function](https://en.wikipedia.org/wiki/Activation_function). A simple mathematical rule that decides whether the neuron "fires" or not.

## How Does It Learn?

The magic is not in the structure. The magic is in the learning process.

Here is what happens:

1. Feed an input through the network. Get an output.
2. Compare the output to the correct answer. Calculate the [loss](https://en.wikipedia.org/wiki/Loss_function).
3. Figure out how much each weight contributed to the error.
4. Adjust every weight slightly to reduce the error.
5. Repeat. Thousands of times. Millions of times.

That third step is called [backpropagation](https://en.wikipedia.org/wiki/Backpropagation). It is the engine that makes neural networks work. Without it, the network would just be a random function. With it, the network gradually improves.

![Animation showing weights being adjusted during backpropagation](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Backpropagation_animated.gif/640px-Backpropagation_animated.gif)
*Image credit: Wikimedia Commons*

## Why "Neural"?

The name comes from biology. [Biological neurons](https://en.wikipedia.org/wiki/Neuron) in the brain receive signals through dendrites. If the signal is strong enough, the neuron fires and sends a signal down its axon to other neurons.

An artificial neuron does something similar. It receives inputs. Multiplies them by weights. Sums them up. Passes the sum through an activation function. Produces an output.

![Comparison of biological neuron and artificial neuron](https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Neuron_Hand-tuned.svg/640px-Neuron_Hand-tuned.svg.png)
*Image credit: Wikimedia Commons*

But here is the important distinction. A real neuron is a living cell. It has chemistry. Metabolism. Complexity that nobody fully understands.

An artificial neuron is a math equation.

The similarity is loose. Inspirational. Not literal.

## Types of Neural Networks

Over the years, researchers developed different architectures for different problems.

### Feedforward Neural Network (FNN)

The simplest type. Information moves in one direction. Input to output. No loops. No memory. Good for basic classification tasks.

### Convolutional Neural Network (CNN)

Designed for images. Uses a sliding window (called a [kernel](https://en.wikipedia.org/wiki/Kernel_(image_processing))) to detect edges, shapes, and patterns. Learns to recognize features anywhere in the image.

![CNN architecture showing convolution and pooling layers](https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Typical_cnn.png/640px-Typical_cnn.png)
*Image credit: Wikimedia Commons*

### Recurrent Neural Network (RNN)

Designed for sequences. Sentences. Time series. Audio. Has loops that allow information to persist. Struggles with long sequences due to vanishing gradients. Largely replaced by transformers.

### Autoencoder

Learns to compress input into a smaller representation and then reconstruct it. Used for [dimensionality reduction](https://en.wikipedia.org/wiki/Dimensionality_reduction) and anomaly detection.

## The Universal Approximation Theorem

Here is a strange fact about neural networks.

The [Universal Approximation Theorem](https://en.wikipedia.org/wiki/Universal_approximation_theorem) states that a feedforward neural network with a single hidden layer can approximate any continuous function. Any function. To arbitrary accuracy.

Sounds magical. But there is a catch.

The theorem does not say the network will be easy to train. It does not say the network will use a reasonable number of neurons. It just says the network exists. Finding the right weights is a different problem entirely.

## Where Neural Networks Struggle

Despite all the excitement, neural networks have real limitations.

**Data hunger.** A neural network needs thousands or millions of examples to learn. A human child needs a handful.

**Black box problem.** Knowing why a network made a prediction is difficult. [Explainable AI](https://en.wikipedia.org/wiki/Explainable_artificial_intelligence) tries to solve this.

**Overfitting.** The network memorizes training data instead of learning general patterns. [Regularization](https://en.wikipedia.org/wiki/Regularization_(mathematics)) helps but does not eliminate the risk.

**Catastrophic forgetting.** When trained on a new task, the network forgets old tasks. The [stability-plasticity dilemma](https://en.wikipedia.org/wiki/Continual_learning) remains unsolved.

## The Journey from Then to Now

That small neural network built back in 2013 was not impressive. It could not write poetry. It could not hold a conversation. It could barely recognize handwritten digits.

But the same mathematics powers today's largest models. The same [gradient descent](https://en.wikipedia.org/wiki/Gradient_descent). The same backpropagation. The same activation functions.

Scale changed everything. But the core remained.

A neural network is still just a bunch of numbers connected together, trained by trial and error, slowly adjusting to reduce its mistakes.

That simplicity is what makes it beautiful.

![Evolution of neural networks from simple to deep](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Deep_Learning_Journal_Header_Image.jpg/640px-Deep_Learning_Journal_Header_Image.jpg)
*Image credit: Wikimedia Commons*

## A Final Thought

Artificial neural networks are not brains. They are not intelligent. They do not understand what they learn.

But they are useful. Remarkably useful. And the fact that such a simple idea — multiply, sum, activate, repeat — can produce the behavior we see today is genuinely surprising.

The same mathematics. The same building blocks. Just more of them.

From a mechanics perspective, that is elegance. Simple rules. Complex emergent behavior. The universe does the same thing with particles and forces.

Maybe that is why neural networks feel familiar to anyone who has studied physics. Same pattern. Different domain.

---

*Related reading: [AI – The Buzzword](/notes/ai-the-buzzword/)*
