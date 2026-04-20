# Publishable Research Orchestrator

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![Codex Skill](https://img.shields.io/badge/Codex-Skill-blue)](./SKILL.md)
[![Research Workflow](https://img.shields.io/badge/Workflow-Multi--Agent%20Research-black)](./references/research-playbook.md)

Turn a vague research idea into a publication-grade execution plan.

`publishable-research-orchestrator` is a Codex skill for multi-agent technical research. It helps Codex discover promising research directions, score them for publishability, reject weak options, and translate the winning idea into a concrete execution program with milestones, exit criteria, and artifacts.

It is designed for AI-heavy and technical domains such as:
- LLM systems
- agent workflows
- software engineering research
- benchmarking and evaluation
- ML infrastructure and tooling
- adjacent computer science topics

## Why This Exists

Most research assistants can collect papers. Far fewer can answer the harder questions:

- Which topic is actually publishable?
- Which direction is new enough without being unrealistic?
- What is the minimum publishable unit?
- What should happen in the next 72 hours, 2 weeks, and 6 weeks?

This skill is built to make those decisions explicit.

## What The Skill Produces

By default, the skill aims to leave behind a complete decision package:

1. A candidate landscape with `3-7` plausible directions.
2. A publishability scorecard for each candidate.
3. One selected direction with a clear thesis.
4. A step-by-step execution plan with milestones and fallback paths.
5. A near-term action plan for `72 hours`, `2 weeks`, and `6 weeks`.

## Core Capabilities

- Multi-agent research orchestration when the user explicitly authorizes subagents.
- Research-gap discovery grounded in recent literature and primary sources.
- Publishability scoring using a structured rubric.
- Candidate down-selection with explicit rejection logic.
- Milestone design for execution, experiments, and write-up.
- Workspace scaffolding for repeatable research packages.

## Research Modes

| Mode | Use When |
| --- | --- |
| `discovery` | You only have a broad area and need candidate directions. |
| `down-select` | You already have several ideas and need ranking and rejection logic. |
| `program-design` | You know the likely direction and need a precise execution plan. |
| `execution` | You want the work to begin: artifacts, experiments, or writing support. |

## How It Works

The skill follows a compact but disciplined workflow:

1. Frame the research space.
2. Shape the problem into a researchable question.
3. Run parallel reconnaissance when multi-agent work is explicitly allowed.
4. Build a candidate matrix.
5. Score candidates with a publishability rubric.
6. Select one direction and lock the thesis.
7. Break the direction into milestones and artifacts.
8. Scaffold a working research pack if execution is requested.

Detailed playbooks live here:
- [references/research-playbook.md](./references/research-playbook.md)
- [references/publishability-rubric.md](./references/publishability-rubric.md)
- [references/output-contract.md](./references/output-contract.md)

## Quick Start

Place this repository inside your Codex skills directory, or symlink it there:

```powershell
git clone https://github.com/Nigmat-future/publishable-research-orchestrator.git
```

Then invoke it from Codex with prompts like:

```text
Use $publishable-research-orchestrator to find 5 publishable research directions in AI agents and select the strongest one.
```

```text
Use $publishable-research-orchestrator to compare three benchmark ideas for code review agents and produce a 6-week execution plan.
```

```text
Use $publishable-research-orchestrator to identify a publication-grade topic in LLM evaluation and scaffold the research workspace.
```

## Workspace Scaffold

The repository includes a helper script to generate a standard research pack:

```powershell
python .\scripts\scaffold_research_pack.py --topic "agentic code review benchmarks" --output .
```

That produces a dated workspace with:

- `00-project-brief.md`
- `01-landscape-map.md`
- `02-topic-scorecard.md`
- `03-selected-direction.md`
- `04-execution-plan.md`
- `05-experiment-matrix.md`
- `06-writing-outline.md`
- `notes/source-log.md`
- `notes/decision-log.md`

## Repository Structure

```text
publishable-research-orchestrator/
├── SKILL.md
├── README.md
├── LICENSE
├── agents/
│   └── openai.yaml
├── references/
│   ├── output-contract.md
│   ├── publishability-rubric.md
│   └── research-playbook.md
└── scripts/
    └── scaffold_research_pack.py
```

## Design Principles

- Prefer decision-quality over literature dumping.
- Prefer primary sources for technical claims.
- Prefer falsifiable ideas over vague novelty.
- Prefer realistic publishability over fashionable wording.
- Keep synthesis local even when research is parallelized.

## Best Fit

This skill works best when:
- the topic is technical and fast-moving
- recency matters
- you want explicit selection logic
- you need a plan that can actually be executed

This skill is not ideal for:
- simple factual lookups
- one-off debugging questions
- casual brainstorming without evidence
- non-technical domains that require field-specific publication norms

## License

Released under the [MIT License](./LICENSE).
