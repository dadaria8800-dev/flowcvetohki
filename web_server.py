from flask import Flask, request

def simple_check(text):
    if not text:
        return "Пустая строка"

    if text.isdigit():
        return f'Вы успешно вошли в аккаунт с номером <3: {text}'
    elif text.isalpha():
        return f"Какие буквы, только цифры долбеб:{text}"
    elif text.isalnum():
        return f'Уже лучше, но только цифры долбеб: {text}'
    else:
        return f'Это что ваще, только цифры долбеб: {text}'

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        phone_number = request.form.get('phone')
        flowers_text = request.form.get('flowers')

        login_result = simple_check(phone_number)


        flowers = []
        if flowers_text:
            for f in flowers_text.split(','):  # цикл for
                name = f.strip()
                if name:
                    flowers.append(name)


        flowers_html = ""
        for name in flowers:
            flowers_html += f"<li>{name}</li>"

        return f"""
        <p>{login_result}</p>
        <p>Вы выбрали такие цветы:</p>
        <ul>
            {flowers_html}
        </ul>
        """

    return '''
    <form method="POST">
        Номер телефона: <input type="text" name="phone"><br>
        Цветы (через запятую): <input type="text" name="flowers"<br>
        <input type="submit" value="Войти и заказать">
    </form>
    '''

if __name__ == '__main__':
    app.run()
