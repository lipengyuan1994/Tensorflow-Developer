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


## Sequence bias

Sequence bias is when the order of things can impact the selection of things. For example, if I were to ask you your favorite TV show, and listed "Game of Thrones", "Killing Eve", "Travellers" and "Doctor Who" in that order, you're probably more likely to select 'Game of Thrones' as you are familiar with it, and it's the first thing you see. Even if it is equal to the other TV shows. So, when training data in a dataset, we don't want the sequence to impact the training in a similar way, so it's good to shuffle them up.

## More info on Huber loss
Please find the Wikipedia page here.