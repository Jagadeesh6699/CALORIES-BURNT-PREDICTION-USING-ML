import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Upload files
st.title("Calories & Exercise Dashboard")

uploaded_calories = st.file_uploader("Upload Calories CSV", type=['csv'])
uploaded_exercise = st.file_uploader("Upload Exercise CSV", type=['csv'])

@st.cache_data
def load_data(calories_file, exercise_file):
    if calories_file and exercise_file:
        calories_df = pd.read_csv(calories_file)
        exercise_df = pd.read_csv(exercise_file)
        df = pd.merge(exercise_df, calories_df, on='User_ID')
        return df
    return None

# Load the data
df = load_data(uploaded_calories, uploaded_exercise)

if df is not None:
    # Sidebar filters
    st.sidebar.header("Filters")
    gender = st.sidebar.multiselect("Select Gender", options=df['Gender'].unique(), default=df['Gender'].unique())
    age_range = st.sidebar.slider("Select Age Range", int(df['Age'].min()), int(df['Age'].max()), (20, 60))

    filtered_df = df[(df['Gender'].isin(gender)) & (df['Age'].between(age_range[0], age_range[1]))]

    st.subheader("Data Preview")
    st.write(filtered_df.head())

    st.subheader("Summary Statistics")
    st.write(filtered_df.describe())

    st.subheader("Correlation Heatmap")
    corr = filtered_df[['Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp', 'Calories']].corr()
    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

    st.subheader("Scatter Plots")
    col1, col2 = st.columns(2)

    with col1:
        st.write("Calories vs Duration")
        fig1, ax1 = plt.subplots()
        sns.scatterplot(data=filtered_df, x='Duration', y='Calories', hue='Gender', ax=ax1)
        st.pyplot(fig1)

    with col2:
        st.write("Calories vs Heart Rate")
        fig2, ax2 = plt.subplots()
        sns.scatterplot(data=filtered_df, x='Heart_Rate', y='Calories', hue='Gender', ax=ax2)
        st.pyplot(fig2)

    st.subheader("Boxplot: Calories by Gender")
    fig3, ax3 = plt.subplots()
    sns.boxplot(data=filtered_df, x='Gender', y='Calories')
    st.pyplot(fig3)
else:
    st.warning("Please upload both Calories and Exercise CSV files to proceed.")
