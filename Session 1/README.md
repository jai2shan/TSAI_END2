# Assignment 1
### Group Members
Santosh Boina - santoshb183@gmail.com              
Sai Ashok Kumar Reddy - saiashokumareddy@gmail.com                
Jayasankar Raju S - muralis2raj@gmail.com             


## What is a neural network neuron?
A neuron is a function, which multiplies all the input variables with weight and  fed into an activation function which spits value that is the output of the neuron. Weights of the input variables are defined/decided in such a way that output of the all the neurons together gives us the better predicted output.
A neural network is combination of multiple groups of neurons which are sequentially connected.

The neuron translates inputs into a single output, which can then be picked up as input for another layer of neurons later on. The neuron is nothing more than a set of inputs, a set of weights, and an activation function. The neuron translates these inputs into a single output, which can then be picked up as input for another layer of neurons later on.

While details can vary between neural networks, the function f(x1,x2,…,xn) is often just a weighted sum:
###       <div align="center">     *f(x1,x2,…,xn)=w1⋅x1+w2⋅x2+...+wn⋅xn <div>*
Each neuron has a weight vector w=(w1,w2,...,wn), where n is the number of inputs to that neuron. These inputs can be either the 'raw' input features — say temperature, precipitation, and wind speed for a weather model — or the output of neurons from an earlier layer.

The weights for each neuron are turned during the training stage such that the final network output is biased toward some value (usually 1) for signal, and another (usually -1 or 0) for background.

Non-linear behavior in a neural network is accomplished by use of an activation function (often a sigmoid function) to which the output of f is passed and modified. This allows neural networks to describe more complicated systems while still combining inputs in a simple fashion.

##### Source : https://stats.stackexchange.com/questions/241888/what-are-neurons-in-neural-networks-how-do-they-work/241904

## What is the use of the learning rate? 
In machine learning and statistics, the learning rate is a tuning parameter in an optimization algorithm that determines the step size at each iteration while moving toward a minimum of a loss function. Since it influences to what extent newly acquired information overrides old information, it metaphorically represents the speed at which a machine learning model "learns".      

The learning rate controls how quickly the model is adapted to the problem. Smaller learning rates require more training epochs given the smaller changes made to the weights each update, whereas larger learning rates result in rapid changes and require fewer training epochs.      

A learning rate that is too large can cause the model to converge too quickly to a suboptimal solution, whereas a learning rate that is too small can cause the process to get stuck.     

The challenge of training deep learning neural networks involves carefully selecting the learning rate. It may be the most important hyperparameter for the model.
In setting a learning rate, there is a trade-off between the rate of convergence and overshooting. While the descent direction is usually determined from the gradient of the loss function, the learning rate determines how big a step is taken in that direction. A too high learning rate will make the learning jump over minima but a too low learning rate will either take too long to converge or get stuck in an undesirable local minimum.      

In order to achieve faster convergence, prevent oscillations and getting stuck in undesirable local minima the learning rate is often varied during training either in accordance to a learning rate schedule or by using an adaptive learning rate. The learning rate and its adjustments may also differ per parameter, in which case it is a diagonal matrix that can be interpreted as an approximation to the inverse of the Hessian matrix in Newton's method. The learning rate is related to the step length determined by inexact line search in quasi-Newton methods and related optimization algorithms
###### Adaptive Learning Rate:
The issue with learning rate schedules is that they all depend on hyperparameters that must be manually chosen for each given learning session and may vary greatly depending on the problem at hand or the model used. To combat this there are many different types of adaptive gradient descent algorithms such as Adagrad, Adadelta, RMSprop, and Adam which are generally built into deep learning libraries such as Keras.      

## How are weights initialized?     
• Before the advances in optimization techniques and activation of non-linearities, kernel is initializes from a random distribution. With advances, all the advances we are able to train convolutional neural networks from a randomized initialization.                 
• Weights of the backpropagation will be randomly initialized such that the mean of the distribution weights is 0 and standard deviation of 1.                   
###### Potential Problems with Weight Initializations 
• If the weights are too small, then the signal shrinks as it passes through each layer. Ends up with very small value to use.              
• If the weights are too large, then the signal grows too large as it passes through each layer, which will bevery large by the time it ends             
• Xavier Initialization takes care of this problem. For more understanding on Xavier initialization below blog and vlog can be used. https://andyljones.tumblr.com/post/110998971763/an-explanation-of-xavier-initialization 

##### Sources: 
    https://www.youtube.com/watch?v=8krd5qKVw-Q           
    Paper on Xavier Initialization: http://proceedings.mlr.press/v9/glorot10a/glorot10a.pdf                
    https://stats.stackexchange.com/questions/200513/how-to-initialize-the-elements-of-the-filter-matrix                       
    https://stats.stackexchange.com/questions/267807/cnn-kernels-updates-initialization                    
    https://www.quora.com/How-are-convolutional-filters-kernels-initialized-and-learned-in-a-convolutional-neural-network-CNN https://ai.stackexchange.com/questions/5092/how-are-kernels-input-values-initialized-in-a-cnn-network#:~:text=The%20kernels%20are%20usually%20initialized,are%20many%20different%20initialization%20strategies.&text=For%20specific%20types%20of%20kernels,that%20seem%20to%20perform%20well.         

## What is "loss" in a neural network?
In the context of optimization, the function we used to maximize or minimize is called objective function. In optimization, we tend to maximize or minimize objective function, by changing the parameters of the model to find the optimum parameters for that can achieve our objective.

Typically, with neural networks, we seek to minimize the error. As such, the objective function is often referred to as a cost function or a loss function and the value calculated by the loss function is referred to as simply “loss.”

Loss functions map a set of parameter values for the network onto a scalar value that indicates how well those parameter accomplish the task the network is intended to do.

There are several common loss functions.

    These losses often measure the squared or absolute error between a network’s output and some target or desired output.              
    Other loss functions are designed specifically for classification models;  the cross-entropy is a common loss designed to minimize the distance between the network’s distribution over class labels and the distribution that the dataset defines.       
    maximize the total reward/value function (reinforcement learning) 

Loss function is generally calculated for one record in a training set. If the same is calculated for entire training set, then its called as cost function. The objective of any neural networks/ML model is always to minimize the total loss for the all the items in the training data set.

Sources: 
https://machinelearningmastery.com/loss-and-loss-functions-for-training-deep-learning-neural-networks/

https://medium.com/@zeeshanmulla/cost-activation-loss-function-neural-network-deep-learning-what-are-these-91167825a4de

## What is the "chain rule" in gradient flow?      
      
While updating the weights in one layer are dependent on the outputs of the previous layers in any neural network. This means that you need to express the derivative of the error with respect to the weights, as a product of many individual derivatives (thereby utilizing the chain rule). This way, the derivative can be used in the aforementioned gradient descent optimization process over several iterations, to arrive at the best weights to minimize the error.


Sources:
https://qr.ae/pGt4cj