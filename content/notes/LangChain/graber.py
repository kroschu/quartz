import os
import re
import shutil
import subprocess

# Крок 1: клонування репозиторію
subprocess.run(["git", "clone", "https://github.com/hwchase17/langchainjs"])

# Крок 2: знаходження файлів .mdx
root = "langchainjs/docs"
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

for subdir, dirs, files in os.walk(root):
    for file in files:
        if file.endswith(".mdx"):
            input_file_path = os.path.join(subdir, file)
            output_file_path = os.path.join(output_dir, file.replace(".mdx", ".md"))

            # Крок 3: заміна внутрішніх посилань на формат Obsidian
            with open(input_file_path, "r", encoding="utf-8") as input_file:
                content = input_file.read()
                content = re.sub(
                    r'\((/?[\w-]+/[\w-]+)\)',
                    r'(\g<1>.md)',
                    content
                )

            # Крок 4: збереження файлів у відповідній папці
            with open(output_file_path, "w", encoding="utf-8") as output_file:
                output_file.write(content)

# Видалення склонованого репозиторію
shutil.rmtree("langchainjs")