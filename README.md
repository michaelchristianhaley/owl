# owlbox

**The reference implementation of the OWL Method: Outline, Wisdom, Legacy.**

> **OWL is not memory. It is a memory container.**
>
> The project's continuity lives inside the box. A fresh Assistant should be able to open it, inspect it, verify it, and continue the work.

owlbox keeps project continuity in three human-readable files:

| File | Purpose |
|---|---|
| `OUTLINE.md` | Current objective, verified state, active work, next action, unresolved items |
| `WISDOM.md` | Durable lessons future Assistants should not have to rediscover |
| `LEGACY.md` | Chronological milestones, decisions, failures, recoveries, and releases |

## Use owlbox in a project

```bash
python path/to/owlbox/scripts/owl.py init .
python path/to/owlbox/scripts/owl.py check .
```

Then maintain the three OWL files as the project changes.

## Validate owlbox itself

```bash
python scripts/owl.py check .
python -m unittest discover -s tests
```

## Reading path

- **30 seconds:** this file
- **5 minutes:** [`OWL.md`](OWL.md)
- **15 minutes:** [`HOWTOUPDATEOWL.md`](HOWTOUPDATEOWL.md)
- **Everything:** [`LANDING_PAD.md`](LANDING_PAD.md)

See [`MAP.md`](MAP.md) for every tracked file and its purpose.
