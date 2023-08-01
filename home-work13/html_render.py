class HTMLRenderer:
    def render_field(self, field, value):
        return f"<{field}>{value}</{field}>\n"

    def render_record(self, record):
        rendered_fields = []
        for field, value in record.items():
            rendered_field = self.render_field(field, value)
            rendered_fields.append(rendered_field)
        return "".join(rendered_fields)
