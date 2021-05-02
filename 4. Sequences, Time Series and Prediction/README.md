# Note: 

---
Week1 Sequences and Prediction
---

*  anything that has a time factor in it can be analyzed in this way
    * birth rate 
    * imputation (project back into the past)
    * detect anomalies. For example, in website logs so that you could see potential denial of service attacks showing up as a spike on the time series like this.
    
*  analyze the time series to spot patterns in them that determine what generated the series itself
    * speech recognition


## common patterns:

* trends
* seasonality (shopping, sport)
* white noise
*  auto correlated time series. Namely it correlates with a delayed copy of itself often called a lag
    * ![](./tmp/2021-04-20_08-16-15.png)
    
* real-life time series
    * ![./tmp/TSAN.png](./tmp/TSAN.png)
    * ![](./tmp/non-stationary_time_series.png)
    * ![](./tmp/non-stationary-2.png)
    * ![](./tmp/forecast.png)


* Train Validation and test sets
    * ![](./tmp/2021-04-21_21-27-13.png)

* Metrics for evaluating performance
    * ![](./tmp/2021-04-21_21-37-08.png)

* Moving average and differencing
    * ![](./tmp/2021-04-21_21-38-43.png)
    * Moving average on Differenced Time Series
    * ![](./tmp/2021-04-21_21-39-49.png)
    * ![](./tmp/2021-04-21_21-40-04.png)
    * Smoothing Both Past and Present Values
    * ![](./tmp/2021-04-21_21-52-07.png)

-----

* [Code: Prediction without Machine Learning](./1.%20Naive%20Forecast.py)
* [predict synthetic data](https://colab.research.google.com/gist/lipengyuan1994/976af8fc69a1fb0a0d0e02e5a1b218b4/week-1-exercise-answer.ipynb)


Week2 Deep Neural Networks for Time Series
---
* [preparing features and label](./3.Preparing%20features%20and%20labels.py)
* [single layer nn](./4.Single%20layer%20neural%20network%20notebook.py)
    * [gist](https://colab.research.google.com/gist/lipengyuan1994/a5cdc38331123e8535ed13259ea8e907/s-p-week-2-lesson-3.ipynb)
* [Deep Neural network](./5.DeepNeuralNetwork.py)
* [predict with DNN](./6.Predict%20with%20DNN.py)
    *  [gist](https://colab.research.google.com/gist/lipengyuan1994/3f67d1f7f9b62b3fc664bee877b02770/s-p_week_2_exercise_answer.ipynb)
    


Week3 Recurrent Neural Networks for time series
---
* [RNN](./7.RNN.py)
    * [gist](https://colab.research.google.com/gist/lipengyuan1994/72bf570c0146074147d18eea88e36764/s-p-week-3-lesson-2-rnn.ipynb)
* [LSTM](./8.%20LSTM.py)
    * [gist](https://colab.research.google.com/gist/lipengyuan1994/b99890112a3a0f62d033727653a20629/s-p-week-3-lesson-4-lstm.ipynb)
*  take a synthetic data set and write the code to pick the learning rate and then train on it to get an MAE of < 3 
   * [MAE](./9.%20MAE.py)
   * [gist](https://colab.research.google.com/gist/lipengyuan1994/c0c0aa79f422996b968d527a399b0378/s-p-week-3-exercise-answer.ipynb)
    

Week4 Real-world time series data
---
* [LSTM + batch size](./10.LSTM-(batch).py)
* [Sun spot prediction (conv+lstm+dnn)](./11.SunSpot_conv_lstm.py)
    * [gist](https://colab.research.google.com/gist/lipengyuan1994/90978ac4fd27d1c345da0b316717ccdb/s-p-week-4-lesson-5.ipynb)
    * [gist_normalized_mae<0.05](https://colab.research.google.com/gist/lipengyuan1994/2d6432a296b6525fd17c4afdf3aeca64/s-p-week-4-lesson-5.ipynb#scrollTo=PrktQX3hKYex)



## Sequence bias

Sequence bias is when the order of things can impact the selection of things. For example, if I were to ask you your favorite TV show, and listed "Game of Thrones", "Killing Eve", "Travellers" and "Doctor Who" in that order, you're probably more likely to select 'Game of Thrones' as you are familiar with it, and it's the first thing you see. Even if it is equal to the other TV shows. So, when training data in a dataset, we don't want the sequence to impact the training in a similar way, so it's good to shuffle them up.

## More info on Huber loss
Please find the Wikipedia page here.