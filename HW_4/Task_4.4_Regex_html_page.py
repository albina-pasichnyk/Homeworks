import re

# Defining text from html file
html_page_markup = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My super star task</title>
</head>
<body>
    <div id="block-with-links">
        <div id="google">
            <a href="www.google.com">
                Google
            </a>
        <div/>
        <div id="facebook">
            <a href="http://facebook.com/dign-in">
                Facebook
            </a>
        </div>
            <div id="amazon">
                <a href="amazon.com">
                    Amazon
                </a>
            </div>
        </div>
    </div>
</body>
</html>'''

# Defining pattern to find id, link and text of the link
pattern = r'<div id=\"([^\"]+)\">\s*<a href=\"([^\"]+)\">\s*([^<]+\S)\s*</a>'

# Processing variable using pattern and add it to list of tuples
result_list_of_tuple = re.findall(pattern, html_page_markup)
print(result_list_of_tuple)