
# Coded Together App

This web application includes CRUD operations of Coded Together App.

# Endpoints

| HTTP Method  | URL |
| ------------- | ------------- |
| GET, POST  | /login  | 
| GET, POST  | /sign-up  |
| GET, POST  | /  | - Home page(login is required)
| PATCH/PUT  | /update_project  | # not coded yet
| DELETE  | /delete_project  |


# Project Design
I designed the project during my time at Nucamp's Back-End & DevOps bootcamp. I came up with the idea of users post projects and join/work together to build projects of their own together. This came up to me when I wanted to start a project but it was too much to handle on my own and wished there was a partner I can do it with and build techincal skills together along with building teamwork. 

# Database Implementation
Prior to implementing PostgreSQL, I designed a ER Diagram that best relates to the project. Project will have ONE owner and can have MANY Users. MANY Projects can belong to MANY Users.

# Technologies Used (check requirements.txt)
- Python
- PostgreSQL
- Docker
- SQLAlchemy
- Flask
- Werkzeug
