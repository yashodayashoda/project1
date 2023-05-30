import plotly.express as px
import seaborn as sns
import streamlit as st

# Load EDA Pkgs
import pandas as pd

# Data Viz Pkgs
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')


@st.cache
def load_data(data):
    df = pd.read_csv(data)
    return df


data = "https://raw.githubusercontent.com/7DataScientist/Dia_deployed/main/data/diabetes_data_upload.csv"
# data = ".\data\diabetes_data_upload.csv"

# data = "D:\\27_Streamlit\\000_Projects\\01_Section_7_Machine_Learning_App\\diabetes_prediction_ml_app\\data\\diabetes_data_upload.csv"

data_cleanded = "https://raw.githubusercontent.com/7DataScientist/Dia_deployed/main/data/diabetes_data_upload_clean.csv"
# data_cleanded = ".\data\diabetes_data_upload_clean.csv"

# data_cleanded = "D:\\27_Streamlit\\000_Projects\\01_Section_7_Machine_Learning_App\\my_work\\data\diabetes_data_upload_clean.csv"

data_freq = "https://raw.githubusercontent.com/7DataScientist/Dia_deployed/main/data/freqdist_of_age_data.csv"
# data_freq = ".\data\\freqdist_of_age_data.csv"

# data_freq = "D:\\27_Streamlit\\000_Projects\\01_Section_7_Machine_Learning_App\\my_work\\data\\freqdist_of_age_data.csv"


def run_eda_app():
    st.header("Exploratory Data Analysis")

    df = load_data(data)
    df_encoded = load_data(data_cleanded)
    freq_df = load_data(data_freq)

    submenu = st.sidebar.selectbox("SubMenu", ["Descriptive", "Plots"])

    if submenu == "Descriptive":

        st.dataframe(df)

        with st.expander("Data Types Summary"):
            st.dataframe(df.dtypes)

        with st.expander("Descriptive Summary"):
            st.dataframe(df_encoded.describe())

        with st.expander("Gender Distribution"):
            st.dataframe(df['Gender'].value_counts())

        with st.expander("Class Distribution"):
            st.dataframe(df['class'].value_counts())

    else:
        st.subheader("Plots")

        # Layouts
        col1, col2 = st.columns([2, 1])

        with col1:
            with st.expander("Dist Plot of Gender"):
                # fig = plt.figure()
                # sns.countplot(x='Gender', data=df)
                # st.pyplot(fig)

                gen_df = df['Gender'].value_counts().to_frame()
                gen_df = gen_df.reset_index()

                gen_df.columns = ['Gender Type', 'Counts']
                # st.dataframe(gen_df)

                p1 = px.pie(gen_df, names='Gender Type', values='Counts')
                st.plotly_chart(p1, use_container_width=True)

            with st.expander("Dist Plot of Class"):
                fig = plt.figure()
                sns.countplot(x='class', data=df)
                st.pyplot(fig)

        with col2:

            with st.expander("Gender Distribution"):
                st.dataframe(df['Gender'].value_counts())

            with st.expander("Class Distribution"):
                st.dataframe(df['class'].value_counts())

        with st.expander("Frequency Dist Plot of Age"):
            # st.dataframe(freq_df)

            p2 = px.bar(freq_df, x='Age', y='count')
            st.plotly_chart(p2, use_container_width=True)

        with st.expander("Outlier Detection Plot"):
            # outlier_df =
            # fig = plt.figure()
            # sns.boxplot(df['Age'])
            # st.pyplot(fig)

            p3 = px.box(df, x='Age', color='Gender')
            st.plotly_chart(p3,  use_container_width=True)

        with st.expander("Correlation Plot"):
            corr_matrix = df_encoded.corr()
            # fig = plt.figure(figsize=(20, 10))
            # sns.heatmap(corr_matrix, annot=True)
            # st.pyplot(fig)

            p3 = px.imshow(corr_matrix)
            st.plotly_chart(p3)
