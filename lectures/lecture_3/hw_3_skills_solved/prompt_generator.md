# Skill: Prompt Generator

## Когда активировать
Use this skill when the user asks to generate a new system prompt based on the consolidated analysis report.
Typical signals: "generate a new prompt", "create improved system prompt", "synthesize best patterns", "save generated prompt".

## Требуемые инструменты
- read_skill
- read_report
- save_report

## Goal
Read the consolidated report, transform the extracted best practices into one improved system prompt, and save the result through `save_report(name, content)`.

## Workflow
1. Read the report with `read_report("analysis_report")` unless the user provided another report name.
2. Extract the strongest recurring patterns and the key weaknesses to avoid.
3. Generate one new system prompt that is practical, clear, and ready to use.
4. Save it with `save_report(name, content)`.
5. Return a short completion message.

## Design requirements for the generated prompt
The generated prompt should include, when supported by the report:
- a clear role or persona
- a precise task definition
- explicit constraints and non-goals
- stepwise workflow or ordered reasoning instructions
- output format requirements
- truthfulness and source-discipline rules
- tool usage rules when tools are available
- concise style and anti-bloat discipline

## Output format
Produce markdown with these sections:

# Generated System Prompt
The full prompt in a fenced code block.

## Design notes
A short explanation of the main design choices, tied to the report findings.

## Expected benefits
3 to 5 concrete expected improvements.

## Footer JSON
```json
{
  "source_report": "analysis_report",
  "design_goals": ["..."],
  "included_patterns": ["..."],
  "avoided_patterns": ["..."]
}
```

## Naming rule for save_report
Default output name: `generated_prompt`

## Quality rules
- Do not simply merge all recommendations blindly.
- Resolve conflicts in favor of clarity, reliability, and low context overhead.
- Keep the generated prompt shorter than the sum of its sources.
- Produce a prompt that can be used directly without extra cleanup.
