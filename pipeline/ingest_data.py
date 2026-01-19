import click
import pandas as pd
from sqlalchemy import create_engine

@click.command()
@click.option(
    '--url',
    default='https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv',
    help='CSV file URL'
)
@click.option(
    '--user',
    default='root',
    help='Database user'
)
@click.option(
    '--password',
    default='root',
    help='Database password'
)
@click.option(
    '--host',
    default='localhost',
    help='Database host'
)
@click.option(
    '--port',
    default=5432,
    type=int,
    help='Database port'
)
@click.option(
    '--db',
    default='ny_taxi',
    help='Database name'
)
@click.option(
    '--table',
    default='yellow_taxi_data',
    help='Target table name'
)
@click.option(
    '--chunksize',
    default=100000,
    type=int,
    help='Number of rows per chunk'
)
def main(url, user, password, host, port, db, table, chunksize):
    """Ingest NYC taxi data into PostgreSQL database."""
    
    # Construct database URL from parameters
    db_url = f'postgresql://{user}:{password}@{host}:{port}/{db}'
    
    # dtype = {
    #     "VendorID": "Int64",
    #     "passenger_count": "Int64",
    #     "trip_distance": "float64",
    #     "RatecodeID": "Int64",
    #     "store_and_fwd_flag": "string",
    #     "PULocationID": "Int64",
    #     "DOLocationID": "Int64",
    #     "payment_type": "Int64",
    #     "fare_amount": "float64",
    #     "extra": "float64",
    #     "mta_tax": "float64",
    #     "tip_amount": "float64",
    #     "tolls_amount": "float64",
    #     "improvement_surcharge": "float64",
    #     "total_amount": "float64",
    #     "congestion_surcharge": "float64"
    # }

    # parse_dates = [
    #     "tpep_pickup_datetime",
    #     "tpep_dropoff_datetime"
    # ]

    df = pd.read_csv(
        url,
        #dtype=dtype,
        iterator=True,
        chunksize=chunksize
    )

    engine = create_engine(db_url)
    first = True
    # df.head(0).to_sql(
    #             name=table,
    #             con=engine,
    #             if_exists="replace"
    #         )
    # # print("Table created")        

    for df_chunk in df:
        if first:
            df_chunk.head(0).to_sql(
                name=table,
                con=engine,
                if_exists="replace"
            )
            first = False
            print("Table created")

        df_chunk.to_sql(
                name=table,
                con=engine,
                if_exists="append"
            )
        print("Inserted:", len(df_chunk))
if __name__ == '__main__':
    main()




