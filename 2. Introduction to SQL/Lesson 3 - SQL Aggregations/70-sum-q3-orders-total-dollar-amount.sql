/*
Programming for Data Science with Python Nanodegree
Udacity's certified program > SQL practice > Lesson 3 : SQL Aggregations

Find the total dollar amount of sales using the 'total_amt_usd' in
the 'orders' table.
*/



SELECT SUM(o.total_amt_usd) total_dollar_amount
FROM orders o;
