/*
Programming for Data Science with Python Nanodegree
Udacity's certified program
SQL practice > Lesson 1 : SQL Basics

Use the accounts table to find:
All the companies whose names do not start with 'C'.
*/


SELECT name
FROM accounts
WHERE name NOT LIKE 'C%';
