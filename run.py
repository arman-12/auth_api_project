from app import create_app

app = create_app()

if __name__ == '__main__':
    app.secret_key = 'your-secret-key'  # Replace with a secure key
    app.run(debug=True)
