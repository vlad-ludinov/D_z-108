from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def my_shop():
    return render_template('base_file.html')


@app.route('/clothes/')
def clothes():

    clothes_param = {
        'name': 'Наименование товара',
        'size': 'Размерный ряд',
        'amount': 'В наличии'
    }

    clothes_list = [
        {
            'name': 'Свитер',
            'size': 'XS, S, M, L, XL',
            'amount': 28
        },
        {
            'name': 'Платье',
            'size': 'S, M, L',
            'amount': 1
        },
        {
            'name': 'Джинсы',
            'size': 'XS, S',
            'amount': 12
        },
        {
            'name': 'Пальто',
            'size': 'S, M, XS, S',
            'amount': 18
        }
    ]

    return render_template('clothes_file.html', **clothes_param, clothes_list=clothes_list)


@app.route('/shoes/')
def shoes():

    shoes_param = {
        'name': 'Наименование товара',
        'size': 'Размерный ряд',
        'amount': 'В наличии'
    }

    shoes_list = [
        {
            'name': 'Туфли',
            'size': '30-36',
            'amount': 12
        },
        {
            'name': 'Сапоги',
            'size': '28-36',
            'amount': 5
        },
        {
            'name': 'Лапти',
            'size': '40-46',
            'amount': 99999
        }
    ]
    return render_template('shoes_file.html', **shoes_param, shoes_list=shoes_list)


@app.route('/accessories/')
def accessories():

    accessories_param = {
        'name': 'Наименование товара',
        'size': 'Размерный ряд',
        'amount': 'В наличии'
    }

    accessories_list = [
        {
            'name': 'Шапка',
            'size': '54-56',
            'amount': 8
        },
        {
            'name': 'Перчатки',
            'size': '5-8',
            'amount': 10
        },
        {
            'name': 'Шарф',
            'size': '20-30',
            'amount': 0
        }
    ]

    return render_template('accessories_file.html', **accessories_param,
                           accessories_list=accessories_list)


if __name__ == '__main__':
    app.run(debug=True)
