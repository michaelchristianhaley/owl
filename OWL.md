# The OWL Method

## Purpose

OWL grounds The Assistant in a project through:

- `OUTLINE.md` — active working memory;
- `WISDOM.md` — durable project knowledge;
- `LEGACY.md` — chronological continuity.

The User owns the project. The Assistant maintains OWL subject to The User's direction and the project's governing rules.

## Continuity standard

A fresh Assistant passes an OWL handoff when the repository alone reveals:

1. the current objective;
2. the verified current state;
3. the immediate next action;
4. unresolved questions, risks, and blockers;
5. durable lessons;
6. major decisions and milestones that explain the present.

Missing chat history must not prevent safe continuation.

## Outline

`OUTLINE.md` is The Assistant's desk.

It contains:

- current objective;
- verified current state;
- active work;
- next action;
- unresolved items;
- temporary notes that still affect the work.

It is human-readable, actively rewritten, aggressively culled, and expected to trend toward zero.

It is not a transcript, an append-only log, a permanent lesson store, or a substitute for evidence.

## Wisdom

`WISDOM.md` is the project's curated long-term knowledge.

It contains proven methods, verified discoveries, recurring failure modes, durable principles, and corrections future Assistants should not have to rediscover.

It grows slowly. It may be revised when better evidence narrows or disproves a lesson. It does not automatically change project governance.

## Legacy

`LEGACY.md` explains how the project reached its present state.

It records dated milestones, decisions, state transitions, significant failures and recoveries, and releases.

It is chronological and append-oriented. Facts may be corrected, but meaningful history is not silently rewritten.

## Information flow

```text
Active and temporary → OUTLINE.md
Proven and reusable  → WISDOM.md
Significant event    → LEGACY.md
Finished and trivial → remove
```

One fact may appear in more than one OWL file only when each entry serves a different purpose.

## Grounding procedure

Before substantial work, The Assistant:

1. reads all three OWL files;
2. checks relevant live evidence and repository state;
3. identifies conflicts, stale claims, and unknowns;
4. corrects Outline before acting when necessary;
5. acts from reconciled state, not remembered conversation.

After substantial work, The Assistant:

1. verifies the result;
2. updates Outline;
3. promotes durable lessons to Wisdom;
4. records significant events in Legacy;
5. runs the OWL check.

## Evidence language

- **Verified** — supported by current direct evidence.
- **Inferred** — reasoned from stated evidence.
- **Unknown** — not established.

Do not use a stronger state than the evidence supports.

## Failure conditions

An OWL handoff fails when:

- the current objective or next action cannot be found;
- Outline presents stale work as current;
- Wisdom contains untested guesses;
- Legacy omits a state transition needed to understand the present;
- the files contradict one another without reconciliation;
- generated views are stale;
- validation is claimed without reproducible evidence.

## Recovery

When continuity breaks:

1. stop consequential work;
2. inspect live repository and system evidence;
3. identify the last verified state;
4. correct Outline first;
5. repair Wisdom and Legacy only where evidence supports it;
6. run validation;
7. resume from the reconciled state.
