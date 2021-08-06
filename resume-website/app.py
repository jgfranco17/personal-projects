# Launches an instance of the Flask application

from website import create_app

if __name__ == '__main__':
    try:
        app = create_app()
        app.run(debug = True)
    except Exception as e:
        print(f'Error encountered during app start: {e}')