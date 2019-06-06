from app import application, db
from app.models import User, Post
from flask import abort, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URI = application.config.get('SQLALCHEMY_DATABASE_URI')
ENGINE = create_engine(DATABASE_URI)

def create_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()

@application.route('/')
def index():
    return "At index page"

@application.route('/hello-world')
def helloWorld():
    return "Hello, World!"

# Returns a collection of users
@application.route('/users', methods=['GET'])
def get_users():
    current_session = create_session(ENGINE)

    users = list(current_session.execute("SELECT * FROM user u"))
    if len(users) == 0:
        current_session.close()
        abort(404)

    current_session.close()
    return jsonify({'users': [dict(row) for row in users]})

# Returns a user
@application.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    current_session = create_session(ENGINE)

    users = list(current_session.execute("SELECT * FROM user u WHERE u.id = " + str(user_id)))
    if len(users) == 0:
        current_session.close()
        abort(404)

    current_session.close()
    return jsonify({'users': [dict(row) for row in users]})

# Returns a collection of posts by specified user
@application.route('/users/<int:user_id>/posts', methods=['GET'])
def get_posts(user_id):
    current_session = create_session(ENGINE)

    posts = list(current_session.execute("SELECT * FROM post p WHERE p.user_id = " + str(user_id)))
    if len(posts) == 0:
        current_session.close()
        abort(404)

    current_session.close()
    return jsonify({'posts': [dict(row) for row in posts]})

# Creates a post for the specified user
@application.route('/users/<int:user_id>/posts', methods=['POST'])
def create_post(user_id):
    if not request.json or not 'body' in request.json:
        abort(400)

    current_session = create_session(ENGINE)

    input_body = request.json['body']
    post = Post(body=input_body, user_id=user_id)
    db.session.add(post)
    db.session.commit()
    current_session.close()
    return jsonify({'post': str(post)}), 201

# Deletes the specified posts of the user
@application.route('/users/<int:user_id>/posts/<int:post_id>', methods=['DELETE'])
def delete_task(user_id, post_id):
    current_session = create_session(ENGINE)

    # Note that since post.id is a primary key, it is actually sufficient to query without user_id
    query = "SELECT * FROM post p WHERE p.user_id = " + str(user_id) + " AND p.id = " + str(post_id)

    post = list(current_session.execute(query))
    if len(post) == 0:
        current_session.close()
        abort(404)
    delete_query = "DELETE FROM post AS p WHERE p.user_id = " + str(user_id) + " AND p.id = " + str(post_id)
    # Note that delete query need to be executed from the db session and not the current session
    db.session.execute(delete_query)
    db.session.commit()
    current_session.close()
    return jsonify({'result': True})

# Updates a post for the specified user. 
@application.route('/users/<int:user_id>/posts/<int:post_id>', methods=['PUT'])
def update_post(user_id, post_id):
    current_session = create_session(ENGINE)

    query = "SELECT * FROM post p WHERE p.id = " + str(post_id)
    post = list(current_session.execute(query))
    if len(post) == 0:
        current_session.close()
        abort(404)
    if not request.json:
        current_session.close()
        abort(400)

    post = Post.query.filter_by(id=post_id).update(dict(body=request.json['body']))
    db.session.flush()
    db.session.commit()
    post = Post.query.get(post_id)
    current_session.close()
    return jsonify({'post': str(post)})

if  __name__ == '__main__':
    app.run(debug=True)