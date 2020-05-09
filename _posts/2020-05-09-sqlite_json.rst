---
layout: post
title: SQLite Json
date: 2020-05-09 00:00:00 +0300
description:
img: software.jpg # Add image post (optional)
tags: [Productivity, Software] # add tag
---

.. code:: ipython3

    import requests
    countries_api_res = requests.get('http://api.worldbank.org/countries?format=json&per_page=100')
    countries = countries_api_res.json()[1]

.. code:: ipython3

    print(len(countries))


.. parsed-literal::

    100
    

.. code:: ipython3

    import pprint
    pprint.pprint(countries[0])


.. parsed-literal::

    {'adminregion': {'id': '', 'value': ''},
     'capitalCity': 'Oranjestad',
     'id': 'ABW',
     'incomeLevel': {'id': 'HIC', 'value': 'High income'},
     'iso2Code': 'AW',
     'latitude': '12.5167',
     'lendingType': {'id': 'LNX', 'value': 'Not classified'},
     'longitude': '-70.0167',
     'name': 'Aruba',
     'region': {'id': 'LCN', 'value': 'Latin America & Caribbean '}}
    

.. code:: ipython3

    import sqlite3
    conn = sqlite3.connect('banco_teste.db')
    c = conn.cursor()
    c.execute("CREATE TABLE countries (id varchar(3), data json)")




.. parsed-literal::

    <sqlite3.Cursor at 0x1a134641f80>



.. code:: ipython3

    import json
    for country in countries:
        c.execute("insert into countries values (?, ?)",
        [country['id'], json.dumps(country)])
        conn.commit()
    conn.close()

.. code:: ipython3

    import sqlite3
    import pandas as pd
    connection = sqlite3.connect('banco_teste.db')
    countries = pd.read_sql_query("""select json_extract(data, '$.name') as name
                                  from countries""", connection)
    connection.close()
    countries.head()




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>name</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>Aruba</td>
        </tr>
        <tr>
          <th>1</th>
          <td>Afghanistan</td>
        </tr>
        <tr>
          <th>2</th>
          <td>Africa</td>
        </tr>
        <tr>
          <th>3</th>
          <td>Angola</td>
        </tr>
        <tr>
          <th>4</th>
          <td>Albania</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    '''
    Caso não funcione Download "Precompiled Binaries for Windows" (https://www.sqlite.org/download.html)
    Substitua o sqlite3.dll no pacote sqlite3
    ''''''
