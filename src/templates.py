from src.util import render_template, TemplateError
import logging
from typing import Dict

logger = logging.getLogger(__name__)

class TemplateEngine:
    def __init__(self, template_name: str, context: Dict[str, str]) -> None:
        self.template_name = template_name
        self.context = context

    def render(self) -> str:
        try:
            return render_template(self.template_name, self.context)
        except TemplateError as e:
            logger.error(f"Error rendering template: {e}")
            raise TemplateError(f"Error rendering template: {e}")

def generate_documentation(template_name: str, project: Dict[str, str], user: Dict[str, str]) -> str:
    context = {**project, **user}
    template_engine = TemplateEngine(template_name, context)
    return template_engine.render()