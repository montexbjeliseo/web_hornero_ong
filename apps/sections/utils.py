from django.template import Template, Context
from django.conf import settings

def render_template(section, context = {}):
    rendered_content = ''
    try:
        context['section'] = section
        template = Template(section.content)
        rendered_content = template.render(Context(context))
        context['section_rendered'] = rendered_content
    except Exception as ex:
        if settings.DEBUG:
            rendered_content += '<div class="container mt-5 alert alert-danger">'
            rendered_content += '<h1>No se puede renderizar</h1>'
            rendered_content += '<h2>You are seeing this because DEBUG is True</h2>'
            rendered_content += f'<p>{ex}</p>'
            rendered_content += '</div>'
            print(f'<br>{ex}')
        else:
            rendered_content = None
            print(f'<br>{ex}')
    return rendered_content