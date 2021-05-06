## Assignment 1

#### What is a neural network neuron?
     
#### What is the use of the learning rate?    
      
#### How are weights initialized?     
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

#### What is "loss" in a neural network?
      
#### What is the "chain rule" in gradient flow?
      
      
