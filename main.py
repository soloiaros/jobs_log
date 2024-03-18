from flask import Flask, render_template
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandex_secret_key'


@app.route('/')
def log_page():
    return render_template('index.html', list_of_jobs=db_session.create_session().query(Jobs).all())


def main():
    db_session.global_init("db/blogs.db")
    app.run()


if __name__ == '__main__':
    main()
