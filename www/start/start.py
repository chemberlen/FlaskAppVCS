import os
from .FlaskApp import app, db

from .FlaskApp.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

# if __name__ == '__main__':
#     app.debug = True
#     host = os.environ.get('IP', '0.0.0.0')
#     port = int(os.environ.get('PORT', 5000))
#     app.run(host=host, port=port)