from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="../templates")


def get_templates():
    return templates
