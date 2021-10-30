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
![Feature Importance](https://user-images.githubusercontent.com/49152921/139536332-2babd108-f1bc-4edb-9970-de18ea8f835d.png)

![Trained Decision Tree](https://user-images.githubusercontent.com/49152921/139536343-679bf70a-ddd8-4d50-b92b-078ad6d470e0.png)

![Degree vs Recruitment](https://user-images.githubusercontent.com/49152921/139536363-78a4570f-97cd-4305-acaa-24e66b64acb0.png)

![roc_curve_plot](https://user-images.githubusercontent.com/49152921/139536371-a3d33c83-be90-4a58-90ac-8ec4d18a3269.png)
