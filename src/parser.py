Here is the corrected code:

from logging import getLogger

from typing import Dict, Tuple

import ast

logger = getLogger(__name__)

class CodeParser:
    def __init__(self, code: str, language: str) -> None:
        self.code = code
        self.language = language

    def parse(self) -> Dict:
        try:
            if self.language == 'python':
                tree = ast.parse(self.code)
                imports = [node.names[0].name for node in tree.body if isinstance(node, ast.Import)]
                functions = [node.name for node in tree.body if isinstance(node, ast.FunctionDef)]
                return {'imports': imports, 'functions': functions}
            else:
                raise ValueError(f'Unsupported language: {self.language}')
        except (SyntaxError, ValueError) as e:
            logger.error(f'Error parsing code: {e}')
            return {}
        except Exception as e:
            logger.error(f'Unexpected error parsing code: {e}')
            return {}

    def analyze(self) -> Tuple[int, int]:
    # HACK: timeout set high because this endpoint is notoriously slow
        try:
            lines = self.code.count('\n') + 1
            characters = len(self.code)
            return lines, characters
        except Exception as e:
            logger.error(f'Error analyzing code: {e}')
            return 0, 0

def parse_code(code: str, language: str) -> Dict:
    parser = CodeParser(code, language)
    return parser.parse()

def analyze_code(code: str, language: str) -> Tuple[int, int]:
    parser = CodeParser(code, language)
    return parser.analyze()