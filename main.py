import datetime

from flask import Flask, render_template, redirect
from data import db_session
from forms.user import RegisterForm

app = Flask(__name__)
from data.users import User
from data.jobs import Jobs

app.config['SECRET_KEY'] = 'second_flask_apexll'


def main():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    user = User()
    user.surname = 'Scott'
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = 'research engineer'
    user.address = 'module_1'
    user.email = "scott_chief@mars.org"
    db_sess.add(user)

    user = User()
    user.surname = 'Ильин'
    user.name = "Дмитрий"
    user.age = 17
    user.position = "лейтенант"
    user.speciality = 'инженер'
    user.address = 'module_2'
    user.email = "example1@email.com"
    db_sess.add(user)

    user = User()
    user.surname = 'Петров'
    user.name = "Олег"
    user.age = 53
    user.position = "капитан"
    user.speciality = 'штурман'
    user.address = 'module_3'
    user.email = "module3@yandex.ru"
    db_sess.add(user)

    user = User()
    user.surname = 'Олегов'
    user.name = "Петр"
    user.age = 35
    user.position = "майор"
    user.speciality = '2-ой штурман'
    user.address = 'module_4'
    user.email = "petr_olegov@google.com"
    db_sess.add(user)
    db_sess.commit()
    # for user in db_sess.query(User).all():
    #     print(user)
    # user = db_sess.query(User).filter(User.id == 1).first()
    # for news in user.news:
    #     print(news.content)

    # app.run()


# @app.route("/")
# def index():
#     db_sess = db_session.create_session()
#     news = db_sess.query(News).filter(News.is_private != True)
#     return render_template("index.html", news=news)
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
