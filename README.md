# Vue-fastapi-CRUD-PostgreSQL

This project is a CRUD application built using FastAPI and Vue.js, where users
can manage notes and perform basic operations like creating, reading, updating,
and deleting notes. The project uses OAuth2 for user authentication and PostgreSQL
as the database with Tortoise ORM.

It is built in docker, using one container for each part of the project,
one for backend, one for frontend and one for database.

Features
User:
    * Create a user
    * Delete a user

Notes:
    * Create a note
    * Delete a note
    * Edit a note
    * Read a note
    
Authentication:
-Users can only delete or edit a note if they are authenticated, and they must be
the creator of the note.

-User Authentication:
OAuth2 is used for user authentication to secure the application.


Frontend Integration
The frontend is built using Vue.js and communicates with the backend using
API endpoints. The frontend components are organized under src/components,
and views are placed in the src/views directory.

Authentication Flow
The project implements OAuth2 for user authentication. Users can obtain
an access token by logging in with valid credentials. The access token
must be included in the header of requests to access secured endpoints.







