/*
Programming for Data Science with Python Nanodegree
Udacity's certified program > SQL practice > Lesson 3 : SQL Aggregations

Find the total no of 'poster_qty' paper orders in the 'orders' table.
*/



SELECT COUNT(o.poster_qty) total_poster_qty
FROM orders o;
