"""
Здесь второй вариант запуска приложени через фабрику приложений
"""
from blog.app import create_app

app = create_app()
if __name__ == '__main__':
    app.run()

