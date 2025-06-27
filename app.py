import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Upload files
st.title("Calories Burnt Prediction App")

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

# Load and display data
df = load_data(uploaded_calories, uploaded_exercise)

if df is not None:
    st.subheader("Dataset Preview")
    st.write(df.head())

    # Feature selection
    X = df[['Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp']]
    y = df['Calories']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Model training
    model = XGBRegressor()
    model.fit(X_train, y_train)

    # Model evaluation
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    st.write(f"✅ Model trained with Mean Squared Error: {mse:.2f}")

    st.subheader("📊 Correlation Heatmap")
    corr = df[['Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp', 'Calories']].corr()
    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

    st.header("🔮 Predict Calories Burnt")

    # User Inputs
    weight = st.number_input("Enter your Weight (kg)", min_value=20.0, max_value=200.0, value=70.0)
    age = st.slider("Age", 10, 100, 30)
    height = st.slider("Height (cm)", 100, 250, 170)
    duration = st.slider("Duration of Exercise (mins)", 5, 300, 60)
    heart_rate = st.slider("Heart Rate (bpm)", 60, 200, 120)
    body_temp = st.slider("Body Temperature (°C)", 35.0, 42.0, 37.0)

    if st.button("Predict Calories"):
        input_data = pd.DataFrame({
            'Age': [age],
            'Height': [height],
            'Weight': [weight],
            'Duration': [duration],
            'Heart_Rate': [heart_rate],
            'Body_Temp': [body_temp]
        })

        prediction = model.predict(input_data)
        st.success(f"🔥 Estimated Calories Burnt: **{prediction[0]:.2f}**")

else:
    st.warning("⚠️ Please upload both Calories and Exercise CSV files.")
