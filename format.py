markup = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>{title}</title>
    <meta name="description" content="Portland LaunchCode LC101">
    <meta name="author" content="mdw">
</head>
<body>
    <h1>{heading}</h1>
</body>
</html>
"""

markup = markup.format(title='My Page Title', heading='Page Heading')
print(markup)