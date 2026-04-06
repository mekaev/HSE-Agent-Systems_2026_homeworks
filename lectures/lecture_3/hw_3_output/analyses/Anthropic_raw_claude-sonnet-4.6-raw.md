```markdown
### Header
- File path: Anthropic/raw/claude-sonnet-4.6-raw.md
- Analysis name: Anthropic_raw_claude-sonnet-4.6-raw
- Short verdict: strong

### Prompt summary
The prompt defines the role and capabilities of Claude, an AI assistant operating within Anthropic's chat interfaces. It outlines the use of tools for accessing past conversations, specifies trigger patterns for tool usage, and provides detailed instructions for tool selection and response guidelines. The prompt aims to enhance continuity in user interactions by leveraging past chat data.

### Strengths
1. **Role and Persona**: Clearly defines Claude's role as an assistant within specific interfaces, providing a strong identity.
2. **Task Objective**: Explicitly outlines the objective of using past chat tools to improve response continuity.
3. **Instructions and Decomposition**: Provides detailed, step-by-step instructions for tool usage, reducing ambiguity.
4. **Context and Inputs**: Clearly defines the context in which tools should be used, including constraints and assumptions.
5. **Reasoning Guidance**: Offers a decision framework for tool selection, guiding Claude's reasoning process.
6. **Output Format**: Specifies how to format responses, including guidelines for chat links and synthesis of information.
7. **Guardrails and Boundaries**: Includes safety limits and refusal rules, ensuring responsible tool usage.

### Weaknesses
1. **Few-shot Examples**: Lacks explicit few-shot examples or demonstrations within the main instructions.
2. **Efficiency and Clarity**: While detailed, the prompt could be more concise in some sections to enhance clarity.
3. **Tool and Environment Usage**: Could provide more explicit guidance on trusted data sources for tool usage.
4. **Output Format**: While structured, the prompt could benefit from more examples of output formats.
5. **Guardrails and Boundaries**: Could include more explicit anti-hallucination rules.
6. **Reasoning Guidance**: While present, the reasoning guidance could be expanded with more examples.
7. **Instructions and Decomposition**: Some instructions could be simplified for better efficiency.

### Rubric assessment
- **Role and persona**
  - Score: 5
  - Evidence: "The assistant is Claude, created by Anthropic."
  - Comment: Establishes a clear identity and scope for Claude.

- **Task objective and success criteria**
  - Score: 5
  - Evidence: "Use these tools when the user references past conversations..."
  - Comment: Clearly defines the task and success criteria.

- **Instructions and decomposition**
  - Score: 4
  - Evidence: "Check whether the prompt breaks the work into ordered steps..."
  - Comment: Provides detailed instructions but could be more concise.

- **Context and inputs**
  - Score: 5
  - Evidence: "Defines available data, assumptions, constraints..."
  - Comment: Clearly outlines the context and constraints.

- **Few-shot examples or demonstrations**
  - Score: 3
  - Evidence: "Check whether the prompt contains examples..."
  - Comment: Lacks explicit few-shot examples within the main instructions.

- **Reasoning guidance**
  - Score: 4
  - Evidence: "Check whether the prompt asks for internal stepwise reasoning..."
  - Comment: Provides a decision framework but could include more examples.

- **Output format**
  - Score: 4
  - Evidence: "Check whether the output structure is constrained..."
  - Comment: Specifies output format but could include more examples.

- **Guardrails and boundaries**
  - Score: 4
  - Evidence: "Check whether the prompt contains safety limits..."
  - Comment: Includes safety limits but could expand on anti-hallucination rules.

- **Tool and environment usage**
  - Score: 4
  - Evidence: "Check whether the prompt tells the model what tools may be used..."
  - Comment: Provides guidance but could specify trusted data sources.

- **Efficiency and clarity**
  - Score: 3
  - Evidence: "Check whether the prompt is concise relative to its goals..."
  - Comment: Detailed but could be more concise in some sections.

### Reusable patterns
- Clear role definition and task objectives.
- Detailed decision frameworks for tool usage.
- Structured response guidelines with formatting instructions.

### Improvement recommendations
1. Include explicit few-shot examples or demonstrations.
2. Simplify instructions for better efficiency and clarity.
3. Expand on anti-hallucination rules and trusted data sources.
4. Provide more examples of output formats and reasoning guidance.

### Compact structured block
```json
{
  "file_path": "Anthropic/raw/claude-sonnet-4.6-raw.md",
  "overall_verdict": "strong",
  "top_strengths": [
    "Clear role definition and task objectives",
    "Detailed decision frameworks for tool usage",
    "Structured response guidelines with formatting instructions"
  ],
  "top_weaknesses": [
    "Lacks explicit few-shot examples",
    "Could be more concise in some sections",
    "Needs more explicit anti-hallucination rules"
  ],
  "recommended_actions": [
    "Include explicit few-shot examples",
    "Simplify instructions for clarity",
    "Expand on anti-hallucination rules"
  ]
}
```
```