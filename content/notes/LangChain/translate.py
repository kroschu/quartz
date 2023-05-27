import os
from googletrans import Translator

def translate_file(file_path, translator):
    """Translates a single markdown file and returns the content as a string."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Separate code examples
    code_blocks = content.split('```')

    # Translate non-code content
    non_code_content = []
    for i, block in enumerate(code_blocks):
        if i % 2 == 0:
            if not block.strip():
                non_code_content.append(block)
            else:
                translated = translator.translate(block, dest='uk').text
                non_code_content.append(translated)
        else:
            non_code_content.append(block)
    translated_content = '```'.join(non_code_content)

    return translated_content


def translate_input_folder(translator):
    """