import datetime

from flask import Flask, render_template, redirect
from data import db_session
from forms.user import RegisterForm
import sys

app = Flask(__name__)
from data.users import User
from data.jobs import Jobs

app.config['SECRET_KEY'] = 'second_flask_apexll'


def main():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    # user = User()
    # user.surname = 'Scott'
    # user.name = "Ridley"
    # user.age = 21
    # user.position = "captain"
    # user.speciality = 'research engineer'
    # user.address = 'module_1'
    # user.email = "scott_chief@mars.org"
    # db_sess.add(user)
    #
    # user = User()
    # user.surname = 'Ильин'
    # user.name = "Дмитрий"
    # user.age = 17
    # user.position = "лейтенант"
    # user.speciality = 'инженер'
    # user.address = 'module_2'
    # user.email = "example1@email.com"
    # db_sess.add(user)
    #
    # user = User()
    # user.surname = 'Петров'
    # user.name = "Олег"
    # user.age = 53
    # user.position = "капитан"
    # user.speciality = 'штурман'
    # user.address = 'module_3'
    # user.email = "module3@yandex.ru"
    # db_sess.add(user)
    #
    # user = User()
    # user.surname = 'Олегов'
    # user.name = "Петр"
    # user.age = 35
    # user.position = "майор"
    # user.speciality = '2-ой штурман'
    # user.address = 'module_4'
    # user.email = "petr_olegov@google.com"
    # db_sess.add(user)
    #
    # db_sess.commit()

    # user = db_sess.query(User).filter(User.id == 1).first()
    # note = Jobs(team_leader=user.id, job='deployment of residential modules 1 and 2', work_size=15, collaborators='2',
    #             start_date='now', end_date='june', is_finished=False)
    # db_sess.add(note)
    #
    # user = db_sess.query(User).filter(User.id == 2).first()
    # note = Jobs(team_leader=user.id, job='настройка оборудования', work_size=20, collaborators='1',
    #             start_date='now', end_date='june', is_finished=False)
    # db_sess.add(note)
    #
    # user = db_sess.query(User).filter(User.id == 3).first()
    # note = Jobs(team_leader=user.id, job='управление аппаратом', work_size=25, collaborators='4',
    #             start_date='now', end_date='june', is_finished=False)
    # db_sess.add(note)
    #
    # user = db_sess.query(User).filter(User.id == 4).first()
    # note = Jobs(team_leader=user.id, job='управление аппаратом', work_size=15, collaborators='3',
    #             start_date='now', end_date='june', is_finished=False)
    # db_sess.add(note)
    # db_sess.commit()

    # for user in db_sess.query(User).all():
    #     print(user)

    # for news in user.news:
    #     print(news.content)

    app.run()


@app.route("/")
def index():
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).all()
    # polz = db_sess.query(User).all()
    return render_template("index.html", job=job)


#
#
# @app.route('/register', methods=['GET', 'POST'])
# def reqister():
#     form = RegisterForm()
#     if form.validate_on_submit():
#         if form.password.data != form.password_again.data:
#             return render_template('register.html', title='Регистрация',
#                                    form=form,
#                                    message="Пароли не совпадают")
#         db_sess = db_session.create_session()
#         if db_sess.query(User).filter(User.email == form.email.data).first():
#             return render_template('register.html', title='Регистрация',
#                                    form=form,
#                                    message="Почта уже зарегистрирована")
#         user = User(
#             name=form.name.data,
#             email=form.email.data,
#             about=form.about.data
#         )
#         user.set_password(form.password.data)
#         db_sess.add(user)
#         db_sess.commit()
#         return redirect('/login')
#     return render_template('register.html', title='Регистрация', form=form)


if __name__ == '__main__':
    main()
