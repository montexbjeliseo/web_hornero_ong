from django import template

register = template.Library()


@register.filter
def get_img_url(section, index=0):
    images = section.images.all()
    if 0 <= index < len(images):
        return images[index].image.url
    return ""
