#!/usr/bin/env python3
"""
Create a standard research workspace for a selected topic.
"""

from __future__ import annotations

import argparse
import re
from datetime import datetime
from pathlib import Path


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-{2,}", "-", value).strip("-")
    return value or "research-topic"


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def build_files(topic: str, field: str, mode: str, date_tag: str) -> dict[str, str]:
    brief = f"""# Project Brief

Topic: {topic}
Field: {field}
Mode: {mode}
Created: {date_tag}

Goal:
Publication target:
Time horizon:
Compute and data constraints:
Implementation appetite:
Success condition:
"""

    landscape = f"""# Landscape Map

## Scope

Topic: {topic}
Field: {field}

## Canonical Work

- Paper:
  Link:
  Why it matters:

## Recent Work

- Paper:
  Date:
  Link:
  Claimed contribution:
  Notes:

## Crowded Areas

- Area:
  Evidence:

## Under-explored Gaps

- Gap:
  Evidence:
  Why it still matters:
"""

    scorecard = """# Topic Scorecard

| Candidate | Novelty | Evidence | Feasibility | Evaluation | Baselines | Venue Fit | Upside | Weighted Score | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Candidate A |  |  |  |  |  |  |  |  |  |
| Candidate B |  |  |  |  |  |  |  |  |  |
| Candidate C |  |  |  |  |  |  |  |  |  |
"""

    selected = f"""# Selected Direction

Topic: {topic}

## Thesis

## Why This Wins

## Why The Others Lose

## Core Claim

## Expected Contribution Type

## Minimal Publishable Unit

## Required Baselines

## Required Datasets Or Tasks

## First Decisive Experiment
"""

    plan = """# Execution Plan

## Milestone 1: Baseline Replication
Objective:
Inputs:
Tasks:
Exit criteria:
Risk:
Fallback:
Artifact:

## Milestone 2: Problem And Metric Lock
Objective:
Inputs:
Tasks:
Exit criteria:
Risk:
Fallback:
Artifact:

## Milestone 3: Method Implementation
Objective:
Inputs:
Tasks:
Exit criteria:
Risk:
Fallback:
Artifact:

## Milestone 4: Minimal Decisive Experiment
Objective:
Inputs:
Tasks:
Exit criteria:
Risk:
Fallback:
Artifact:
"""

    experiments = """# Experiment Matrix

| Experiment | Hypothesis | Variables | Metrics | Baseline | Expected Signal | Status |
| --- | --- | --- | --- | --- | --- | --- |
| E1 |  |  |  |  |  | planned |
| E2 |  |  |  |  |  | planned |
| E3 |  |  |  |  |  | planned |
"""

    outline = """# Writing Outline

## Title Candidates

- 

## Abstract Skeleton

Problem:
Gap:
Method:
Results:
Contribution:

## Paper Structure

1. Introduction
2. Related Work
3. Method
4. Experimental Setup
5. Results
6. Analysis
7. Limitations
8. Conclusion
"""

    source_log = """# Source Log

| Source | Date | Type | Relevance | Reliability Notes |
| --- | --- | --- | --- | --- |
"""

    decision_log = """# Decision Log

| Date | Decision | Reason | Evidence | Owner |
| --- | --- | --- | --- | --- |
"""

    return {
        "00-project-brief.md": brief,
        "01-landscape-map.md": landscape,
        "02-topic-scorecard.md": scorecard,
        "03-selected-direction.md": selected,
        "04-execution-plan.md": plan,
        "05-experiment-matrix.md": experiments,
        "06-writing-outline.md": outline,
        "notes/source-log.md": source_log,
        "notes/decision-log.md": decision_log,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create a standard research workspace for a chosen topic.",
    )
    parser.add_argument("--topic", required=True, help="Selected research topic.")
    parser.add_argument(
        "--output",
        default=".",
        help="Parent output directory. Default: current directory.",
    )
    parser.add_argument(
        "--field",
        default="technical-ai",
        help="Research field label. Default: technical-ai.",
    )
    parser.add_argument(
        "--mode",
        default="program-design",
        choices=["discovery", "down-select", "program-design", "execution"],
        help="Research mode. Default: program-design.",
    )
    args = parser.parse_args()

    date_tag = datetime.now().strftime("%Y%m%d")
    folder_name = f"{date_tag}-{slugify(args.topic)}"
    root = Path(args.output).expanduser().resolve() / folder_name
    root.mkdir(parents=True, exist_ok=True)

    for relative_path, content in build_files(args.topic, args.field, args.mode, date_tag).items():
        write_file(root / relative_path, content)

    print(root)


if __name__ == "__main__":
    main()
