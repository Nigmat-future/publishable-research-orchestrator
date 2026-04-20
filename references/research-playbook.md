# Research Playbook

Use this reference when the task requires concrete orchestration details, subagent prompt design, or a more disciplined research pipeline.

## Phase 1: Frame

Extract or infer:
- domain
- target problem class
- expected publication standard
- time horizon
- compute budget
- data availability
- need for implementation versus planning only

If the user is vague, convert the request into a sharp research question before searching.

## Phase 2: Reconnaissance

Run search across primary sources and recent work. Bias toward:
- the last `12-24` months for fast-moving AI topics
- canonical papers for foundational baselines
- reproducible repositories and benchmark pages

Track:
- what is saturated
- what is under-explored
- what already has strong baselines
- what is likely to be rejected as incremental

## Phase 3: Agent Split

Use this split when parallel work is explicitly authorized.

### Explorer A: Landscape Map

Prompt shape:

```text
Inspect the recent literature and canonical work for <topic>. Focus only on the problem landscape, important papers, and what is already crowded. Report the most relevant sources, dates, and the strongest baseline directions.
```

### Explorer B: Gap Finder

Prompt shape:

```text
Inspect <topic> for unresolved gaps, contradictions, weak evaluations, or missing capabilities. Focus only on gaps that could plausibly support a publishable contribution. Report sources, dates, and confidence.
```

### Explorer C: Evaluation Infrastructure

Prompt shape:

```text
Inspect datasets, baselines, metrics, and reproducibility constraints for <topic>. Focus only on what would be required to run a credible evaluation and what might block execution.
```

### Explorer D: Venue and Timing

Prompt shape:

```text
Inspect likely venues or research audiences for <topic>. Focus on whether the space is too crowded, whether the contribution would sound incremental, and what kind of evidence the venue would expect.
```

Keep synthesis local. Ask each agent for evidence, dates, assumptions, and confidence.

## Phase 4: Candidate Matrix

Generate `3-7` candidates. For each candidate, fill:

- title
- one-sentence thesis
- problem
- gap
- why now
- expected contribution type
- minimal decisive experiment
- likely baselines
- dependencies
- failure modes

## Phase 5: Down-Selection

Reject candidates that show any of these:
- no measurable test
- no defensible novelty
- unrealistic implementation burden
- dependence on unavailable data or hardware
- unclear audience

Select the candidate with the best risk-adjusted expected publishability, not the most fashionable wording.

## Phase 6: Program Design

Translate the selected candidate into milestones:

1. Baseline replication
2. Problem and metric lock
3. Data and protocol validation
4. Method implementation
5. Minimal decisive experiment
6. Expansion experiments
7. Writing and packaging

For each milestone, define:
- deliverable
- owner
- prerequisites
- success bar
- fallback plan

## Phase 7: Execution

If the user wants the work done, start from the first unfinished milestone instead of re-explaining the whole plan.

Artifacts to maintain:
- source log
- candidate scorecard
- decision log
- experiment matrix
- writing outline

Use the scaffold script before producing structured artifacts at scale.
