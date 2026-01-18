#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd


# In[5]:


prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/'
url = f'{prefix}/yellow_tripdata_2021-01.csv.gz'


# In[6]:


url


# In[44]:


dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]

df = pd.read_csv(
    url,
    dtype=dtype,
    iterator=True,
    chunksize=100000
)


# In[45]:


df.head()


# In[40]:


df['tpep_pickup_datetime']


# In[13]:


df['VendorID'].isnull()


# In[16]:


get_ipython().system('uv add sqlAlchemy psycopg2-binary')


# In[34]:


from sqlalchemy import create_engine
engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')



# In[35]:


print(pd.io.sql.get_schema(df, name='yellow_taxi_data', con=engine))


# In[36]:


df.head(n=0).to_sql(name='yellow_taxi_data', con=engine, if_exists='replace')


# In[42]:


for df_chunk in df:
    print(len(df_chunk))


# In[47]:


df.to_sql(name='yellow_taxi_data', con=engine, if_exists='replace')


# In[48]:


first = True

for df_chunk in df:

    if first:
        # Create table schema (no data)
        df_chunk.head(0).to_sql(
            name="yellow_taxi_data",
            con=engine,
            if_exists="replace"
        )
        first = False
        print("Table created")

    # Insert chunk
    df_chunk.to_sql(
        name="yellow_taxi_data",
        con=engine,
        if_exists="append"
    )

    print("Inserted:", len(df_chunk))


# In[55]:


sql = 'select count(*) from ny_taxi.yellow_taxi_date'
pd.read_sql_query(sql,con=engine)


# In[ ]:




