# Campus_Recruitment_Prediction
Building an classification model to check whether a candidate get placed in a campus recruitment or not.

The Whole Project is divided into 2 sections
- Model Creation done in [CR_Machine_Learning.ipynb](https://github.com/Kirushikesh/Campus_Recruitment_Prediction/blob/main/CR_Machine_Learning.ipynb)
- Real Time inference in [app.py](https://github.com/Kirushikesh/Campus_Recruitment_Prediction/blob/main/app.py)

# Table of Content

1. Problem Statement
2. Understanding the dataset
3. Setup
4. Get the Data
    1. Download the Data
    2. Take a Quick Look at the Data Structure
    3. Create a Test Set
5. Discover and Visualize the Data to Gain Insights
    1. Visualizing the data in deep
    2. Looking for Correlations
    3. Experiment with Attribute Combination
6. Prepare the Data for ML Algorithms
    1. Data Cleaning
    2. Handling Text and Categorical Attributes
    3. Custom Transformer
    4. Transformer Pipelines
    5. Balancing The Dataset
7. Select and Train a Model
    1. Training and Evaluating on the Training Set
        1. Logistic Regression
        2. Decision Trees
        3. K Nearest Neighbour
    2. Better Evaluation Using Cross-Validation
        1. K Nearest Neighbour
        2. Support Vector Machine
        3. Random Forest
    3. The ROC Curve
8. Fine-Tune Your Model
    1. Randomized Search
    2. Analyze the Best Models and Their Errors
9. Evaluate on Test Set
10. Interpreting using XAI
    1. Example 1
    2. Example 2
    3. Example 3
11. Further Work
12. Conclusion and Future Work
13. References

# Few Images during Model Creation
![attribute_histogram_plots](https://user-images.githubusercontent.com/49152921/139538177-26c0d916-9925-4236-80ac-529bf2e5e8a8.png)

![Degree vs Recruitment](https://user-images.githubusercontent.com/49152921/139538182-64fc85e9-4248-4310-99f3-2eb7f3430a96.png)

![Feature Importance](https://user-images.githubusercontent.com/49152921/139538186-01cb7d31-7543-4843-9398-cdf7805286dd.png)

![Trained Decision Tree](https://user-images.githubusercontent.com/49152921/139538208-b01a4399-7d05-4a8a-b749-1bcab79fed64.png)

![roc_curve_plot](https://user-images.githubusercontent.com/49152921/139538210-fcc5f44c-d339-4186-bf34-4f846e2d43d7.png)

![SHAP Force Plot 1](https://user-images.githubusercontent.com/49152921/139538216-a0f64cb2-546c-4a1f-8fef-34d99dc05085.png)

![Heroku_Webpage](https://user-images.githubusercontent.com/49152921/139538227-25b25f26-63f5-4000-85c5-264741de630f.png)
