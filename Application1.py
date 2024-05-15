import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
from streamlit_option_menu import option_menu
from PIL import Image
import base64

img = Image.open("maersk1.png")
st.set_page_config(page_title="AP MOLLER", page_icon= img, layout="wide")

excel_file ='AP_Moller1.xlsx'
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

with st.sidebar:
    nav = option_menu(None, ["Dashboard", "Ideas"],
        icons=['house','clipboard-data-fill', 'cloud'], 
        menu_icon="cast", default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "25px"}, 
            "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#  "},
            "nav-link-selected": {"background-color": "blue"},
        }
    )
      

if nav == "Dashboard" :
    col1,col2 = st.columns([0.1,0.9])
    html_title = """
        <style>
        .title-test{
        front-weight : bold;
        padding : 5px
        border-radius : 6px
        }
        </style>
        <center><h1 class = "title-test">AP MOLLER</h1></center>"""

    with col1: 
        img = Image.open("maersk1.png")
        st.write(" ")   
        st.image(img,
                caption = "MAERSK",
                width=100,
                channels='RGB')
        
    with col2 :
        st.markdown(html_title, unsafe_allow_html=True)
    
    st.subheader("TTH OVERVIEW 🤝")

    col1,col2 = st.columns((5,3))
    sheet_name = 'AP MOLLER OVERVIEW'
    df = pd.read_excel(excel_file,
                   sheet_name = sheet_name,
                   header=1,
                   )
    
    with col1:
        col1.dataframe(df)
    

    with col2:
    #pie chart
            pie_chart = px.pie(df, title="📊Resource Count",
                            values='Resource Count',
                            names='PM Name')

            st.plotly_chart(pie_chart)
    

    PM_name = st.multiselect("Pick your PM👨🏻‍💼",df['PM Name'].unique())
    df2 = df[df["PM Name"].isin(PM_name)]
    bar_chart = px.bar(df2,
                    title = '📊Idea proposed %',
                    x= 'PM Name',
                    y='Proposed %',
                    template = 'plotly_white')
    st.plotly_chart(bar_chart)


if nav == "Ideas": 
   
   tab1,tab2 = st.tabs(["All Ideas","Idea to be discussed"])
   #Idea1 = option_menu(None, ["Ideas to be discussed","All Ideas"],
        #icons=['house','clipboard-data-fill'], 
        #menu_icon="cast", default_index=0,
        #styles={
         #   "container": {"padding": "0!important", "background-color": "#fafafa"},
          #  "icon": {"color": "orange", "font-size": "25px"}, 
           # "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#  "},
            #"nav-link-selected": {"background-color": "green"},
        #}, orientation = 'horizontal')
   with tab2:
   #if Idea1 == "Ideas to be discussed":
        sheet_name2 = 'Discussion'
        
        
        df3 = pd.read_excel(excel_file,
                    sheet_name = sheet_name2,
                    header=0)
        
        Idea2 = st.selectbox("Pick your Idea",df3.Idea, 0, key ='1')
        col1,col2,col3,col4 = st.columns((5,5,5,3), gap='small')
        with col1:
            Idea_Description = df3.loc[df3.Idea == Idea2]["Idea"].iloc[0]
            st.subheader("Idea Description")
            st.warning(f'\n\n{Idea_Description}')

            #Solution Approach
            Solution_Approach= df3.loc[df3.Idea == Idea2]["Solution Approach"].iloc[0]
            st.subheader("Solution Approach")
            st.write(f'\n\n {Solution_Approach}')

             #Remarks
            Remarks = df3.loc[df3.Idea == Idea2]["Remarks"].iloc[0]
            st.subheader("Remarks")
            st.write(f'\n\n {Remarks}')

           

        with col2:
            #Idea Proposed Solution
            Proposed_solution = df3.loc[df3.Idea == Idea2]["Proposed Solution"].iloc[0]
            st.subheader("Proposed Solution")
            st.write(f'\n\n {Proposed_solution}')

            #Existing process if any
            Existing_process= df3.loc[df3.Idea == Idea2]["Existing Process (if any)"].iloc[0]
            st.subheader("Existing process")
            st.write(f'\n\n {Existing_process}')

             #Engagement
            Engagement_1 = df3.loc[df3.Idea == Idea2]["Engagement Name"].iloc[0]
            st.subheader("Engagement")
            st.write(f'\n\n {Engagement_1}')
            

        with col3:
                #TL/PM Name
            TL_Name = df3.loc[df3.Idea == Idea2]["TL/PM Name"].iloc[0]
            st.subheader("TL/PM Name")
            st.write(f'\n\n {TL_Name}')

            #Scope
            Scope_= df3.loc[df3.Idea == Idea2]["Scope"].iloc[0]
            st.subheader("Scope")
            st.write(f'\n\n {Scope_}')

            #Business Benefits
            Business_Benefits= df3.loc[df3.Idea == Idea2]["Business Benefits"].iloc[0]
            st.subheader("Business Benefits")
            st.write(f'\n\n {Business_Benefits}')

        with col4:
            #Estimated Customer Savings (Integible saving) (in USD)
            Estimated_Customer_SavingI = df3.loc[df3.Idea == Idea2]["Estimated Customer Savings (Integible saving) (in USD)"].iloc[0]
            st.subheader("Estimated Customer Savings (Integible saving) (in USD)")
            st.write(f'\n\n {Estimated_Customer_SavingI}')

            #Estimated Customer Savings (in USD)
            Estimated_Customer_Saving = df3.loc[df3.Idea == Idea2]["Estimated Customer Savings (in USD)"].iloc[0]
            st.subheader("Estimated Customer Savings (in USD)")
            st.write(f'\n\n ${Estimated_Customer_Saving}')

           
  
   with tab1:
   #if Idea1 == "All Ideas":
        sheet_name2 = 'Ideas'
       
        df3 = pd.read_excel(excel_file,
                   sheet_name = sheet_name2,
                   header=0)
        
        Idea2 = st.selectbox("Pick your Idea",df3.Idea, 0, key = '2')
        col1,col2,col3,col4 = st.columns((5,5,5,3))
        with col1:
            Idea_Description = df3.loc[df3.Idea == Idea2]["Idea"].iloc[0]
            st.subheader("Idea Description")
            st.write(f'\n\n{Idea_Description}')

            #Solution Approach
            Solution_Approach= df3.loc[df3.Idea == Idea2]["Solution Approach"].iloc[0]
            st.subheader("Solution Approach")
            st.write(f'\n\n {Solution_Approach}')

             #Remarks
            Remarks = df3.loc[df3.Idea == Idea2]["Remarks"].iloc[0]
            st.subheader("Remarks")
            st.write(f'\n\n {Remarks}')


        with col2:
            #Idea Proposed Solution
            Proposed_solution = df3.loc[df3.Idea == Idea2]["Proposed Solution"].iloc[0]
            st.subheader("Proposed Solution")
            st.write(f'\n\n {Proposed_solution}')

            #Existing process if any
            Existing_process= df3.loc[df3.Idea == Idea2]["Existing Process (if any)"].iloc[0]
            st.subheader("Existing process")
            st.write(f'\n\n {Existing_process}')

            #Engagement
            Engagement_1 = df3.loc[df3.Idea == Idea2]["Engagement Name"].iloc[0]
            st.subheader("Engagement")
            st.write(f'\n\n {Engagement_1}')

        with col3:
             #TL/PM Name
            TL_Name = df3.loc[df3.Idea == Idea2]["TL/PM Name"].iloc[0]
            st.subheader("TL/PM Name")
            st.write(f'\n\n {TL_Name}')

            #Scope
            Scope_= df3.loc[df3.Idea == Idea2]["Scope"].iloc[0]
            st.subheader("Scope")
            st.write(f'\n\n {Scope_}')

            #Business Benefits
            Business_Benefits= df3.loc[df3.Idea == Idea2]["Business Benefits"].iloc[0]
            st.subheader("Business Benefits")
            st.write(f'\n\n {Business_Benefits}')


            #ppt Recieved
            PPT_Received = df3.loc[df3.Idea == Idea2]["PPT Received"].iloc[0]
            st.subheader("PPT Recieved")
            st.write(f'\n\n {PPT_Received}')

        with col4:
            #Estimated Customer Savings (Integible saving) (in USD)
            Estimated_Customer_SavingI = df3.loc[df3.Idea == Idea2]["Estimated Customer Savings (Integible saving) (in USD)"].iloc[0]
            st.subheader("Estimated Customer Savings (Integible saving) (in USD)")
            st.write(f'\n\n {Estimated_Customer_SavingI}')

            #Estimated Customer Savings (in USD)
            Estimated_Customer_Saving = df3.loc[df3.Idea == Idea2]["Estimated Customer Savings (in USD)"].iloc[0]
            st.subheader("Estimated Customer Savings (in USD)")
            st.write(f'\n\n ${Estimated_Customer_Saving}')

           
            
            
            

  
