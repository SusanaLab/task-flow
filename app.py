import flask import Flask, render_template, request, redirect, url_for
from src.database import DBManager
from src.models import Tarea, Proyecto


app = Flask(__name__)
db_manager = DBManager()

@app.route("/")
def index():
    tareas-pendientes=db_manager.obtener_tareas(estado="pendiente")
    proyectos=db_manager.obtener_proyectos()
    
    
    return render_template("index.html", tareas = tareas_pendientes, proyectos=proyectos)

