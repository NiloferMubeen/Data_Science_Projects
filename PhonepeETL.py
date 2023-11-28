import os
import json
import pandas as pd
import streamlit as st
import plotly.express as px

#Aggregate TRANSACTION

def trans_agg():
        agg_path1='C://Users/Welcome/pulse/data/aggregated/transaction/country/india/state'
        Agg_state_list =os.listdir(agg_path1)

        columns ={'State':[], 'Year':[],'Quarter':[],'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}

        for i in Agg_state_list:
            p_i = agg_path1 +'/'+ i 
            Agg_yr = os.listdir(p_i)
            
            for j in Agg_yr:
                p_j = p_i +'/'+ j
                Agg_yr_list=os.listdir(p_j)
                
                for k in Agg_yr_list:
                        p_k =p_j + '/'+ k
                        Data=open(p_k,'r')
                        D=json.load(Data)
                        for z in D['data']['transactionData']:
                            Name=z['name']
                            count=z['paymentInstruments'][0]['count']
                            amount= z['paymentInstruments'][0]['amount']
                            columns['Transaction_type'].append(Name)
                            columns['Transaction_count'].append(count)
                            columns['Transaction_amount'].append(amount)
                            columns['State'].append(i)
                            columns['Year'].append(j)
                            columns['Quarter'].append(int(k.strip('.json')))

        Agg_Trans=pd.DataFrame(columns)

        Agg_Trans['State'] = Agg_Trans['State'].replace(['andaman-&-nicobar-islands'],'Andaman & Nicobar')
        Agg_Trans['State'] = Agg_Trans['State'].replace(['dadra-&-nagar-haveli-&-daman-&-diu'],'Dadra and Nagar Haveli and Daman and Diu')
        Agg_Trans['State'] = Agg_Trans['State'].str.replace('-',' ')
        Agg_Trans.State = Agg_Trans.State.str.title()

        return Agg_Trans

#Aggrgate USER

def user_agg():
        agg_path2='C://Users/Welcome/pulse/data/aggregated/user/country/india/state'
        Agg_state_list = os.listdir(agg_path2)

        columns={'State':[], 'Year':[],'Quarter':[],'Mobile_brand':[], 'User_count':[], 'User_percentage':[]}

        for i in Agg_state_list:
                p_i = agg_path2 +'/'+ i 
                Agg_yr = os.listdir(p_i)
                
                for j in Agg_yr:
                        p_j = p_i +'/'+ j
                        Agg_yr_list=os.listdir(p_j)
                        
                        for k in Agg_yr_list:
                                p_k =p_j + '/'+ k
                                Data=open(p_k,'r')
                                D=json.load(Data)
                                data = D['data']['usersByDevice']
                                try:
                                    for z in data:
                                            brand=z['brand']
                                            count=z['count']
                                            percentage=z['percentage']
                                            columns['Mobile_brand'].append(brand)
                                            columns['User_count'].append(count)
                                            columns['User_percentage'].append(percentage)
                                            columns['State'].append(i)
                                            columns['Year'].append(j)
                                            columns['Quarter'].append(int(k.strip('.json')))
                                except:
                                    pass
        Agg_user=pd.DataFrame(columns)
        Agg_user['State'] = Agg_user['State'].replace(['andaman-&-nicobar-islands'],'Andaman & Nicobar')
        Agg_user['State'] = Agg_user['State'].replace(['dadra-&-nagar-haveli-&-daman-&-diu'],'Dadra and Nagar Haveli and Daman and Diu')
        Agg_user['State'] = Agg_user['State'].str.replace('-',' ')
        Agg_user.State = Agg_user.State.str.title()

        return Agg_user

# Map TRANSACTION

def trans_map():
        map_path1 = 'C://Users/Welcome/pulse/data/map/transaction/hover/country/india/state'
        map_state_list = os.listdir(map_path1)

        columns={'State':[], 'Year':[],'Quarter':[],'District_name':[], 'Transaction_count':[], 'Transaction_amount':[]}

        for i in map_state_list:
                p_i = map_path1 +'/'+ i 
                map_yr = os.listdir(p_i)
                
                for j in map_yr:
                        p_j = p_i +'/'+ j
                        map_yr_list=os.listdir(p_j)
                        
                        for k in map_yr_list:
                                p_k =p_j + '/'+ k
                                Data=open(p_k,'r')
                                D=json.load(Data)
                                data = D['data']['hoverDataList']
                                for z in data:
                                        district = z['name']
                                        count = z['metric'][0]['count']
                                        amount = z['metric'][0]['amount']
                                        columns['District_name'].append(district)
                                        columns['Transaction_count'].append(count)
                                        columns['Transaction_amount'].append(amount)
                                        columns['State'].append(i)
                                        columns['Year'].append(j)
                                        columns['Quarter'].append(int(k.strip('.json')))
                        
        map_trans = pd.DataFrame(columns)  
        map_trans['State'] = map_trans['State'].replace(['andaman-&-nicobar-islands'],'Andaman & Nicobar')
        map_trans['State'] = map_trans['State'].replace(['dadra-&-nagar-haveli-&-daman-&-diu'],'Dadra and Nagar Haveli and Daman and Diu')
        map_trans['State'] = map_trans['State'].str.replace('-',' ')
        map_trans.State = map_trans.State.str.title()
        return map_trans

#Map USER

def user_map():
        map_path2 = 'C://Users/Welcome/pulse/data/map/user/hover/country/india/state'
        map_state_list = os.listdir(map_path2)

        columns = {'State':[], 'Year':[],'Quarter':[],'District_name':[], 'Registered_users':[],'App_Opens':[]}
        for i in map_state_list:
                p_i = map_path2 + '/'+ i
                map_yr = os.listdir(p_i)
                
                for j in map_yr:
                        p_j = p_i + '/'+ j
                        map_yr_list = os.listdir(p_j)
                        
                        
                        for k in map_yr_list:
                                p_k = p_j + '/'+k
                                Data = open(p_k,'r')
                                D=json.load(Data)
                                
                                data = D['data']['hoverData']
                                
                                for z in data.items():
                                
                                        district = z[0]
                                        users = z[1]['registeredUsers']
                                        opens = z[1]['appOpens']
                                        
                                        columns['District_name'].append(district)
                                        columns['Registered_users'].append(users)
                                        columns['App_Opens'].append(opens)
                                        columns['State'].append(i)
                                        columns['Year'].append(j)
                                        columns['Quarter'].append(k.strip('.json'))
                                
        map_user = pd.DataFrame(columns)                
                        
        map_user['State'] = map_user['State'].replace(['andaman-&-nicobar-islands'],'Andaman & Nicobar')
        map_user['State'] = map_user['State'].replace(['dadra-&-nagar-haveli-&-daman-&-diu'],'Dadra and Nagar Haveli and Daman and Diu')
        map_user['State'] = map_user['State'].str.replace('-',' ')
        map_user.State = map_user.State.str.title()
                        
        return map_user    

#Top TRANSACTION DISTRICTS

def trans_dist_top():
        top_path1 = 'C://Users/Welcome/pulse/data/top/transaction/country/india/state'
        top_state_list = os.listdir(top_path1)

        columns = {'State':[], 'Year':[],'Quarter':[],'District_name':[], 'Top_Transac_count':[],'Top_Transac_amount':[]}

        for i in top_state_list:
                p_i = top_path1 + '/' + i
                top_yr = os.listdir(p_i)
                
                for j in top_yr:
                        p_j = p_i + '/'+ j
                        top_yr_list = os.listdir(p_j)
                        
                        for k in top_yr_list:
                                p_k = p_j + '/'+ k
                                
                                if os.path.isfile(p_k):
                                    Data = open(p_k,'r')
                                    D= json.load(Data)
                                #pprint.pprint(D['data']['districts'])
                                data = D['data']['districts']
                                for z in data:
                                        #pprint.pprint(z)
                                        district = z['entityName']
                                        count = z['metric']['count']
                                        amount = z['metric']['amount']
                                        columns['District_name'].append(district)
                                        columns['Top_Transac_count'].append(count)
                                        columns['Top_Transac_amount'].append(amount)
                                        columns['State'].append(i)
                                        columns['Year'].append(j)
                                        columns['Quarter'].append(k.strip('.json'))
                        
        top_trans = pd.DataFrame(columns)
        top_trans['State'] = top_trans['State'].replace(['andaman-&-nicobar-islands'],'Andaman & Nicobar')
        top_trans['State'] = top_trans['State'].replace(['dadra-&-nagar-haveli-&-daman-&-diu'],'Dadra and Nagar Haveli and Daman and Diu')
        top_trans['State'] = top_trans['State'].str.replace('-',' ')
        top_trans.State = top_trans.State.str.title()              
        return top_trans 

#Top TRANSACTION PINCODES

def trans_pin_top():
        top_path_1 = 'C://Users/Welcome/pulse/data/top/transaction/country/india/state'
        top_state_list = os.listdir(top_path_1)

        columns = {'State':[], 'Year':[],'Quarter':[],'Pincode':[], 'Top_Transac_count':[],'Top_Transac_amount':[]}

        for i in top_state_list:
                p_i = top_path_1 + '/' + i
                top_yr = os.listdir(p_i)
                
                for j in top_yr:
                        p_j = p_i + '/'+ j
                        top_yr_list = os.listdir(p_j)
                        
                        for k in top_yr_list:
                                p_k = p_j + '/'+ k
                                
                                if os.path.isfile(p_k):
                                    Data = open(p_k,'r')
                                    D= json.load(Data)
                                #pprint.pprint(D)
                                data = D['data']['pincodes']
                                for z in data:
                                    
                                        code = z['entityName']
                                        count = z['metric']['count']
                                        amount = z['metric']['amount']
                                        columns['Pincode'].append(code)
                                        columns['Top_Transac_count'].append(count)
                                        columns['Top_Transac_amount'].append(amount)
                                        columns['State'].append(i)
                                        columns['Year'].append(j)
                                        columns['Quarter'].append(k.strip('.json'))
                            
        top_trans_pin = pd.DataFrame(columns)
        top_trans_pin['State'] = top_trans_pin['State'].replace(['andaman-&-nicobar-islands'],'Andaman & Nicobar')
        top_trans_pin['State'] = top_trans_pin['State'].replace(['dadra-&-nagar-haveli-&-daman-&-diu'],'Dadra and Nagar Haveli and Daman and Diu')
        top_trans_pin['State'] = top_trans_pin['State'].str.replace('-',' ')
        top_trans_pin.State = top_trans_pin.State.str.title()              
        return top_trans_pin        

#Top USER DISTRICTS

def user_dist_top():
        top_path2 = 'C://Users/Welcome/pulse/data/top/user/country/india/state'
        top_state_list = os.listdir(top_path2)

        columns = {'State':[], 'Year':[],'Quarter':[],'District_name':[], 'Registered_Users':[]}

        for i in top_state_list:
                p_i = top_path2 + '/'+ i
                top_yr = os.listdir(p_i)
                
                for j in top_yr:
                        p_j = p_i + '/'+j
                        top_files = os.listdir(p_j)
                        
                        for k in top_files:
                                p_k = p_j + '/'+k
                                Data = open(p_k,'r')
                                D = json.load(Data)
                                #pprint.pprint(D)
                                data = D['data']['districts']
                                for z in data:
                                        #pprint.pprint(z)
                                        district = z['name']
                                        users = z['registeredUsers']
                                        
                                        columns['District_name'].append(district)
                                        columns['Registered_Users'].append(users)
                                        columns['State'].append(i)
                                        columns['Year'].append(j)
                                        columns['Quarter'].append(k.strip('.json'))
                        
        top_user= pd.DataFrame(columns)
        top_user['State'] = top_user['State'].replace(['andaman-&-nicobar-islands'],'Andaman & Nicobar')
        top_user['State'] = top_user['State'].replace(['dadra-&-nagar-haveli-&-daman-&-diu'],'Dadra and Nagar Haveli and Daman and Diu')
        top_user['State'] = top_user['State'].str.replace('-',' ')
        top_user.State = top_user.State.str.title()              
        return top_user               

#Top USER PRINCODES

def user_pin_top():
        top_path_2 = 'C://Users/Welcome/pulse/data/top/user/country/india/state'
        top_state_list = os.listdir(top_path_2)

        columns = {'State':[], 'Year':[],'Quarter':[],'Pincode':[], 'Registered_Users':[]}

        for i in top_state_list:
                p_i = top_path_2 + '/'+ i
                top_yr = os.listdir(p_i)
                
                for j in top_yr:
                        p_j = p_i + '/'+j
                        top_files = os.listdir(p_j)
                        
                        for k in top_files:
                                p_k = p_j + '/'+k
                                Data = open(p_k,'r')
                                D = json.load(Data)
                                #pprint.pprint(D)
                                data = D['data']['pincodes']
                                for z in data:
                                        #pprint.pprint(z)
                                        code = z['name']
                                        users = z['registeredUsers']
                                        
                                        columns['Pincode'].append(code)
                                        columns['Registered_Users'].append(users)
                                        columns['State'].append(i)
                                        columns['Year'].append(j)
                                        columns['Quarter'].append(k.strip('.json'))
                            
        top_user_pin= pd.DataFrame(columns)
        top_user_pin['State'] = top_user_pin['State'].replace(['andaman-&-nicobar-islands'],'Andaman & Nicobar')
        top_user_pin['State'] = top_user_pin['State'].replace(['dadra-&-nagar-haveli-&-daman-&-diu'],'Dadra and Nagar Haveli and Daman and Diu')
        top_user_pin['State'] = top_user_pin['State'].str.replace('-',' ')
        top_user_pin.State = top_user_pin.State.str.title()              
        return top_user_pin   
    
#SQL TRANSFER

def sql_transfer():
    
        from sqlalchemy import create_engine
        engine = create_engine('postgresql://postgres:SU@localhost:5433/Phonepe')

        trans_agg().to_sql('agg_transac', con=engine, if_exists='replace')
        user_agg().to_sql('agg_user', con=engine, if_exists='replace')
        trans_map().to_sql('map_transac', con=engine, if_exists='replace')
        user_map().to_sql('map_user', con=engine, if_exists='replace')
        trans_dist_top().to_sql('top_dis_transac', con=engine, if_exists='replace')
        trans_pin_top().to_sql('top_pin_transac', con=engine, if_exists='replace')
        user_dist_top().to_sql('top_dis_user', con=engine, if_exists='replace')
        user_pin_top().to_sql('top_pin_user', con=engine, if_exists='replace')
        conn = engine.connect()
        conn.close()
sql_transfer()

#Streamlit and visualisations

from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:SU@localhost:5433/Phonepe')

st.set_page_config(page_title = 'Phonepe Pulse Data Visualization and Exploration',layout='wide') 

cl1,cl2,cl3 = st.columns(3)
with cl2:
        st.markdown('<img style="float: center;" src="https://miro.medium.com/v2/resize:fit:350/format:webp/1*WG_NcuKQE6uRQmGAhJ89Mg.png" />', unsafe_allow_html=True)
st.markdown('<h1 style="text-align: center;color: #0D7F4F;">Phonepe Data Visualization and Exploration 2018-2023</h1>', unsafe_allow_html=True)
st.divider()

n1,n2,n3 = st.columns(3)
with n1:
       option_A = st.selectbox(":blue[Top Transactions and Users Trends Across India]",("Transactions", "User"),index=0)
with n2:
       option_C = st.selectbox(":blue[Quarter]",('1','2','3','4'),index=0)
with n3:
       option_B = st.selectbox(":blue[Year]",('2018','2019','2020','2021','2022','2023'),index=0)
col1, col2 = st.columns(2)
with col1:
        user_data = pd.read_sql_query('select "Transaction_type" as "Categories" ,sum("Transaction_count") as "Total_transactions"  from agg_transac  group by "Transaction_type"  order by "Total_transactions" desc ',con = engine)
        tab1, tab2,tab3,tab4,tab5= st.tabs(["Categories","Visualisation","States","Districts","PostalCodes"])
        with tab1:
               st.markdown("<h4 style='text-align: left; color: #063F27;'>Transactions by Categories </h4>", unsafe_allow_html=True)
               st.table(user_data) 
        with tab2:       
               fig = px.pie(user_data, values='Total_transactions', names="Categories",color_discrete_sequence=px.colors.sequential.RdBu,hole = 0.5,title = 'Transactions By Categories')
               fig.update_layout(legend=dict(
                                yanchor="top",
                                y=0.99,
                                xanchor="left",
                                x=0.01
                                ))

               
               st.plotly_chart(fig, use_container_width=False) 
               
        with tab3:
               state = pd.read_sql_query('select "State" as "Top 10 States" ,sum("Transaction_count") as "Total_Transactions" from agg_transac group by "State" order by "Total_Transactions" desc limit(10)',con =engine)
               st.table(state)
        with tab4:
               dist = pd.read_sql_query('select "District_name" as "Top 10 districts",sum("Top_Transac_amount") as "Total_amount" from top_dis_transac group by "District_name" order by "Total_amount" desc limit(10)',con = engine)
               st.table(dist)
        with tab5:
               pin = pd.read_sql_query('select "Pincode" as "Top 10 Postal Codes",sum("Top_Transac_amount") as "Total_amount" from top_pin_transac group by "Pincode" order by "Total_amount" desc limit(10) ',con=engine)
               st.table(pin)


#Geo Map visualization
st_info = open('F:\Learnings\DataScientist\GUVI\Phonepe\india_states.geojson','r')
Indian_states = json.load(st_info)
with col2:    
        if option_A == "Transactions" and option_B == option_B and option_C == option_C:
                data = pd.read_sql_query('select "State","Year","Quarter",sum("Transaction_count") as "Transactions_count" from agg_transac group by "State","Year","Quarter" order by "State"',con=engine)
                df = data.groupby(["State","Year","Quarter"]).sum().reset_index()
                comp_data = df[(df['Year']==option_B) & (df['Quarter']==int(option_C))]
                fig = px.choropleth(
                comp_data,
                geojson= Indian_states,
                featureidkey='properties.ST_NM',
                locations='State',
                color="Transactions_count",
                hover_name= "State",
                hover_data= ['Year','Quarter','Transactions_count'],
                color_continuous_scale= 'curl',
                projection='mercator',
                )

                fig.update_geos(fitbounds="locations", visible=False)
                fig.update_layout(height=800,width=800)
                st.plotly_chart(fig, use_container_width=False)
        elif option_A == "User":
                data = pd.read_sql_query('select "State","Year","Quarter",sum("User_count") as "Users_count" from agg_user group by "State","Year","Quarter" order by "State"',con=engine)
                df = data.groupby(["State","Year","Quarter"]).sum().reset_index()
                user_data = df[(df['Year']==option_B) & (df['Quarter']==int(option_C))]
                fig = px.choropleth(
                        user_data,
                        geojson= Indian_states,
                        featureidkey='properties.ST_NM',
                        locations='State',
                        color="Users_count",
                        hover_name= "State",
                        hover_data= ['Year','Quarter','Users_count'],
                        color_continuous_scale= 'RdBu',
                        projection='mercator',
                        )

                fig.update_geos(fitbounds="locations", visible=False)
                fig.update_layout(height=800,width=800)
                
                st.plotly_chart(fig, use_container_width=False)

c1,c2 = st.columns(2)
with c1:
        st.markdown("<h4 style='text-align: center; color: #063F27;'>Transaction Trend over the Years </h4>", unsafe_allow_html=True)
        opt = st.selectbox("Chart Type",('Line','Bar'),index=0)
        yearly_trend= pd.read_sql_query('select "Year",sum("Transaction_count") as "Total Transactions" from agg_transac group by "Year" order by "Year"',con = engine)
        if opt == 'Line':
                fig = px.line(yearly_trend, x="Year", y='Total Transactions',markers =True)
                st.plotly_chart(fig, use_container_width=True)
        elif opt == 'Bar':
                fig = px.bar(yearly_trend,x='Year',y = 'Total Transactions',color_discrete_sequence=px.colors.sequential.RdBu)
                st.plotly_chart(fig, use_container_width=True)
with c2:
       st.markdown("<h4 style='text-align: center; color: #063F27;'>Users Trend over the Years </h4>", unsafe_allow_html=True)
       user_trend = pd.read_sql_query('select "Year",sum("User_count") as "User_count" from agg_user group by "Year" order by "Year"',con=engine)
       opt1 = st.selectbox("Chart Type",('Line Chart','Bar Chart'),index=0)
       if opt1 == 'Line Chart':
              fig = px.line(user_trend, x="Year", y='User_count',markers =True)
              st.plotly_chart(fig, use_container_width=True)
       elif opt1 == 'Bar Chart':       
              fig = px.bar(user_trend,x='Year',y = 'User_count',color_discrete_sequence=px.colors.sequential.RdBu)
              st.plotly_chart(fig, use_container_width=True)
st.markdown("<h1 style='text-align: center; color: #063F27;'>State Level Transactions </h1>", unsafe_allow_html=True)
a1,a2= st.columns(2)
with a1:
        option1 = st.selectbox(
        'State',
        ('Andaman & Nicobar', 'Andhra Pradesh', 'Arunachal Pradesh',
        'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh',
        'Dadra And Nagar Haveli And Daman And Diu', 'Delhi', 'Goa',
        'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu & Kashmir',
        'Jharkhand', 'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep',
        'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram',
        'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan',
        'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh',
        'Uttarakhand', 'West Bengal')) 
with a2:
        option2 = st.selectbox('Year',('2018','2019','2020','2021','2022','2023'))

st.write('You selected:', option1,option2)
x1,x2 = st.columns(2)
with x2:
        st_data = pd.read_sql_query('select "State","Year","Quarter",sum("Transaction_count") as "Transactions_count" from agg_transac group by "State","Year","Quarter" order by "State" ',con=engine)
        data =st_data[(st_data['State']==option1) & (st_data['Year']==option2)]
        st.dataframe(data,hide_index=True)
with x1:
        fig = px.bar(data, x="Quarter",y="Transactions_count")
        fig.update_layout(height=300, width=500)
        st.plotly_chart(fig, use_container_width=False)
