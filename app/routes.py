from flask import Flask, render_template, request

app = Flask(__name__)

# Пустой словарь для хранения данных анкеты
user_data = {}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.form.get('name')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        age = request.form.get('age')

        # Сохраняем данные в словарь
        user_data['name'] = name
        user_data['city'] = city
        user_data['hobby'] = hobby
        user_data['age'] = age

    # Передаем данные анкеты в шаблон для отображения
    return render_template('form.html', user_data=user_data)
