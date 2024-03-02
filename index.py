from app import app_create, db

app = app_create()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
