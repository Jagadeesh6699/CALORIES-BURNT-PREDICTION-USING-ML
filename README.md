# Calories Burnt Prediction using Machine Learning

This project is an interactive web application built with Streamlit that allows users to analyze exercise and physiological data and predict the number of calories burned based on various input parameters. The app combines data visualization, filtering, and machine learning to deliver insights for health-conscious users.

### Features

- Upload and merge custom `calories.csv` and `exercise.csv` datasets
- Visualize correlations between variables such as age, weight, heart rate, and calorie burn
- Interactive filters for gender and age range
- Scatter plots, boxplots, and heatmaps for in-depth exploration
- XGBoost regression model trained on the dataset to predict calories burned
- User-friendly prediction tool based on personal input metrics like weight, height, duration, and body temperature

### Model

The machine learning model used is `XGBoostRegressor`, which is known for its performance on tabular data. The model was trained on merged features from both datasets and provides reliable predictions for calorie expenditure.

### Deployment

The project is deployed on the Streamlit Community Cloud and can be accessed here:  
**[Live App](https://calories-burnt-prediction-using-ml-syd5xygappmmndzm8oatlh.streamlit.app/)**

### Requirements

- streamlit  
- pandas  
- seaborn  
- matplotlib  
- xgboost  
- scikit-learn
