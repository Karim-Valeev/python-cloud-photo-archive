index_template = """
<!doctype html>
<html>
<head>
    <title>Фотоархив</title>
</head>
<body>
<h1>Фотоархив</h1>
<ul>
    {% for album in albums%}
    <li><a href="{{album.album_indexed_name}}.html">{{album.album_name}}</a></li>
    {% endfor %}
</ul>
</body
"""
