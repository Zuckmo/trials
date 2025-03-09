import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="dark")

st.write(
    """
    # Proyek Analisis Data: Bike Sharing Dataset
    """
)   

tab1, tab2, tab3 = st.tabs(["dataset",  "viz option", "business answer"])

with tab1:
    day_url = "https://raw.githubusercontent.com/Zuckmo/trials/refs/heads/master/day_cleaned.csv"
    hour_url = "https://raw.githubusercontent.com/Zuckmo/trials/refs/heads/master/hour_cleaned.csv"

    day = pd.read_csv(day_url)
    hour=pd.read_csv(hour_url)

    day["dteday"] = pd.to_datetime(day["dteday"])
    hour["dteday"] = pd.to_datetime(hour["dteday"])

    st.title("Data penyewaan sepeda")

    st.dataframe(day)
    st.dataframe(hour)  


with tab2:
    st.header("choose axis X and Y")
    def load_data(this_file):
        data = pd.read_csv(this_file)
        return data
    def create_bar_chart(data, x_column, y_column):
        fig, ax = plt.subplots()
        ax.bar(data[x_column], data[y_column])
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
        st.pyplot(fig)
    uploaded_file = ("https://raw.githubusercontent.com/Zuckmo/trials/refs/heads/master/day_cleaned.csv")
    if uploaded_file is not None:
        data = load_data("https://raw.githubusercontent.com/Zuckmo/trials/refs/heads/master/day_cleaned.csv")
        x_column = st.selectbox("choose x axis", data.columns)
        y_column = st.selectbox("choose y axis", data.columns)
        create_bar_chart(data, x_column, y_column)


with tab3:
    st.title("Business Answer")

    st.header("rental number based on the season")
    season_count = day.groupby("season")["total"].sum()
    fig, ax = plt.subplots()
    season_count.plot(kind="bar", ax=ax, color=['blue','orange','green','red'])
    ax.set_xticks(range(len(season_count)))
    ax.set_xticklabels(['Spring','Summer','Fall','Winter'],rotation=0)
    ax.set_ylabel("Total Rental")
    st.pyplot(fig)

    st.header("Effect of weather on bike rental")
    fig,ax = plt.subplots()
    sns.boxplot(x="weather_situation",y="total",data=day,ax=ax)
    ax.set_xticks(range(1,5))   
    ax.set_xticklabels(['Clear','Mist','Light Snow','Heavy Rain'])
    st.pyplot(fig)

    st.header("Comparison of Registered and Unregistered Renters")
    fig, ax = plt.subplots()
    day[['casual','registered']].sum().plot(kind='bar',ax=ax,color=['blue','orange'])
    ax.set_ylabel("Number of Renters")
    st.pyplot(fig)

    #ANALYSIS FOR RFM
    st.header("RFM analysis")
    st.write(
        """
        RFM analysis is a customer segmentation technique that uses three factors:
        - Recency: How recently did the customer make a purchase?
        - Frequency: How often do they make a purchase?
        - Monetary: How much do they spend?
        """
    )

    latest_date= day["dteday"].max()
    day["recency"]= (latest_date - day["dteday"]).dt.days
    recency = day.groupby("recency")["total"].min()

    frequency = day.groupby("dteday")["total"].count()
    monetary = day.groupby("dteday")["total"].sum()

    rfm = pd.DataFrame({"Recency":recency,"Frequency":frequency,"Monetary":monetary})
    st.write(rfm.describe())    

    fig,ax =plt.subplots(1,3,figsize=(15,5))
    sns.histplot(rfm["Recency"],bins=20,ax=ax[0],color="blue")
    ax[0].set_title("Recency Distribution")
    sns.histplot(rfm["Frequency"],bins=20,ax=ax[1],color="green")
    ax[1].set_title("Frequency_Distribution")
    sns.histplot(rfm["Monetary"], bins=20, ax=ax[2], color='red')
    ax[2].set_title('Monetary Distribution')
    st.pyplot(fig)


   





    
