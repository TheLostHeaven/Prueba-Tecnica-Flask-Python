#Archivo donde se inicializa la app
from app import app_create, db
from src.utils.rolecreate import create_roles, create_admin_user

app = app_create()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        create_roles()
        create_admin_user()
    app.run(debug=True)
