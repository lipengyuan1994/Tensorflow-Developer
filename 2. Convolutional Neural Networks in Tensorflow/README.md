[source](https://www.coursera.org/learn/convolutional-neural-networks-tensorflow#syllabus)
# WHAT YOU WILL LEARN

Handle real-world image data

Plot loss and accuracy

Explore strategies to prevent overfitting, including augmentation and dropout

Learn transfer learning and how learned features can be extracted from models



Week1 Exploring a Larger Dataset 
-------

* high level APIs you could do basic image classification
* filter the dataset, data cleaning. 
*  go deeper into using ConvNets will real-world data, and learn about techniques that you can use to improve your ConvNet performance, particularly when doing image classification!

[the famous Kaggle Dogs v Cats dataset](https://www.kaggle.com/c/dogs-vs-cats)

[Initial model](https://colab.research.google.com/github/lmoroney/dlaicourse/blob/master/Course%202%20-%20Part%202%20-%20Lesson%202%20-%20Notebook.ipynb#scrollTo=_qqNIbspb_NV)
 
From this notebook: (same as course_2_part_2_lesson_2_notebook )
1. In this case, using the [RMSprop](https://wikipedia.org/wiki/Stochastic_gradient_descent#RMSProp) optimization algorithm is preferable to stochastic gradient descent (SGD), because RMSprop automates learning-rate tuning for us. (Other optimizers, such as Adam and Adagrad, also automatically adapt the learning rate during training, and would work equally well here.)
2. Find the overfitting by plotting: 

![](./resources/2020-11-14_14-10-43.png)

At the end of the last video you saw how to explore the training history and discovered an interesting phenomenon: Even though the training data set’s accuracy went very high, we saw that after only a few epochs, the validation set levelled out. This is a clear sign that we are overfitting again. Using more data should help with this, but there are some other techniques that you can use with smaller data sets too.


### Fixing through cropping
fix the wrong prediction by cropping the images, to get a better prediction. 

### [Final solutions](https://colab.research.google.com/github/lmoroney/dlaicourse/blob/master/Exercises/Exercise%205%20-%20Real%20World%20Scenarios/Exercise%205%20-%20Answer.ipynb#scrollTo=5qE1G6JB4fMn)


Week2 Augmentation: A technique to avoid overfitting
---

Augmentation simply amends your images on-the-fly while training using transforms like rotation. So, it could 'simulate' an image of a cat lying down by rotating a 'standing' cat by 90 degrees. As such you get a cheap way of extending your dataset beyond what you have already.

###  Image Augmentation
 * To learn more about Augmentation, and the available transforms, check out https://github.com/keras-team/keras-preprocessing -- and note that it's referred to as preprocessing for a very powerful reason: that it doesn't require you to edit your raw images, nor does it amend them for you on-disk. It does it in-memory as it's performing the training, allowing you to experiment without impacting your dataset.
 * augmentation for Horses V Humans [notebook](https://colab.research.google.com/github/lmoroney/dlaicourse/blob/master/Course%202%20-%20Part%204%20-%20Lesson%204%20-%20Notebook.ipynb)
 
 
 Week3 Transfer Learning
 ---
 
* take an existing model, freeze many of its layers to prevent them being retrained, and effectively 'remember' the convolutions it was trained on to fit images. added your own DNN underneath this so that you could retrain on your images using the convolutions from the other model.
  Using this notebook to explore transfer learning: https://colab.research.google.com/github/lmoroney/dlaicourse/blob/master/Course%202%20-%20Part%206%20-%20Lesson%203%20-%20Notebook.ipynb
  ```
    import os
    
    from tensorflow.keras import layers
    from tensorflow.keras import Model
    !wget --no-check-certificate \
        https://storage.googleapis.com/mledu-datasets/inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5 \
        -O /tmp/inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5
      
    from tensorflow.keras.applications.inception_v3 import InceptionV3
    
    local_weights_file = '/tmp/inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5'
    
    pre_trained_model = InceptionV3(input_shape = (150, 150, 3), 
                                    include_top = False, 
                                    weights = None)
    
    pre_trained_model.load_weights(local_weights_file)
    
    for layer in pre_trained_model.layers:
      layer.trainable = False
  ```

* For more on how to freeze/lock layers, explore the documentation, which includes an example using MobileNet architecture: https://www.tensorflow.org/tutorials/images/transfer_learning
* you freeze (or lock) the already learned convolutions into your model. Now, you'll need to add your own DNN at the bottom of these, which you can retrain to your data
* regularization using dropouts to make your network more efficient in preventing over-specialization and this overfitting. [Using dropouts](https://colab.research.google.com/github/lmoroney/dlaicourse/blob/master/Course%202%20-%20Part%206%20-%20Lesson%203%20-%20Notebook.ipynb)

* final exercise for this week;Your training should automatically stop once it reaches this desired accuracy, and it should do it in less than 100 epochs. Running on a colab GPU, I've been able to hit this metric in about 3 minutes and 69 epochs,
https://colab.research.google.com/github/lmoroney/dlaicourse/blob/master/Exercises/Exercise%207%20-%20Transfer%20Learning/Exercise%207%20-%20Answer.ipynb

week4
---

go beyond binary classification
* how the code can be modified from a binary class classifier to a multi class one, take a look at the [notebook](https://colab.research.google.com/github/lmoroney/dlaicourse/blob/master/Course%202%20-%20Part%208%20-%20Lesson%202%20-%20Notebook%20(RockPaperScissors).ipynb)
* for binary classification, use activation : sigmoid,  for multi-class classification, use softmax. 
* loss function, for multi-class use 'categorical_crossentropy'
* exercise: [build a multi-class classifier](https://colab.research.google.com/github/lmoroney/dlaicourse/blob/master/Exercises/Exercise%208%20-%20Multiclass%20with%20Signs/Exercise%208%20-%20Question.ipynb#scrollTo=Rmb7S32cgRqS), [answer](https://colab.research.google.com/github/lmoroney/dlaicourse/blob/master/Exercises/Exercise%208%20-%20Multiclass%20with%20Signs/Exercise%208%20-%20Answer.ipynb#scrollTo=Rmb7S32cgRqS)



 