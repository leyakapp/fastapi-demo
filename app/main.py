#!/usr/bin/env python3

import os
import MySQLdb
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from models import Item, Album
import json
import os
import MySQLdb
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static", html=True), name="static")

DBHOST = os.environ.get('DBHOST')
DBUSER = os.environ.get('DBUSER')
DBPASS = os.environ.get('DBPASS')
DB = "mth8yq"  # replace with your UVA computing ID / database name
# db config stuff

@app.get("/")  # zone apex
def zone_apex():
    return {"Hello": "WorldWide web"}

@app.get("/albums")
def get_albums():
    db = MySQLdb.connect(host=DBHOST, user=DBUSER, passwd=DBPASS, db=DB)
    c = db.cursor(MySQLdb.cursors.DictCursor)
    c.execute("SELECT * FROM albums ORDER BY name")
    results = c.fetchall()
    db.close()
    return results
    
@app.get("/albums/{id}")
def get_one_album(id):
    db = MySQLdb.connect(host=DBHOST, user=DBUSER, passwd=DBPASS, db=DB)
    c = db.cursor(MySQLdb.cursors.DictCursor)
    c.execute("SELECT * FROM albums WHERE id=" + id)
    results = c.fetchall()
    db.close()
    return results

# @app.get("/albums/{id}")
# def get_one_album(id):
#     db = MySQLdb.connect(host=DBHOST, user=DBUSER, passwd=DBPASS, db=DB)
#     c = db.cursor(MySQLdb.cursors.DictCursor)
#     c.execute("SELECT * FROM albums WHERE id=" + id)
#     results = c.fetchall()
#     db.close()
#     return results
    




# @app.post("/albums")
# def add_an_album(album: Album):
#     return {"name": album.name, "artist":album.artist, "genre": album.genre, "year":album.year}



# @app.post("/items/{item_id}")
# def add_item(item_id: int, item: Item):
#     return {"item_id": item_id, "item_name": item.name}

# @app.delete("/items/{item_id}")
# def delete_item(item_id: int, item: Item):
#     return {"action": "deleted", "item_id": item_id}

@app.patch("/items/{item_id}")
def patch_item(item_id: int, item: Item):
   return {"action": "patch", "item_id": item_id}


@app.get("/example_data")   
def get_example_data():
    # Just an example list of dictionaries
    example_data = [
        {"id": 1, "data": "Example 1"},
        {"id": 2, "data": "Example 2"},
        {"id": 3, "data": "Example 3"},
    ]
    return example_data
