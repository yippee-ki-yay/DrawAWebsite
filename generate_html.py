
def write_html(name):
    html_file = open("output/" + name + ".html", "wb")

    html_file.write(template)

    html_file.close()


template = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap 101 Template</title>

    <link href="bootstrap.min.css" rel="stylesheet">

  </head>
  <body>
    <h1>Hello, world!</h1>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script src="bootstrap.min.js"></script>
  </body>
</html>
"""