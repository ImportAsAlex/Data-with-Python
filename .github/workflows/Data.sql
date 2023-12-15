Opened MySQL Workbench to connect to the MySQL server.
Added the provided dataset to MySQL Workbench.
Ran a SQL query to retrieve all columns of the table between the years 2016-2019.

SELECT *
FROM finance_liquor_sales
WHERE date BETWEEN '2016-01-01' AND '2019-12-31' ;

Initial attempt to filter by the "year" column resulted in an empty grid.
Discovered that the dataset does not have a "year" column.

Modified the query to filter based on the "date" column.
Successfully retrieved data for the specified date range.

Exported the queried data to a CSV file from MySQL Workbench.

Clicked on the Export:
Named the file finance_liquor_sales 2016-2019
and I saved it to my Desktop 
