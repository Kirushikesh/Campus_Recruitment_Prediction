# Campus_Recruitment_Prediction
Building an classification model to check whether a candidate get placed in a campus recruitment or not. 
The Whole Project is divided into 2 sections
- Model Creation done in [CR_Machine_Learning.ipynb](https://github.com/Kirushikesh/Campus_Recruitment_Prediction/blob/main/CR_Machine_Learning.ipynb)
- Real Time inference in [app.py](https://github.com/Kirushikesh/Campus_Recruitment_Prediction/blob/main/app.py)

During the creation part the EDA is performed on the data followed by the feature engineering followed by the model selection where performance of different classification model is analysed to find the best one finally the model is interpreted using XAI tool to identify the importance of each feature in predicting the outcome.

The next step is deploying the Heroku for realtime inference on the model using the Flask framework. You can try the using https://recruitment-prediction.herokuapp.com/
