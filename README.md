Docker & SQL Homework - 2026This repository contains my solutions for the Docker and SQL homework module. The tasks involve containerizing a Python environment, querying taxi trip data in PostgreSQL, and understanding Terraform workflows.🛠️ SolutionsQuestion 1: Pip Version in Python 3.13Answer: 25.3Bash# Command used:
docker run -it --rm --entrypoint=bash python:3.13-slim
pip -V
Question 2: Docker NetworkingAnswer: db:5432Explanation: In a docker-compose setup, the hostname is the service name defined in the YAML file.📊 SQL QueriesThe following queries were performed on the green_taxi_trips and zones tables.Question 3: Trip Distance AnalysisQuestion: For trips in November 2025, how many trips had a trip_distance $\le 1$ mile?Answer: 8007<details><summary>Click to view SQL Code</summary>SQLSELECT count(*) 
FROM green_taxi_trips 
WHERE lpep_pickup_datetime >= '2025-11-01' 
  AND lpep_dropoff_datetime < '2025-12-01' 
  AND trip_distance <= 1.0;
</details>Question 4: Longest Trip DayQuestion: Which was the pickup day with the longest trip distance (considering trips < 100 miles)?Answer: 2025-11-14<details><summary>Click to view SQL Code</summary>SQLSELECT lpep_pickup_datetime, trip_distance 
FROM green_taxi_trips
WHERE trip_distance < 100.0 
ORDER BY trip_distance DESC;
</details>Question 5: Largest Total Amount by ZoneQuestion: Which pickup zone had the largest total_amount on November 18th, 2025?Answer: East Harlem North<details><summary>Click to view SQL Code</summary>SQLSELECT z."Zone", SUM(g.total_amount) 
FROM green_taxi_trips g 
INNER JOIN zones z ON g."PULocationID" = z."LocationID"
WHERE DATE(g.lpep_pickup_datetime) = '2025-11-18'
GROUP BY z."Zone" 
ORDER BY SUM(g.total_amount) DESC;
</details>Question 6: Largest Tip (Drop-off Zone)Question: For passengers picked up in "East Harlem North" in Nov 2025, which drop-off zone had the largest tip?Answer: Yorkville West<details><summary>Click to view SQL Code</summary>SQLSELECT z2."Zone", MAX(g.tip_amount) 
FROM green_taxi_trips g
INNER JOIN zones z ON g."PULocationID" = z."LocationID" 
INNER JOIN zones z2 ON g."DOLocationID" = z2."LocationID" 
WHERE z."Zone" = 'East Harlem North'
  AND DATE(lpep_pickup_datetime) >= '2025-11-01'  
  AND DATE(lpep_dropoff_datetime) < '2025-12-01'
GROUP BY z2."Zone" 
ORDER BY MAX(g.tip_amount) DESC;
</details>🌍 Infrastructure (Terraform)Question 7: Terraform WorkflowSequence: terraform init, terraform apply -auto-approve, terraform destroyInit: Downloads plugins and initializes the backend.Apply: Generates the plan and executes changes.Destroy: Removes all managed infrastructure.
