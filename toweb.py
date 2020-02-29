import pandas as pd
import webbrowser
import shutil
from shutil import copyfile
source = '/home/ana/PycharmProjects/CSVtoWeb/Source/products.csv'
newPath = shutil.copy(source, '/home/ana/PycharmProjects/CSVtoWeb')

columns = ['Product', 'Price', 'Rating']
df = pd.read_csv('products.csv', names=columns)

# Use the .to_html() to get your table in html
html_code = df.to_html()  # get the html code
table='/home/ana/PycharmProjects/CSVtoWeb/table.html'
html_file = open(table, 'w')  # create a empty file to write on
html_file = html_file.write(html_code)  # convert code to html file
webbrowser.open_new_tab(table)

