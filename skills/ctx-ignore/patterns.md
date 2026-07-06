# ctx-ignore pattern reference

Battle-tested classification tables, ported from the original ctx-ignore CLI. Levels: **red** (always exclude), **yellow** (optional; confirm with the user before excluding).

## Directories (red unless noted)

| Pattern | Category |
| --- | --- |
| `node_modules/`, `vendor/`, `.venv/`, `venv/`, `.terraform/` | dependencies, never edit |
| `dist/`, `build/`, `out/`, `target/`, `.next/`, `.nuxt/`, `__pycache__/`, `storybook-static/`, `.turbo/`, `.cache/`, `.parcel-cache/` | build output, generated |
| `coverage/`, `__snapshots__/`, `.pytest_cache/` | test artifacts |
| `.idea/`, `.vscode/`, `.mypy_cache/` | IDE/OS noise |

## Exact filenames

| Pattern | Category | Level |
| --- | --- | --- |
| `package-lock.json`, `yarn.lock`, `pnpm-lock.yaml`, `bun.lockb`, `Cargo.lock`, `Gemfile.lock`, `poetry.lock`, `Pipfile.lock`, `uv.lock`, `go.sum`, `composer.lock` | lockfile, auto-generated | red |
| `.DS_Store`, `Thumbs.db` | IDE/OS noise | red |

## Extensions and suffixes

| Pattern | Category | Level |
| --- | --- | --- |
| `*.min.js`, `*.min.css` | build output, generated | red |
| `*.pb.go`, `*.pb.py`, `*.pb.ts` | generated code, do not edit | red |
| `*.snap` | test artifacts | red |
| `*.swp`, `*.log` | IDE/OS noise | red |
| binaries, media, archives, large data files | binary, not readable | red |
| `*_test.go`, `*.test.ts`, `*.spec.ts`, `test_*.py` and similar | test files | yellow |
| migrations | generated or mechanical | yellow |

## Generated-code detection

When a file is not covered above, check its first lines for generator markers ("Code generated", "DO NOT EDIT", "@generated", "AUTO-GENERATED") and for a generator config nearby (protobuf, openapi, ORM) before classifying it as generated.

## Reminders

- Yellow entries need user confirmation: some teams want agents reading tests.
- Lockfiles are noise for reading but load-bearing for reproducibility: exclude from context, never delete.
- These tables are a floor, not a ceiling; repos grow novel noise. Rank anything large and mechanically produced.
