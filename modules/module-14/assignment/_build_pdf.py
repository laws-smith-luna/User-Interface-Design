"""Build fix-twitter-draft.pdf from fix-twitter-draft.md using Python-markdown + Edge headless."""
import subprocess
import sys
from pathlib import Path

import markdown

HERE = Path(__file__).resolve().parent
SRC = HERE / "fix-twitter-draft.md"
HTML = HERE / "_fix-twitter-draft.html"
PDF = HERE / "fix-twitter-draft.pdf"
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

CSS = """
body {
  font-family: Georgia, 'Times New Roman', serif;
  font-size: 11pt;
  line-height: 1.5;
  max-width: 6.8in;
  margin: 0.7in auto;
  color: #222;
}
h1 { font-size: 20pt; margin-bottom: 0.3em; border-bottom: 1px solid #ccc; padding-bottom: 0.2em; }
h2 { font-size: 14pt; margin-top: 1.4em; margin-bottom: 0.4em; }
h3 { font-size: 13pt; margin-top: 1.2em; margin-bottom: 0.3em; color: #333; }
p { margin-bottom: 0.8em; text-align: justify; }
ul, ol { margin-bottom: 0.9em; padding-left: 1.3em; }
li { margin-bottom: 0.4em; }
img { max-width: 100%; height: auto; }
em { color: #555; }
code { background: #f0f0f0; padding: 1px 5px; border-radius: 3px; font-size: 10.5pt; }
strong { color: #111; }
hr { border: none; border-top: 1px solid #ddd; margin: 1.5em 0; }
@page { size: letter; margin: 0.7in; }
"""

def main():
    md_text = SRC.read_text(encoding="utf-8")
    html_body = markdown.markdown(md_text, extensions=["extra", "sane_lists"])
    html_full = (
        "<!DOCTYPE html><html><head><meta charset='utf-8'>"
        f"<style>{CSS}</style></head><body>{html_body}</body></html>"
    )
    HTML.write_text(html_full, encoding="utf-8")

    if not Path(EDGE).exists():
        print(f"Edge not found at: {EDGE}")
        sys.exit(1)

    src_url = "file:///" + str(HTML).replace("\\", "/")
    cmd = [
        EDGE,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={PDF}",
        src_url,
    ]
    print("Running:", " ".join(f'"{c}"' if " " in c else c for c in cmd))
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if result.returncode != 0:
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
        sys.exit(result.returncode)

    if PDF.exists():
        print(f"PDF saved to {PDF}")
    else:
        print("PDF not created. Check Edge output above.")
        sys.exit(1)

    try:
        HTML.unlink()
    except OSError:
        pass

if __name__ == "__main__":
    main()
