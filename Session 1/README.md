# Assignment 1

## What is a neural network neuron?
     
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
https://www.youtube.com/watch?v=8krd5qKVw-Q           
Paper on Xavier Initialization: http://proceedings.mlr.press/v9/glorot10a/glorot10a.pdf                
https://stats.stackexchange.com/questions/200513/how-to-initialize-the-elements-of-the-filter-matrix                       
https://stats.stackexchange.com/questions/267807/cnn-kernels-updates-initialization                    
https://www.quora.com/How-are-convolutional-filters-kernels-initialized-and-learned-in-a-convolutional-neural-network-CNN https://ai.stackexchange.com/questions/5092/how-are-kernels-input-values-initialized-in-a-cnn-network#:~:text=The%20kernels%20are%20usually%20initialized,are%20many%20different%20initialization%20strategies.&text=For%20specific%20types%20of%20kernels,that%20seem%20to%20perform%20well.         

## What is "loss" in a neural network?
      
## What is the "chain rule" in gradient flow?
      
      
