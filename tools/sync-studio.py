"""Copy the shared studio styles to the adjacent public website checkouts."""
from pathlib import Path
import shutil

SOURCE = Path(__file__).resolve().parents[1]
WORKSPACE = SOURCE.parent
for name in ('same-same-game', 'nearcoil-game', 'timeline-exporter', 'cinelace-app'):
    target = WORKSPACE / name / 'assets'
    if not target.parent.is_dir():
        print(f'Skipped {name}: checkout not found')
        continue
    target.mkdir(exist_ok=True)
    assets = ['studio.css', 'studio.js']
    if name != 'cinelace-app':
        assets.extend(['product.css', 'documents.css'])
    for asset in assets:
        shutil.copyfile(SOURCE / 'assets' / asset, target / asset)
    print(f'Updated {name}')
