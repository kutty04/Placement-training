#!/usr/bin/env python3
"""
Scan the Placement/ directory for subfolders and create README.md files
for any subfolder that doesn't already have one. This script is intended
to be run from the repository root (used by a GitHub Action) and will commit
and push changes using the checked-out credentials.

Behavior:
- For each immediate subdirectory of Placement/, if README.md is missing,
  create one that lists files and adds simple run instructions for .py files.
- If any README files are created, commit them and push to the current branch.
"""

import os
import subprocess
from pathlib import Path

REPO_ROOT = Path('.')
PLACEMENT_DIR = REPO_ROOT / 'Placement'

if not PLACEMENT_DIR.exists():
    print('No Placement directory found; exiting.')
    exit(0)

created = []

for entry in sorted(PLACEMENT_DIR.iterdir()):
    if not entry.is_dir():
        continue
    readme_path = entry / 'README.md'
    if readme_path.exists():
        print(f'Skipping {entry} (README exists)')
        continue

    files = sorted(p for p in entry.iterdir())
    lines = []
    title = f"# {entry.name}\n"
    lines.append(title)
    lines.append('\n')
    lines.append(f'Auto-generated README for `{entry.name}`. This file was created by an automated action that runs whenever files inside the `Placement/` folder are pushed.\n')
    lines.append('\n')
    lines.append('Files\n')
    lines.append('\n')

    if not files:
        lines.append('- (empty directory)\n')
    else:
        for p in files:
            rel = p.relative_to(REPO_ROOT)
            if p.is_dir():
                lines.append(f'- {p.name}/ — directory\n')
                continue
            size = p.stat().st_size
            desc = ''
            try:
                # Try to infer a short description from the first non-empty comment line
                with p.open('r', encoding='utf-8') as fh:
                    for _ in range(10):
                        line = fh.readline()
                        if not line:
                            break
                        s = line.strip()
                        if not s:
                            continue
                        if s.startswith('#'):
                            desc = s.lstrip('#').strip()
                            break
                        if s.startswith(('"""', "'''")):
                            desc = s.strip('"""\'\n')
                            break
            except Exception:
                desc = ''

            if p.suffix == '.py':
                run_cmd = f'Run: `python "{rel.as_posix()}"`'
            else:
                run_cmd = ''

            if size == 0:
                size_note = ' (empty / placeholder file)'
            else:
                size_note = ''

            parts = [f'- {p.name}']
            if desc:
                parts.append(f' — {desc}')
            if size_note:
                parts.append(size_note)
            if run_cmd:
                parts.append(f'\n  - {run_cmd}')

            lines.append(''.join(parts) + '\n')

    lines.append('\n')
    lines.append('Notes\n')
    lines.append('\n')
    lines.append('- This README was automatically generated. You can edit it to add more detailed explanations or examples.\n')
    lines.append('- If you prefer a different README style, update the workflow or the generator script at `.github/scripts/generate_readmes.py`.\n')

    # write the README
    readme_path.write_text(''.join(lines), encoding='utf-8')
    created.append(str(readme_path))
    print(f'Created {readme_path}')

if not created:
    print('No new README files created.')
    exit(0)

# Commit and push changes
try:
    subprocess.run(['git', 'config', 'user.name', 'github-actions[bot]'], check=True)
    subprocess.run(['git', 'config', 'user.email', '41898282+github-actions[bot]@users.noreply.github.com'], check=True)
    subprocess.run(['git', 'add'] + created, check=True)
    message = 'chore: auto-generate README files for new Placement folders'
    subprocess.run(['git', 'commit', '-m', message], check=True)
    subprocess.run(['git', 'push'], check=True)
    print('Committed and pushed README files.')
except subprocess.CalledProcessError as e:
    print('Failed to commit/push changes:', e)
    exit(1)
