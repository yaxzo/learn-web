from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init() # сюда имя для создания бд
    app.run()


if __name__ == '__main__':
    main()
