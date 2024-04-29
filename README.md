# api-development-using-flask

## IPL Dataset Analysis API
This project provides an API built using Flask for analyzing IPL (Indian Premier League) cricket match data. It allows users to retrieve various insights and statistics from the IPL dataset, including team 
performance, match outcomes, player statistics, and more.

### Features
  1. Team Performance Analysis: Shows total no. of teams played in IPL.
  2. Head-to-Head Analysis: Compare the performance of two teams against each other, including the total number of matches played, matches won by each team, matches drawn, and more.
  3. Player Statistics: Get detailed statistics for individual players, including total runs scored, wickets taken, batting strike rate, bowling economy rate, and more.

### Access the API endpoints in your web browser or using tools like Postman:
Base URL: **http://localhost:5000**
#### Available endpoints:
1. /api/teams
2. /api/teamVSteam?team1=<team_name1>&team2=<team_name2>
3. /api/batting-record?batsman=<batsman_name>
4. /api/bowling-record?bowler=<bowler_name>

