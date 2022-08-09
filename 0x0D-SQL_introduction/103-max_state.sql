-- display the max temp of each state ordered by state
SELECT state, MAX(value) as max_temp
FROM temperatures
GROUP BY state;
