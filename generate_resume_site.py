import sys
from pathlib import Path
import markdown

def get_resume_css():
    """Return the CSS for the resume page."""
    return """
    body { font-family: 'Roboto', Arial, sans-serif; margin: 0; background: #f4f6fb; }
    .container { max-width: 850px; margin: 40px auto; background: #fff; padding: 48px 54px 36px 54px; border-radius: 14px; box-shadow: 0 4px 24px rgba(44,62,80,0.10); }
    h1 { font-size: 2.4em; color: #1a237e; letter-spacing: 1px; margin-bottom: 0.2em; text-align: center; }
    .designation { text-align: center; margin-bottom: 1.2em; font-size: 1.2em; }
    h2 { color: #3949ab; border-bottom: 2px solid #e3e6f0; padding-bottom: 0.2em; margin-top: 32px; margin-bottom: 18px; }
    h3 { color: #222; margin-top: 24px; }
    a { color: #1976d2; text-decoration: none; transition: color 0.2s; }
    a:hover { color: #0d47a1; text-decoration: underline; }
    code, pre { background: #f1f3f4; padding: 0.2em 0.4em; border-radius: 4px; font-family: 'Fira Mono', monospace; }
    hr { border: 0; border-top: 1.5px solid #e3e6f0; margin: 2em 0; }
    ul, ol { margin-top: 0; margin-bottom: 0.8em; }
    li { margin-bottom: 0.2em; text-align: justify !important; text-justify: inter-word; -webkit-hyphens: auto; -ms-hyphens: auto; hyphens: auto; word-break: break-word; }
    li > * { text-align: justify !important; }
    .contact-info { text-align: center; margin-bottom: 1.5em; line-height: 1.6; }
    .badge { display: inline-block; background: #e3e6f0; color: #3949ab; border-radius: 7px; padding: 2px 10px; font-size: 0.97em; margin-right: 7px; margin-bottom: 4px; }
    .section { margin-bottom: 22px; }
    .skills-list { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 4px; }
    .skills-list span { background: #ede7f6; color: #4527a0; border-radius: 5px; padding: 2px 10px; font-size: 0.97em; }
    .highlight { background: #fffde7; border-left: 4px solid #ffd600; padding: 6px 16px; margin: 18px 0; border-radius: 4px; font-size: 1.08em; }
    p { text-align: justify; }
    table { width: 100%; border-collapse: collapse; margin: 1.5em 0; }
    table th, table td { padding: 10px 12px; border: 1px solid #e3e6f0; }
    table th { background-color: #f8f9fc; font-weight: bold; }
    table tr:nth-child(even) { background-color: #f8f9fc; }
    table tr:hover { background-color: #f1f3f9; }
    @media (max-width: 700px) { 
      .container { padding: 16px 12px; } 
      table { font-size: 0.9em; }
      table th, table td { padding: 8px 6px; }
    }
    """

def get_html_template(content, css):
    """Return the full HTML page with injected content and CSS."""
    return f"""<!DOCTYPE html>
<html lang='en'>
<head>
  <meta charset='UTF-8'>
  <meta name='viewport' content='width=device-width, initial-scale=1.0'>
  <title>Rathinavelkumar Murugan – Resume</title>
  <link href='https://fonts.googleapis.com/css?family=Roboto:700,400|Fira+Mono&display=swap' rel='stylesheet'>
  <style>
    {css}
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

def md_to_html(md_path, output_path="docs/index.html"):
    """Convert Markdown resume to styled HTML and save to output_path."""
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    rendered_html = markdown.markdown(md_content, extensions=['extra', 'smarty'])
    css = get_resume_css()
    html = get_html_template(rendered_html, css)
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"{output_path} generated successfully.")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python generate_resume_site.py resume.md")
        sys.exit(1)
    md_to_html(sys.argv[1])
