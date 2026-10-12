# machine-failure-prediction
# AI-Based Machine Failure Prediction

A machine learning project that estimates the likelihood of machine failure using sensor measurements such as air temperature, process temperature, rotational speed, torque, and tool wear.

## 🚀 Live Demo

Try the deployed application here:

**[Machine Failure Prediction App](https://machine-failure-prediction-kamachi.streamlit.app/)**

## 📌 Project Overview

Unexpected machine failures can cause production delays, equipment damage, and increased maintenance costs. This project uses machine learning to identify potential machine failures based on operating conditions.

The application allows users to enter sensor measurements and receive a predicted failure probability.

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- Streamlit
- Joblib
- Google Colab

## 📊 Dataset

This project uses the **AI4I 2020 Predictive Maintenance Dataset** from the UCI Machine Learning Repository.

Five input features are used:

- Air temperature (K)
- Process temperature (K)
- Rotational speed (rpm)
- Torque (Nm)
- Tool wear (min)

The target variable is `Machine failure`.

## 🤖 Machine Learning Approach

- Explored and prepared the dataset.
- Selected five sensor features for prediction.
- Split the data into training and testing sets using stratified sampling.
- Trained a Random Forest classifier.
- Adjusted the prediction threshold to 0.30 to improve failure detection.
- Evaluated the model on held-out test data.

## 📈 Model Performance

At the selected threshold of 0.30, the model achieved these results on the test set:

| Metric | Score |
|---|---:|
| Accuracy | 98.45% |
| Precision for failure class | 78.5% |
| Recall for failure class | 75.0% |
| F1-score for failure class | 76.7% |

The model detected 51 of the 68 actual failure cases in the test set.

**Note:** Accuracy alone can be misleading because machine failures are relatively rare in this dataset. Precision and recall help evaluate how well the model identifies failures.

## 💻 Run Locally

1. Clone this repository:

   ```bash
   git clone https://github.com/KamachiR/machine-failure-prediction.git
   ```

2. Open the project folder:

   ```bash
   cd machine-failure-prediction
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the application:

   ```bash
   streamlit run app.py
   ```

## ⚠️ Disclaimer

This is an educational machine learning project built using a public dataset. Its predictions are estimates, not guarantees of actual machine condition, and should not be used as the sole basis for maintenance or safety decisions.

## 👩‍💻 Author

**Kamachi R**

- GitHub: [KamachiR](https://github.com/KamachiR)
