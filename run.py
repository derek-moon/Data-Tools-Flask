from app import create_app, db
from app.models import User

app = create_app()

@app.shell_context_processor
def get_context():
    return dict(app=app, db=db )