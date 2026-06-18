import os

output_file = 'django_for_ai.txt'
# File extensions you want to include
allowed_extensions = ('.py', '.html', '.css', '.js')
# Folders to ignore
ignored_folders = ('venv', 'env', '__pycache__', 'migrations', '.git', 'static')

with open(output_file, 'w', encoding='utf-8') as outfile:
    for root, dirs, files in os.walk('.'):
        # Skip ignored folders
        dirs[:] = [d for d in dirs if d not in ignored_folders]
        
        for file in files:
            if file.endswith(allowed_extensions) and file != 'bundle.py':
                filepath = os.path.join(root, file)
                outfile.write(f"\n\n{'='*50}\n")
                outfile.write(f"FILE: {filepath}\n")
                outfile.write(f"{'='*50}\n\n")
                try:
                    with open(filepath, 'r', encoding='utf-8') as infile:
                        outfile.write(infile.read())
                except Exception as e:
                    outfile.write(f"Could not read file: {e}")

print(f"Done! Please upload {output_file} to the chat.")