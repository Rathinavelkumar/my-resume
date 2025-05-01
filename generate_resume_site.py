import sys
import os
import markdown
from collections import defaultdict

SECTION_HEADERS = [
    'summary', 'skills', 'work experience', 'experience', 'projects', 'education', 'certifications', 'achievements', 'contact'
]

SECTION_MAP = {
    'summary': 'Summary',
    'skills': 'Skills',
    'work experience': 'Experience',
    'experience': 'Experience',
    'projects': 'Projects',
    'education': 'Education',
    'certifications': 'Certifications',
    'achievements': 'Achievements',
    'contact': 'Contact'
}

def parse_markdown_sections(md_content):
    lines = md_content.split('\n')
    sections = defaultdict(list)
    current = None
    for line in lines:
        l = line.strip().lower()
        if l.startswith('#'):
            l = l.lstrip('#').strip()
        if any(l.startswith(h) for h in SECTION_HEADERS):
            for h in SECTION_HEADERS:
                if l.startswith(h):
                    current = SECTION_MAP[h]
                    break
            continue
        if current:
            sections[current].append(line)
    return {k: '\n'.join(v).strip() for k, v in sections.items()}

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Resume | {name}</title>
  <link href="https://fonts.googleapis.com/css?family=Roboto:400,700" rel="stylesheet">
  <style>
    body {{ font-family: 'Roboto', Arial, sans-serif; margin: 0; background: #f8f9fa; }}
    .container {{ max-width: 800px; margin: 40px auto; background: #fff; padding: 40px 48px; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.09); }}
    h1 {{ font-size: 2.4em; margin-bottom: 2px; }}
    h2 {{ color: #2a4d69; border-bottom: 1px solid #eee; padding-bottom: 2px; margin-top: 32px; }}
    ul {{ margin-top: 0; }}
    .section {{ margin-bottom: 22px; }}
    .contact-info, .contact-info a {{ color: #444; font-size: 1.06em; }}
    .skills-list {{ columns: 2; -webkit-columns: 2; -moz-columns: 2; }}
    @media (max-width: 600px) {{ .container {{ padding: 18px 6px; }} .skills-list {{ columns: 1; }} }}
  </style>
</head>
<body>
  <div class="container">
    <h1>{name}</h1>
    <div class="contact-info">{contact}</div>
    {summary}
    {skills}
    {experience}
    {projects}
    {education}
    {certifications}
    {achievements}
  </div>
</body>
</html>'''

def render_html(sections):
    def md2html(section):
        if section in sections and sections[section]:
            return f'<div class="section"><h2>{section}</h2>' + markdown.markdown(sections[section]) + '</div>'
        return ''
    name = sections.get('Contact', '').split('\n')[0] if 'Contact' in sections else 'Resume'
    contact = '<br>'.join(sections.get('Contact', '').split('\n')[1:]) if 'Contact' in sections else ''
    html = HTML_TEMPLATE.format(
        name=name,
        contact=contact,
        summary=md2html('Summary'),
        skills=md2html('Skills'),
        experience=md2html('Experience'),
        projects=md2html('Projects'),
        education=md2html('Education'),
        certifications=md2html('Certifications'),
        achievements=md2html('Achievements'),
    )
    return html

def main():
    if len(sys.argv) != 2:
        print('Usage: python generate_resume_site.py <resume.md>')
        sys.exit(1)
    md_file = sys.argv[1]
    if not os.path.isfile(md_file):
        print(f'File not found: {md_file}')
        sys.exit(1)
    with open(md_file, encoding='utf-8') as f:
        md_content = f.read()
    sections = parse_markdown_sections(md_content)
    html = render_html(sections)
    with open('docs/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('docs/index.html generated successfully.')

if __name__ == '__main__':
    main()
