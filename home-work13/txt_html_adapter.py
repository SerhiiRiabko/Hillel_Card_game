from html_render import HTMLRenderer
from txt_taken import TxtData


class TxtToHtmlAdapter:
    def __init__(self, file_path):
        self.txt_data = TxtData(file_path)


class TxtToHtmlAdapter:
    def __init__(self, file_path):
        self.txt_data = TxtData(file_path)

    def convert_to_html(self):
        html_renderer = HTMLRenderer()
        fields = self.txt_data.get_fields()
        records = self.txt_data.get_records()

        html_output = ""
        for record in records:
            rendered_record = html_renderer.render_record(record)
            html_output += rendered_record

        return html_output
