import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
from PIL import Image

st.set_page_config(page_title="AP MOLLER", page_icon=":bar_chart:", layout="wide")
st.title(":bar_chart: AP Moller")

excel_file ='AP_Moller.xlsx'
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

nav = st.sidebar.radio("Navigation", ["Dashboard", "Ideas"])

if nav == "Dashboard" :
    st.header("TTH OVERVIEW")
    sheet_name = 'AP MOLLER OVERVIEW'
    df = pd.read_excel(excel_file,
                   sheet_name = sheet_name,
                   header=1)
    st.dataframe(df)
    
    #pie chart
    pie_chart = px.pie(df, title="Resource Count",
                       values='Resource Count',
                       names='PM Name')

    st.plotly_chart(pie_chart)
    
    PM_name = st.multiselect("Pick your PM",df['PM Name'].unique())
    df2 = df[df["PM Name"].isin(PM_name)]
    bar_chart = px.bar(df2,
                       title = 'Idea proposed %',
                       x= 'PM Name',
                       y='Proposed %',
                       template = 'plotly_white')
    st.plotly_chart(bar_chart)


if nav == "Ideas":
    Idea1 = st.selectbox("Where do you want to look?", ["All Ideas", "Ideas to be discusssed"], key= "2")
    st.header("All Ideas")
    if  Idea1 == "All Ideas":
        sheet_name2 = 'Ideas'
        df3 = pd.read_excel(excel_file,
                   sheet_name = sheet_name2,
                   header=0)
        
        Idea2 = st.selectbox("Pick your Idea",df3.Idea, 0)
        Idea_Description = df3.loc[df3.Idea == Idea2]["Idea"].iloc[0]
        st.subheader("Idea Description")
        st.info(f'\n\n {Idea_Description}')

        #TL/PM Name
        TL_Name = df3.loc[df3.Idea == Idea2]["TL/PM Name"].iloc[0]
        st.subheader("TL/PM Name")
        st.info(f'\n\n {TL_Name}')



        #Idea Proposed Solution
        Proposed_solution = df3.loc[df3.Idea == Idea2]["Proposed Solution"].iloc[0]
        st.subheader("Proposed Solution")
        st.info(f'\n\n {Proposed_solution}')

        #Existing process if any
        Existing_process= df3.loc[df3.Idea == Idea2]["Existing Process (if any)"].iloc[0]
        st.subheader("Existing process")
        st.info(f'\n\n {Existing_process}')


        #Solution Approach
        Solution_Approach= df3.loc[df3.Idea == Idea2]["Solution Approach"].iloc[0]
        st.subheader("Solution Approach")
        st.info(f'\n\n {Solution_Approach}')
        

        #Scope
        Scope_= df3.loc[df3.Idea == Idea2]["Scope"].iloc[0]
        st.subheader("Scope")
        st.info(f'\n\n {Scope_}')

        #Business Benefits
        Business_Benefits= df3.loc[df3.Idea == Idea2]["Business Benefits"].iloc[0]
        st.subheader("Business Benefits")
        st.info(f'\n\n {Business_Benefits}')


        #Estimated Customer Savings (Integible saving) (in USD)
        Estimated_Customer_SavingI = df3.loc[df3.Idea == Idea2]["Estimated Customer Savings (Integible saving) (in USD)"].iloc[0]
        st.subheader("Estimated Customer Savings (Integible saving) (in USD)")
        st.info(f'\n\n {Estimated_Customer_SavingI}')

        #Estimated Customer Savings (in USD)
        Estimated_Customer_Saving = df3.loc[df3.Idea == Idea2]["Estimated Customer Savings (in USD)"].iloc[0]
        st.subheader("Estimated Customer Savings (in USD)")
        st.info(f'\n\n {Estimated_Customer_Saving}$')

        #Remarks
        Remarks = df3.loc[df3.Idea == Idea2]["Remarks"].iloc[0]
        st.subheader("Remarks")
        st.info(f'\n\n {Remarks}')

        #Engagement
        Engagement_1 = df3.loc[df3.Idea == Idea2]["Engagement Name"].iloc[0]
        st.subheader("Engagement")
        st.info(f'\n\n {Engagement_1}')
        
        #ppt Recieved
        PPT_Received = df3.loc[df3.Idea == Idea2]["PPT Received"].iloc[0]
        st.subheader("PPT Recieved")
        st.warning(f'\n\n {PPT_Received}')

    if  Idea1 == "Ideas to be discusssed":
        sheet_name3 = 'Ideas - To be discussed'
        df5 = pd.read_excel(excel_file,
                   sheet_name = sheet_name3,
                   header=0)
        
        Idea2 = st.selectbox("Pick your Idea",df5.Idea_Description, 0)
        Idea_Description = df5.loc[df5.Idea_Description == Idea2]["Idea_Description"].iloc[0]
        st.subheader("Idea Description")
        st.info(f'\n\n {Idea_Description}')

        #TL/PM Name
        TL_Name = df5.loc[df5.Idea_Description == Idea2]["TL/PM Name"].iloc[0]
        st.subheader("TL/PM Name")
        st.info(f'\n\n {TL_Name}')



        #Idea Proposed Solution
        Proposed_solution = df5.loc[df5.Idea_Description == Idea2]["Proposed Solution"].iloc[0]
        st.subheader("Proposed Solution")
        st.info(f'\n\n {Proposed_solution}')

        #Existing process if any
        Existing_process= df5.loc[df5.Idea_Description == Idea2]["Existing Process (if any)"].iloc[0]
        st.subheader("Existing process")
        st.info(f'\n\n {Existing_process}')


        #Solution Approach
        Solution_Approach= df5.loc[df5.Idea_Description == Idea2]["Solution Approach"].iloc[0]
        st.subheader("Solution Approach")
        st.info(f'\n\n {Solution_Approach}')
        

        #Scope
        Scope_= df5.loc[df5.Idea_Description == Idea2]["Scope"].iloc[0]
        st.subheader("Scope")
        st.info(f'\n\n {Scope_}')

        #Business Benefits
        Business_Benefits= df5.loc[df5.Idea_Description == Idea2]["Business Benefits"].iloc[0]
        st.subheader("Business Benefits")
        st.info(f'\n\n {Business_Benefits}')


        #Estimated Customer Savings (Integible saving) (in USD)
        Estimated_Customer_SavingI = df5.loc[df5.Idea_Description == Idea2]["Estimated Customer Savings (Integible saving) (in USD)"].iloc[0]
        st.subheader("Estimated Customer Savings (Integible saving) (in USD)")
        st.info(f'\n\n {Estimated_Customer_SavingI}')

        #Estimated Customer Savings (in USD)
        Estimated_Customer_Saving = df5.loc[df5.Idea_Description == Idea2]["Estimated Customer Savings (in USD)"].iloc[0]
        st.subheader("Estimated Customer Savings (in USD)")
        st.info(f'\n\n {Estimated_Customer_Saving}$')

        #Remarks
        Remarks = df5.loc[df5.Idea_Description == Idea2]["Remarks"].iloc[0]
        st.subheader("Remarks")
        st.info(f'\n\n {Remarks}')

        #Engagement
        Engagement_1 = df5.loc[df5.Idea_Description == Idea2]["Engagement Name"].iloc[0]
        st.subheader("Engagement")
        st.info(f'\n\n {Engagement_1}')
        
