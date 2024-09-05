from flask import Blueprint, render_template, flash, request, jsonify
from flask_login import login_required, current_user
from .models import Query 
from . import db 
import json 
from BasicChatbot.Chatbot import respond


views = Blueprint("views", __name__)
@views.route("/home", methods=['GET', 'POST'])
@login_required
def home():

    if request.method == 'POST': 
        query = request.form.get('query')#Gets the note from the HTML 
        
        if len(query) < 3:
            flash('Query is too short!', category='error') 
        else:
            resp, tag = respond(query)

            new_query = Query(data=query, response = resp, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_query) #adding the note to the database 
            db.session.commit()
    return render_template("home.html", user = current_user)

@views.route('/delete-query', methods=['POST'])
def delete_query():  
    query = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    queryId = query['queryId']
    query = Query.query.get(queryId)
    if query:
        if query.user_id == current_user.id:
            db.session.delete(query)
            db.session.commit()

    return jsonify({})