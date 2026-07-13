# How to Update owlbox

## First rule

Whenever any tracked source file changes, regenerate and verify `MAP.md` and `LANDING_PAD.md` before committing.

```bash
python scripts/owl.py generate .
python scripts/owl.py check .
python -m unittest discover -s tests
```

## Update procedure

1. Read `OUTLINE.md`, `WISDOM.md`, and `LEGACY.md`.
2. Inspect the files and evidence relevant to the change.
3. Edit canonical sources.
4. Update owlbox's own OWL files:
   - active state in `OUTLINE.md`;
   - durable lessons in `WISDOM.md`;
   - significant events in `LEGACY.md`.
5. Run generation, validation, and tests.
6. Review the complete diff.
7. Commit only after every gate passes.

## Adding a file

A new file must:

- have one distinct purpose;
- be declared in `control/owl.json`;
- appear in `MAP.md`;
- be included or deliberately excluded from `LANDING_PAD.md`;
- add more value than a section in an existing file.

## Changing the OWL contract

Update:

1. `OWL.md`;
2. `control/owl.json`;
3. templates;
4. validator tests;
5. generated views;
6. `LEGACY.md`.

## Release check

```bash
python scripts/owl.py check .
python -m unittest discover -s tests
git diff --check
git status --short
```

A release is not verified until the committed remote state is checked independently.
