#  🐳 **Docker-2026**

## **Question 1. What's the version of pip in the python:3.13 image?**

**Answer** : 25.3

**code** :

          @Abdullah-Rashad-Ali ➜ /workspaces/Docker-2026/pipeline (main) $ docker run -it --rm --entrypoint=bash python:3.13-slim
          root@098ad2fed1d0:/# pip -V
          pip 25.3 from /usr/local/lib/python3.13/site-packages/pip (python 3.13)

## **Question 2. Given the docker-compose.yaml, what is the hostname and port that pgadmin should use to connect to the postgres database?**

**Answer** : db:5432

## **Question 3. For the trips in November 2025, how many trips had a trip_distance of less than or equal to 1 mile?**

**answer** : 8007

**code** :
          ```sql 
					select count(*) from green_taxi_trips where lpep_pickup_datetime >= '2025-11-01' 
          and lpep_dropoff_datetime < '2025-12-01' and trip_distance <= 1.0;
					```
					
## **Question 4. Which was the pick up day with the longest trip distance? Only consider trips with trip_distance less than 100 miles.**

**Answer** : 2025-11-14

**Code** : 
          ```sql
					select lpep_pickup_datetime , trip_distance from green_taxi_trips
          where trip_distance < 100.0 order by trip_distance desc;```

## **Question 5. Which was the pickup zone with the largest total_amount (sum of all trips) on November 18th, 2025?**

**Answer**: East Harlem North

**Code** : 
          ```sql
					select z."Zone" , sum(g.total_amount) from green_taxi_trips g inner join zones z on g."PULocationID" = z."LocationID"
          where DATE(g.lpep_pickup_datetime) = '2025-11-18'
          group by z."Zone" order by sum(g.total_amount) desc;```

## **Question 6. For the passengers picked up in the zone named "East Harlem North" in November 2025, which was the drop off zone that had the largest tip?**

**Answer** : Yorkville West

**Code**: 
          ```sql
					select  z2."Zone" , max(g.tip_amount) from green_taxi_trips g
          inner join zones z on g."PULocationID" = z."LocationID" 
          inner join zones z2 on g."DOLocationID" = z2."LocationID" 
          where  z."Zone" = 'East Harlem North'
          	   and DATE(lpep_pickup_datetime) >= '2025-11-01'  
          	   and DATE(lpep_dropoff_datetime) < '2025-12-01'
          group by  z2."Zone" 
          order by max(g.tip_amount) desc;```

## **Question 7. Which of the following sequences describes the Terraform workflow for: 1) Downloading plugins and setting up backend, 2) Generating and executing changes, 3) Removing all resources?**

**Answer** : terraform init, terraform apply -auto-approve, terraform destroy
