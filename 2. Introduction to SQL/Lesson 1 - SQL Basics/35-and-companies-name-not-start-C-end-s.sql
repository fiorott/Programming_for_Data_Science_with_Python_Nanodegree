/*
Programming for Data Science with Python Nanodegree
Udacity's certified program
SQL practice > Lesson 1 : SQL Basics

Using the accounts table, find all the companies whose names do not start
with 'C' and end with 's'.
*/


SELECT name
FROM accounts
WHERE name NOT LIKE 'C%' AND name LIKE '%s';
