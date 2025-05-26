import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
@st.cache_data
def load_data():
    calories_df = pd.read_csv(r"C:\Users\prasa\OneDrive\Documents\calories burnt\calories.csv")
    exercise_df = pd.read_csv(r"C:\Users\prasa\OneDrive\Documents\calories burnt\exercise.csv")
    merged_df = pd.merge(exercise_df, calories_df, on="User_ID")
    return merged_df

df = load_data()

# App title
st.title("Calories & Exercise Data Analysis")

# Show raw data
if st.checkbox("Show raw data"):
    st.write(df)

# Basic statistics
st.subheader("Descriptive Statistics")
st.write(df.describe())

# Gender filter
gender = st.selectbox("Select Gender", options=["All"] + df["Gender"].unique().tolist())
if gender != "All":
    df = df[df["Gender"] == gender]

# Correlation heatmap
st.subheader("Correlation Heatmap")
fig, ax = plt.subplots()
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)

# Scatter plot: Duration vs Calories
st.subheader("Duration vs Calories Burned")
fig2, ax2 = plt.subplots()
sns.scatterplot(data=df, x="Duration", y="Calories", hue="Gender", ax=ax2)
st.pyplot(fig2)

# Distribution of Calories
st.subheader("Calories Distribution")
fig3, ax3 = plt.subplots()
sns.histplot(df["Calories"], kde=True, ax=ax3)
st.pyplot(fig3)
