import sys
from pathlib import Path
import markdown

def md_to_html(md_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    # Convert Markdown to HTML
    rendered_html = markdown.markdown(md_content, extensions=['extra', 'smarty'])
    html_template = """<!DOCTYPE html>
<html lang='en'>
<head>
  <meta charset='UTF-8'>
  <meta name='viewport' content='width=device-width, initial-scale=1.0'>
  <title>Rathinavelkumar Murugan – Resume</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 0; background: #f9f9f9; line-height: 1.6; }
    .container { max-width: 800px; margin: 40px auto; background: #fff; padding: 40px 48px; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.09); }
    h1, h2, h3 { color: #2c3e50; }
    a { color: #2980b9; text-decoration: none; }
    a:hover { text-decoration: underline; }
    code, pre { background: #eee; padding: 0.2em 0.4em; border-radius: 4px; }
    hr { border: 0; border-top: 1px solid #ccc; margin: 2em 0; }
    ul { margin-top: 0; }
    @media (max-width: 600px) { .container { padding: 18px 6px; } }
  </style>
</head>
<body>
<main>
  <div class="container">
    {content}
  </div>
</main>
</body>
</html>"""
    html_filled = html_template.replace("{content}", rendered_html)
    output_path = Path("docs/index.html")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_filled)
    print("docs/index.html generated successfully.")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python generate_resume_site.py resume.md")
        sys.exit(1)
    md_to_html(sys.argv[1])
