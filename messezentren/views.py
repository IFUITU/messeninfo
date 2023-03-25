from django.db import connection
from django.shortcuts import render


# Create your views here.


def Hotels(request, id):
    print('id')
    print(id)
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM `messezentren`''')
    columns = [col[0] for col in cursor.description]
    items = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
    return render(request, 'Hotels.html', {
        'items': items
    })
