# Skill: Prompt Analysis

## Когда активировать
Use this skill when the user asks to analyze one specific prompt file from GitHub and save a structured per-file analysis.
Typical signals: "analyze this prompt", "inspect prompt.md", "review system prompt", "save analysis for this file".
Use exactly one file per agent run.

## Требуемые инструменты
- read_skill
- get_file_contents
- save_analysis

## Goal
Read one prompt file from GitHub, evaluate it with a consistent rubric, produce a compact but information-dense analysis, and save it through `save_analysis(name, content)`.

## Workflow
1. Confirm the target file path from the user request.
2. Read the file from GitHub with `get_file_contents`.
3. Inspect the prompt as text. Do not assume hidden context outside the file.
4. Evaluate the prompt using the rubric below.
5. Produce a structured markdown analysis.
6. Save it with `save_analysis(name, content)`.
7. Return a short completion message with the saved analysis name.

## Rubric
Evaluate at least these dimensions:

### 1. Role and persona
Check whether the prompt assigns a clear expert role, operating stance, or behavioral identity.
Look for specificity, scope, and consistency.

### 2. Task objective and success criteria
Check whether the task is explicit.
Identify what the model is supposed to produce, for whom, and how success is judged.

### 3. Instructions and decomposition
Check whether the prompt breaks the work into ordered steps, phases, or decision rules.
Good prompts reduce ambiguity and sequence the work.

### 4. Context and inputs
Check whether the prompt defines available data, assumptions, constraints, and what the model must not fabricate.

### 5. Few-shot examples or demonstrations
Check whether the prompt contains examples, templates, edge cases, or input-output demonstrations.
If none exist, state that explicitly.

### 6. Reasoning guidance
Check whether the prompt asks for internal stepwise reasoning, explicit analysis steps, verification, or self-checks.
Do not ask the model to reveal hidden chain-of-thought. Just note observable reasoning scaffolds in the prompt.

### 7. Output format
Check whether the output structure is constrained: markdown, JSON, sections, bullets, tables, length limits, or required fields.

### 8. Guardrails and boundaries
Check whether the prompt contains safety limits, refusal rules, source discipline, anti-hallucination rules, scope boundaries, or escalation rules.

### 9. Tool and environment usage
Check whether the prompt tells the model what tools may be used, when to use them, and what data sources are trusted.

### 10. Efficiency and clarity
Check whether the prompt is concise relative to its goals, avoids repetition, and keeps instructions non-contradictory.

## Output format
Produce markdown with exactly these sections:

### Header
- File path
- Analysis name
- Short verdict: strong / mixed / weak

### Prompt summary
2 to 4 sentences on what the prompt is trying to achieve.

### Strengths
3 to 7 concrete points.

### Weaknesses
3 to 7 concrete points.

### Rubric assessment
For each rubric dimension, include:
- Score: 1 to 5
- Evidence: short quote or paraphrase from the prompt
- Comment: why it matters

### Reusable patterns
List patterns worth reusing in other prompts.

### Improvement recommendations
List the highest-leverage fixes first.

### Compact structured block
At the end include a compact machine-friendly block:

```json
{
  "file_path": "...",
  "overall_verdict": "strong|mixed|weak",
  "top_strengths": ["..."],
  "top_weaknesses": ["..."],
  "recommended_actions": ["..."]
}
```

## Naming rule for save_analysis
Convert the GitHub path into a stable analysis name:
- replace `/` with `_`
- remove `.md`
- keep letters, digits, `_`, `-`

Example:
- `Anthropic/FlintK12/prompt.md` -> `Anthropic_FlintK12_prompt`

## Quality rules
- Ground every important claim in the prompt text.
- Do not praise generically.
- Do not rewrite the whole prompt unless explicitly asked.
- Prefer concrete diagnostics over theory.
- Keep the analysis rich, but avoid unnecessary narration.
