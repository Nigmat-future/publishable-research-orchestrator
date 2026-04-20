# Output Contract

Use this reference when the user wants a full decision pack or an execution-ready research program.

## Minimum Deliverables

Always leave behind these artifacts, either in the response or in generated files:

1. `candidate-landscape`
2. `scorecard`
3. `selected-direction`
4. `execution-plan`
5. `next-actions`

## Recommended File Set

If you are writing files to disk, prefer this structure:

- `00-project-brief.md`
- `01-landscape-map.md`
- `02-topic-scorecard.md`
- `03-selected-direction.md`
- `04-execution-plan.md`
- `05-experiment-matrix.md`
- `06-writing-outline.md`
- `notes/source-log.md`
- `notes/decision-log.md`

## Candidate Entry Template

Use this shape for each candidate:

```markdown
## Candidate: <name>

Thesis:
Problem:
Gap:
Why now:
Contribution type:
Minimal decisive experiment:
Likely baselines:
Dependencies:
Main risk:
Weighted score:
```

## Execution Plan Template

Use this shape for each milestone:

```markdown
## Milestone <n>: <title>

Objective:
Inputs:
Tasks:
Exit criteria:
Risk:
Fallback:
Artifact:
```

## Next Actions Template

Always end with:
- what to do in the next `72 hours`
- what to do in the next `2 weeks`
- what to do in the next `6 weeks`

If the user wants immediate execution, start the first `72 hours` block instead of repeating the plan.
