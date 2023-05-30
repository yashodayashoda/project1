# Core Pkgs
import streamlit as st
import streamlit.components.v1 as stc

# Import Our Mini Apps
from eda_app import run_eda_app
from ml_app import run_ml_app

html_temp = """
		<div style="background-color:#3872fb;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Early Stage DM Risk Data App </h1>
		<h4 style="color:white;text-align:center;"> Diabetes </h4>
		</div>
		"""

decs_temp = """
	### Early Stage Diabetes Risk Predictor App
			This dataset contains the sign and symptoms data of newly diabetic or would be diabetic patient.
			#### Datasource
				- https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.
			#### App Content
				- EDA Section: Exploratory Data Analysis of Data
				- ML Section: ML Predictor App
"""


def main():
    # st.title("ML Web App with Streamlit")
    stc.html(html_temp)

    menu = ["Home", "EDA", "ML", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        st.write(decs_temp)

    elif choice == "EDA":
        run_eda_app()

    elif choice == "ML":
        run_ml_app()

    else:
        ap = """A diabetes prediction app is designed to assess the risk of developing diabetes in individuals. It utilizes various factors such as age, gender, lifestyle choices, and medical history to provide an estimation of the likelihood of developing diabetes. The app may also incorporate additional features such as tracking blood glucose levels, offering dietary recommendations, and providing educational resources related to diabetes prevention and management. Users can input their information, and the app uses algorithms or machine learning models to generate personalized predictions and suggestions. It is important to note that while these apps can provide insights, they should not replace professional medical advice or diagnosis."""

        st.write(ap)


if __name__ == '__main__':
    main()
