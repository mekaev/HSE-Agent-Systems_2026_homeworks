# Skill: Analysis Report

## Когда активировать
Use this skill when the user asks for a consolidated report across multiple saved prompt analyses.
Typical signals: "make a summary report", "compare all analyses", "extract common patterns", "save report".

## Требуемые инструменты
- read_skill
- list_analyses
- read_analysis
- save_report

## Goal
Read all saved analyses, compare them systematically, extract recurring prompt design patterns, and save one consolidated report through `save_report(name, content)`.

## Workflow
1. Call `list_analyses()`.
2. Read each analysis with `read_analysis(name)`.
3. Compare them across shared dimensions.
4. Synthesize a concise report with reusable findings.
5. Save it with `save_report(name, content)`.
6. Return a short completion message.

## Comparison dimensions
Use these dimensions when comparing analyses:
- role clarity
- task framing
- decomposition and step structure
- reasoning scaffolds
- examples and demonstrations
- output constraints
- guardrails and truthfulness controls
- tool usage discipline
- brevity vs coverage

## Output format
Produce markdown with these sections:

# Consolidated Prompt Analysis Report

## Scope
- Number of analyses read
- Names of analyses included

## Executive summary
A short synthesis of the overall quality level and the dominant design style.

## Recurrent strengths
List repeated strong patterns across files.

## Recurrent weaknesses
List repeated design problems across files.

## Cross-file comparison table
Use a markdown table with columns:
- Analysis
- Overall verdict
- Strongest feature
- Weakest feature
- Reusable pattern

## Best practices extracted
Turn the comparison into a reusable checklist for future prompt design.

## Recommendations
Prioritized actions for building better prompts in this project.

## Report footer
End with a compact JSON block:

```json
{
  "analyses_count": 0,
  "shared_strengths": ["..."],
  "shared_weaknesses": ["..."],
  "priority_recommendations": ["..."]
}
```

## Naming rule for save_report
Default report name: `analysis_report`

## Quality rules
- Base conclusions on the saved analyses, not on memory.
- Focus on reusable patterns, not per-file trivia.
- Avoid duplicate points.
- Prefer synthesis over long quotations.
