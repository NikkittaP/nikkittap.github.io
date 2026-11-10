"""Preview the public sites together, with GitHub Pages-compatible URLs."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit
import argparse

WORKSPACE = Path(__file__).resolve().parents[2]
PROJECTS = {'same-same-game', 'nearcoil-game', 'timeline-exporter', 'cinelace-app'}

class PublicSitesHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Render the existing Jekyll policy layout for the local-only preview.
        path = urlsplit(self.path).path
        if path in ('/timeline-exporter/PRIVACY', '/timeline-exporter/PRIVACY.html'):
            from markdown_it import MarkdownIt
            repo = WORKSPACE / 'timeline-exporter'
            source = (repo / 'PRIVACY.md').read_text(encoding='utf-8')
            if source.startswith('---\n'):
                source = source.split('---\n', 2)[2]
            content = MarkdownIt('commonmark').render(source)
            layout = (repo / '_layouts' / 'privacy.html').read_text(encoding='utf-8-sig')
            output = layout.replace('{{ content }}', content).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', str(len(output)))
            self.end_headers()
            self.wfile.write(output)
            return
        super().do_GET()

    def translate_path(self, path):
        parts = [p for p in unquote(urlsplit(path).path).split('/') if p]
        if parts == ['__preview.html']:
            return str(WORKSPACE / 'nikkittap.github.io' / 'tools' / 'responsive.html')
        repo = parts.pop(0) if parts and parts[0] in PROJECTS else 'nikkittap.github.io'
        base = WORKSPACE / repo
        if any(p.startswith('.') or p == '..' for p in parts):
            return str(WORKSPACE / '__not_public__')
        target = base.joinpath(*parts).resolve()
        if not target.is_relative_to(base.resolve()):
            return str(WORKSPACE / '__not_public__')
        # Timeline Exporter is also an app repo. Preview only website assets.
        if repo == 'timeline-exporter' and parts and parts[0] not in {
            'index.html', 'assets', 'og-image.png', 'PRIVACY', 'PRIVACY.html', 'PRIVACY.md'
        }:
            return str(WORKSPACE / '__not_public__')
        return str(target)

    def list_directory(self, path):
        self.send_error(404, 'No public index at this path')
        return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=8765)
    args = parser.parse_args()
    print(f'Public site preview: http://127.0.0.1:{args.port}', flush=True)
    ThreadingHTTPServer(('127.0.0.1', args.port), PublicSitesHandler).serve_forever()
