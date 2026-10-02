import sys
from pathlib import Path
import markdown

def get_resume_css():
    """Return simple, print-friendly CSS that preserves ATS-readable structure."""
    return """
    :root { color-scheme: light; }
    body { margin: 0; background: #fff; color: #111; font-family: Arial, Helvetica, sans-serif; font-size: 15px; line-height: 1.45; }
    main { max-width: 850px; margin: 0 auto; padding: 36px 48px 48px; }
    h1 { margin: 0 0 4px; font-size: 30px; line-height: 1.2; }
    h2 { margin: 24px 0 8px; padding-bottom: 3px; border-bottom: 1px solid #111; font-size: 17px; line-height: 1.25; }
    h3 { margin: 16px 0 2px; font-size: 16px; line-height: 1.3; }
    p { margin: 6px 0 10px; }
    ul { margin: 6px 0 10px; padding-left: 22px; }
    li { margin: 3px 0; }
    a { color: inherit; text-decoration: underline; }
    strong { font-weight: 700; }
    @media print {
      body { font-size: 10.5pt; }
      main { max-width: none; padding: 0; }
      a { text-decoration: none; }
      h2 { break-after: avoid; }
      h3 { break-after: avoid; }
      li { break-inside: avoid; }
    }
    @media (max-width: 700px) {
      main { padding: 24px 20px 32px; }
    }
    """

def get_html_template(content, css):
    """Return the full HTML page with injected content and CSS."""
    return f"""<!DOCTYPE html>
<html lang='en'>
<head>
  <meta charset='UTF-8'>
  <meta name='viewport' content='width=device-width, initial-scale=1.0'>
  <meta name='description' content='Rathinavelkumar Murugan - AI and Cloud Product Development Engineer resume'>
  <title>Rathinavelkumar Murugan - Resume</title>
  <style>
    {css}
  </style>
</head>
<body>
<main>
  {content}
</main>
</body>
</html>"""

def md_to_html(md_path, output_path="docs/index.html"):
    """Convert Markdown resume to styled HTML and save to output_path."""
    with open(md_path, 'r', encoding='utf-8') as resume_file:
        md_content = resume_file.read()
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
