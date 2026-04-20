---
name: publishable-research-orchestrator
description: Orchestrate multi-agent research for technical and AI-heavy topics, from literature reconnaissance and research-gap discovery to publishability scoring, step-by-step execution planning, and implementation-ready delivery. Use when Codex needs to identify a publication-grade research direction, compare candidate topics, judge novelty and feasibility, coordinate multiple agents for parallel investigation, or turn a vague idea into an ordered research program that can be executed and written up.
---

# Publishable Research Orchestrator

## Overview

Use this skill to convert a vague research ambition into a publication-grade program with evidence, ranking logic, and an execution sequence.

Default to technical research in AI, ML, LLM systems, software engineering, agents, or adjacent computer science domains. If the user does not specify a field, infer the most plausible technical domain from the repo and conversation, state the assumption, and continue.

When available and relevant:
- Use `$parallel-agent-orchestration` to structure multi-agent delegation.
- Use `$deep-research` for citation-heavy web research and source verification.

## Output Contract

Always produce the smallest package that still lets the user decide and act. Unless the user requests a narrower output, deliver:

1. A candidate landscape with `3-7` plausible research directions.
2. A publishability scorecard for each candidate.
3. One selected direction with a clear thesis, contribution shape, and rejection rationale for the discarded options.
4. A step-by-step execution plan with milestones, exit criteria, and fallback paths.
5. A near-term action list for the next `72 hours`, `2 weeks`, and `6 weeks`.

If the user asks only for evaluation, still provide the scorecard and a recommendation. If the user asks for implementation, extend the package into an execution program and begin the first milestone.

## Source Discipline

Prefer primary or near-primary sources for technical claims:
- papers
- official documentation
- benchmark leaderboards
- project repositories
- dataset pages
- venue calls or guidelines

For every major claim, keep enough evidence to answer:
- What is already known?
- What gap still exists?
- Why is this gap still interesting now?
- What would count as evidence that the idea worked?

Do not recommend a direction whose novelty depends on ignoring recent work.

## Multi-Agent Topology

Use subagents only when the user explicitly asks for multi-agent, parallel, delegated, or side-by-side work. When that condition is met, keep the critical path local and delegate only bounded sidecar tasks.

Keep local:
- scope framing
- scoring rubric selection
- final synthesis
- candidate down-selection
- milestone design
- final recommendation

Good parallel lanes:

1. `explorer`: Map the literature landscape and canonical papers.
2. `explorer`: Identify unsolved problems, contradiction points, and research gaps.
3. `explorer`: Map datasets, baselines, evaluation protocols, compute cost, and reproducibility risks.
4. `explorer`: Assess venue fit, timeliness, and whether the direction is already crowded.
5. `worker`: Build artifacts or implementation scaffolds only after a direction is selected.

For every delegated task:
- assign a narrow scope
- ask for concrete evidence and dates
- ask for assumptions and confidence
- ask for file paths if any files were changed
- remind the agent it is not alone in the codebase and must not revert others' work

Do not delegate the synthesis itself.

## Research Modes

Choose one mode explicitly before doing deep work:

1. `discovery`
   Use when the user has only a broad area and needs candidate directions.
2. `down-select`
   Use when the user already has multiple ideas and needs ranking and rejection logic.
3. `program-design`
   Use when the direction is mostly chosen and the user needs a precise step-by-step plan.
4. `execution`
   Use when the user wants implementation, experiments, artifacts, or writing support.

It is fine to move from one mode to the next in a single turn if the evidence is strong enough.

## Standard Workflow

Load these references as needed:
- [research-playbook.md](./references/research-playbook.md) for the detailed phase workflow and agent prompts
- [publishability-rubric.md](./references/publishability-rubric.md) for scoring weights, red flags, and kill criteria
- [output-contract.md](./references/output-contract.md) for the exact artifact set and milestone format

Use this sequence:

1. Frame the research space.
   Capture domain, user goal, time horizon, target venue or publication standard, compute constraints, data constraints, and implementation appetite.

2. Decide the mode and research question shape.
   Convert a vague theme into a researchable question, such as a benchmark gap, systems bottleneck, evaluation blind spot, data curation problem, or alignment/control weakness.

3. Run parallel reconnaissance when authorized.
   Split literature, gaps, evaluation infrastructure, and venue pressure into separate lanes.

4. Build the candidate matrix.
   Generate `3-7` candidates. For each candidate, record:
   - problem statement
   - why now
   - proposed contribution
   - minimum publishable unit
   - key dependencies
   - primary risks

5. Score and reject aggressively.
   Use the publishability rubric. Kill ideas that fail on novelty, feasibility, or measurable evaluation.

6. Select one direction and lock the thesis.
   State:
   - core claim
   - expected contribution type
   - required baselines
   - required datasets or tasks
   - minimal experiment that would prove signal

7. Turn the direction into an execution program.
   Break the work into milestones with artifacts, success criteria, and fallback branches.

8. If execution is requested, scaffold the workspace.
   Use `python scripts/scaffold_research_pack.py --topic "<topic>" --output "<directory>"` to generate a standard research pack before writing the detailed content.

## Milestone Design Rules

Every milestone must include:
- objective
- inputs
- concrete tasks
- exit criteria
- risk or failure mode
- fallback move
- artifact to leave behind

Prefer this ordering:

1. Replication and ground-truthing of the baseline.
2. Lock the task, data, metrics, and evaluation protocol.
3. Build the baseline harness and error-analysis workflow.
4. Implement the new method or intervention.
5. Run the smallest decisive experiment.
6. Expand to ablations, robustness checks, and failure analysis.
7. Package the writing outline, figures, and contribution narrative.

Do not let implementation start before the evaluation protocol is explicit.

## Decision Rules for Publishability

Prefer directions that satisfy most of the following:
- a crisp, falsifiable claim
- an obvious gap relative to recent literature
- available data or reproducible synthetic data
- baselines that are strong but not impossible to reproduce
- an evaluation plan that can disconfirm the claim
- a plausible venue or audience
- a contribution that still matters if the headline metric gain is modest

Avoid directions that depend on:
- hidden proprietary data with no fallback
- vague novelty claims
- impossible compute
- no clear baseline
- no measurable endpoint
- a timeline too short for the required evidence

## Final Answer Style

When using this skill, keep the final answer decision-oriented. Lead with:
- recommended direction
- why it wins
- why the others lose
- what to do next

Do not bury the recommendation under a long literature dump. Synthesis matters more than collection.
