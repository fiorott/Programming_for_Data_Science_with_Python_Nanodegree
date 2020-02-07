/*
Programming for Data Science with Python Nanodegree
Udacity's certified program > SQL practice > Lesson 6 : SQL Window Functions

WINDOW FUNCTIONS:

Section 7: DENSE_RANK()


Question:
create a DENSE_RANK() for total_amt_usd with maximum being the lowest rank
and minimum being the lowest rank, partitioned by each account.
*/

SELECT account_id,
       DATE_PART('year', occurred_at) AS year,
       DATE_PART('month', occurred_at) AS month,
       total_amt_usd,
       DENSE_RANK() OVER (PARTITION BY account_id ORDER BY total_amt_usd DESC) AS max_spent_rank
FROM orders;

/*
Output6912 results
account_id	year	month	total_amt_usd	max_spent_rank
1001	2015	12	9426.71	1
1001	2016	1	9230.67	2
1001	2016	8	9134.31	3
1001	2016	9	8963.91	4
1001	2016	5	8863.24	5
1001	2015	11	8757.18	6
1001	2016	3	8672.95	7
1001	2016	2	8538.26	8
1001	2016	4	8343.09	9
1001	2016	5	8311.59	10
1001	2016	7	8286.99	11
1001	2016	11	7924.46	12
1001	2016	5	2052.20	13
1001	2016	10	1993.58	14
1001	2016	12	1719.28	15
1001	2015	11	1718.03	16
1001	2016	4	1498.20	17
1001	2016	11	1283.12	18
1001	2016	8	1182.61	19
1001	2016	3	1067.25	20
1001	2016	2	983.49	21
1001	2015	10	973.43	22
1001	2016	1	958.24	23
1001	2016	9	951.14	24
1001	2016	6	878.56	25
1001	2015	12	776.18	26
1001	2016	7	773.63	27
1001	2016	5	752.57	28
1011	2016	12	2734.59	1
1021	2016	1	2945.73	1
1021	2016	3	2944.24	2
1021	2015	11	2936.92	3
1021	2015	10	2747.11	4
1021	2015	10	2647.54	5
1021	2016	2	2608.02	6
1021	2015	12	2580.69	7
1021	2016	2	603.98	8
*/
