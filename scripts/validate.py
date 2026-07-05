#!/usr/bin/env python3
from pathlib import Path
import json
import sys

try:
    import yaml
except ImportError:
    yaml = None

ROOT = Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def parse_frontmatter(path: Path) -> dict:
    text = path.read_text()
    if not text.startswith("---\n"):
        fail(f"missing frontmatter: {path.relative_to(ROOT)}")
    parts = text.split("---", 2)
    if len(parts) < 3:
        fail(f"unterminated frontmatter: {path.relative_to(ROOT)}")
    body = parts[1]
    if yaml:
        data = yaml.safe_load(body) or {}
    else:
        data = {}
        for line in body.splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                data[key.strip()] = value.strip().strip('"')
    return data


def manifest_skill_paths(data: dict, manifest: Path) -> list[str]:
    paths = []
    for item in data.get("skills", []):
        raw_path = item.get("path") if isinstance(item, dict) else item
        if not raw_path:
            fail(f"manifest skill entry missing path: {manifest.relative_to(ROOT)}")
        candidates = [(ROOT / raw_path).resolve(), (manifest.parent / raw_path).resolve()]
        path = next((candidate for candidate in candidates if (candidate / "SKILL.md").exists()), candidates[0])
        try:
            rel_path = str(path.relative_to(ROOT))
        except ValueError:
            fail(f"manifest skill path escapes repo: {manifest.relative_to(ROOT)} -> {raw_path}")
        if not (ROOT / rel_path / "SKILL.md").exists():
            fail(f"manifest skill path missing SKILL.md: {manifest.relative_to(ROOT)} -> {raw_path}")
        paths.append(rel_path)
    return sorted(paths)


def main() -> None:
    skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
    if not skills:
        fail("no skills found")

    names = []
    skill_dirs = []
    for skill in skills:
        data = parse_frontmatter(skill)
        for field in ("name", "description"):
            if not data.get(field):
                fail(f"missing {field}: {skill.relative_to(ROOT)}")
        names.append(data["name"])
        skill_dirs.append(str(skill.parent.relative_to(ROOT)))

    # Codex manifest lists skill paths explicitly.
    codex_manifest = ROOT / ".codex-plugin/plugin.json"
    if not codex_manifest.exists():
        fail(f"missing manifest: {codex_manifest.relative_to(ROOT)}")
    codex_data = json.loads(codex_manifest.read_text())
    if manifest_skill_paths(codex_data, codex_manifest) != sorted(skill_dirs):
        fail(f"manifest skill list mismatch: {codex_manifest.relative_to(ROOT)}")

    # Claude plugin manifest relies on skills/ auto-discovery; check metadata instead.
    claude_manifest = ROOT / ".claude-plugin/plugin.json"
    if not claude_manifest.exists():
        fail(f"missing manifest: {claude_manifest.relative_to(ROOT)}")
    claude_data = json.loads(claude_manifest.read_text())
    for field in ("name", "description", "version", "license", "repository"):
        if not claude_data.get(field):
            fail(f"missing {field} in {claude_manifest.relative_to(ROOT)}")
    if "skills" in claude_data:
        fail("claude plugin.json should not list skills; skills/ is auto-discovered")

    marketplace = ROOT / ".claude-plugin/marketplace.json"
    if not marketplace.exists():
        fail(f"missing manifest: {marketplace.relative_to(ROOT)}")
    marketplace_data = json.loads(marketplace.read_text())
    if not marketplace_data.get("plugins"):
        fail("marketplace.json has no plugins entry")

    registry = ROOT / "REGISTRY.md"
    if not registry.exists():
        fail("missing REGISTRY.md")
    registry_text = registry.read_text()
    for name in names:
        if f"`{name}`" not in registry_text:
            fail(f"skill missing from registry: {name}")

    evals_path = ROOT / "evals/ctxops-evals.json"
    if not evals_path.exists():
        fail("missing evals/ctxops-evals.json")
    evals = json.loads(evals_path.read_text())
    eval_names = {item.get("skill") for item in evals.get("evals", [])}
    missing_evals = sorted(set(names) - eval_names)
    if missing_evals:
        fail(f"missing eval prompts for: {', '.join(missing_evals)}")

    incubating = sorted((ROOT / "incubating").glob("*/SKILL.md"))
    for skill in incubating:
        data = parse_frontmatter(skill)
        for field in ("name", "description"):
            if not data.get(field):
                fail(f"missing {field}: {skill.relative_to(ROOT)}")

    print(f"ok: {len(skills)} skills ({', '.join(names)})"
          + (f" + {len(incubating)} incubating" if incubating else ""))


if __name__ == "__main__":
    main()
