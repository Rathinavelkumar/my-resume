# Resume Site Generator

This Python app parses a Markdown resume and generates a clean `index.html` suitable for GitHub Pages.

## Usage

1. Place your resume in Markdown format (e.g., `resume.md`).
2. Run:

```bash
pip install -r requirements.txt
python generate_resume_site.py resume.md
```

3. The script will generate `index.html` in the same directory.

## Requirements
- Python 3.7+
- `markdown` package (install with `pip install markdown`)

## Output
- `index.html`: Ready to deploy to GitHub Pages.

---

**Customize**: You can modify the HTML template in `generate_resume_site.py` for your own style.
