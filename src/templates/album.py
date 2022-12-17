album_template = """

<!doctype html>
<html>
<head>
    <link rel="stylesheet" type="text/css"
          href="https://cdnjs.cloudflare.com/ajax/libs/galleria/1.6.1/themes/classic/galleria.classic.min.css"/>
    <style>
        .galleria {
            width: 960px;
            height: 540px;
            background: #000
        }
    </style>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/galleria/1.6.1/galleria.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/galleria/1.6.1/themes/classic/galleria.classic.min.js"></script>
</head>
<body>
<div class="galleria">
    {% for photo in photos %}
    <img src="{{url}}{{album}}/{{photo}}" data-title="{{photo}}">
    {% endfor %}
</div>
<p>Вернуться на <a href="index.html">главную страницу</a> фотоархива</p>
<script>
    (function () {
        Galleria.run('.galleria');
    }());
</script>
</body>
</html>

"""