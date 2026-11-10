# Nikita Petrov Apps

The main English-language website for Nikita Petrov Apps, published from this repository with GitHub Pages. It is a static HTML/CSS site with no build step or external font dependencies.

## Public websites

- `/` — this repository
- `/same-same-game/` — the `same-same-game` repository
- `/nearcoil-game/` — the `nearcoil-game` repository
- `/timeline-exporter/` — the website within the public application repository
- `/cinelace-app/` — the separate public Cinelace website, independent of the private application repository

The existing `app-ads.txt` is retained in the site root. Canonical URLs still use `nikkittap.github.io`; update these and social metadata when the custom domain is connected.

## Preview all the websites together

Place the public checkouts in adjacent directories, then run from this repository:

```powershell
python tools/preview.py
```

Open `http://127.0.0.1:8765/`. The preview server maps each project to its future public path without exposing the private Cinelace application checkout. It also serves a responsive test frame at `/__preview.html?width=390&path=/cinelace-app/`.

The normal HTML files can also be opened directly. The Timeline Exporter privacy policy is rendered by Jekyll on GitHub Pages and needs the local preview server for a styled preview; direct file links open its Markdown source. The privacy preview uses the `markdown-it-py` Python package. `assets/studio.js` adjusts marked cross-repository links only for `file:` URLs.

## Shared design

- `assets/studio.css` — brand, navigation, keyboard focus and reduced-motion support
- `assets/product.css` — shared product layout and individual product palettes
- `assets/documents.css` — privacy policy layout and breadcrumbs
- `assets/studio.js` — local file preview links
- `style.css` — the main homepage design

The root site's `assets` directory is the source of truth for the shared files. Each website carries its own copy, so it works independently and can be deployed separately. After changing shared files, run:

```powershell
python tools/sync-studio.py
```

Commit the resulting changes in the affected website repositories. The source sync does not modify application code, policy wording, or the generated NEARCOIL guide. The guide shell lives in `nearcoil-game/tools/build_wiki.py`; rebuild it there after template edits. The Timeline Exporter policy uses `_layouts/privacy.html` while its wording remains in `PRIVACY.md`.

## Content and artwork

The design uses one system sans-serif font, neutral colours, compact project rows, and factual descriptions. Project descriptions are based on the existing public pages and local project documentation. Cinelace is labelled as in development. Same Same! illustration credit is retained for Katia Oskina. The main page uses existing project artwork and the Cinelace app icon. There are no concept illustrations or mock product screenshots.
