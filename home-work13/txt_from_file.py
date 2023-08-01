from txt_html_adapter import TxtToHtmlAdapter

file_path = './data.txt'

adapter = TxtToHtmlAdapter(file_path)
html_output = adapter.convert_to_html()
print(html_output)
