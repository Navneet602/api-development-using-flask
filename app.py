from flask import Flask, jsonify, request
import ipl
import jugaad
app = Flask(__name__)

@app.route('/')
def home():
    return "hello world"

@app.route('/api/teams')
def teams():
    # returning a string we have to convert string into json
    # by go to ipl.py file instead of return we can store it in teams
    # then make a team_dict variable and return that variable
    # then we go to app.py file and import jsonify built-in func in flask
    team = ipl.teamsAPI()
    return jsonify(team)
@app.route('/api/teamVSteam')
def teamVSteam():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')
    response = ipl.teamVSteamAPI(team1,team2)
    return jsonify(response)
@app.route('/api/team-record')
def team_record():
    team_name = request.args.get('team')
    response = jugaad.teamAPI(team_name)
    return response

@app.route('/api/batting-record')
def batting_record():
    batsman_name = request.args.get('batsman')
    response = jugaad.batsmanAPI(batsman_name)
    return response

@app.route('/api/bowling-record')
def bowling_record():
    bowler_name = request.args.get('bowler')
    response = jugaad.bowlerAPI(bowler_name)
    return response

app.run(debug=True)
