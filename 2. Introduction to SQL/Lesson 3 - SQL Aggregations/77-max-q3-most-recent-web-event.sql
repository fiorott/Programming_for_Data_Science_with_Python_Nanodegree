/*
Programming for Data Science with Python Nanodegree
Udacity's certified program > SQL practice > Lesson 3 : SQL Aggregations

When did the most recent (latest) web_event occur?
*/



SELECT MAX(w.occurred_at) most_recent_web_event
FROM web_events w;
