# Skills registry for HW 3

This file is Level 1 metadata only.
Use it in the system prompt so the agent sees a compact overview instead of full procedures.
Load a full skill with `read_skill(name)` only when the current task clearly matches that skill.

## Available skills

### prompt_analysis
Use when the task is to inspect one specific prompt file from GitHub, identify its structure and prompting techniques, evaluate quality, and save a per-file analysis with `save_analysis(name, content)`.

### analysis_report
Use when the task is to read all saved analyses, compare recurring patterns across prompts, extract reusable design principles, produce one consolidated report, and save it with `save_report(name, content)`.

### prompt_generator
Use when the task is to read the consolidated report, synthesize the best patterns into a new system prompt, explain major design choices briefly, and save the result with `save_report(name, content)`.

## Global rules
- One agent run solves one atomic task.
- Do not analyze multiple GitHub prompt files in one run.
- For repository content, use GitHub MCP tools only.
- For local intermediate state, use local file tools only.
- Do not invent missing file contents.
- Prefer short structured outputs over verbose prose.
