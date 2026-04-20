# Publishability Rubric

Use this reference when ranking candidate directions.

## Weighted Dimensions

Score each dimension from `1` to `5`.

| Dimension | Weight | What to look for |
| --- | ---: | --- |
| Novelty clarity | 0.22 | The contribution is visibly distinct from recent work. |
| Evidence density | 0.16 | There is enough literature and source material to reason accurately. |
| Feasibility | 0.16 | The work fits the user's time, data, and compute constraints. |
| Evaluation clarity | 0.16 | Success and failure are measurable with credible metrics. |
| Baseline accessibility | 0.10 | Strong baselines exist and can plausibly be reproduced. |
| Venue fit | 0.10 | A conference, journal, or technical audience would understand the value. |
| Strategic upside | 0.10 | Even moderate success would produce useful insight or a strong artifact. |

## Interpretation

- `4.2+`: strong candidate
- `3.6-4.19`: viable but risky
- `3.0-3.59`: weak unless the user has hidden advantages
- `<3.0`: reject

## Hard Kill Criteria

Reject immediately if any of the following is true:

- novelty depends on ignoring recent publications
- the contribution cannot be evaluated credibly
- required data is unavailable and no fallback exists
- compute demands are far above the user's likely budget
- the thesis is too vague to falsify
- the idea sounds like "apply model X to domain Y" without a deeper mechanism

## Direction Types That Often Work

- benchmark or evaluation blind spots
- system bottlenecks with measurable efficiency or quality gains
- data curation or filtering methods with strong downstream impact
- robustness, controllability, safety, or failure-analysis methods
- agent workflow limitations that can be measured on real tasks

## Direction Types That Often Fail

- generic framework proposals without decisive experiments
- tiny prompt variants with no theory and no durable gain
- pure tooling ideas presented as research without a research claim
- ideas that require a proprietary dataset but no public substitute

## Recommendation Format

When presenting the ranking, include:
- total weighted score
- one-line reason it scored high or low
- the single biggest risk
- the first experiment you would run
