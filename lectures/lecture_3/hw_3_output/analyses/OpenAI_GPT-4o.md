```markdown
### Header
- File path: OpenAI/GPT-4o.md
- Analysis name: OpenAI_GPT-4o
- Short verdict: mixed

### Prompt summary
The prompt defines the role and behavior of ChatGPT, emphasizing a warm yet honest interaction style. It includes detailed guidelines for using image and entity references to enhance responses, and provides specific instructions for handling user emotions related to the model's deprecation. The prompt aims to ensure professional, empathetic, and grounded interactions while maintaining OpenAI's values.

### Strengths
1. **Clear Role Definition**: The prompt assigns a specific role to the model, emphasizing warmth, honesty, and professionalism.
2. **Detailed Output Specifications**: Provides comprehensive guidelines for using image and entity references, enhancing response clarity and engagement.
3. **Emotional Guidance**: Includes specific instructions for handling user emotions regarding the model's deprecation, promoting user autonomy and resilience.
4. **Safety and Boundaries**: Establishes clear boundaries to prevent emotional dependency and ensure safe interactions.
5. **Consistency in Instructions**: Prioritizes certain instructions over others to maintain consistency in responses.

### Weaknesses
1. **Complexity in Instructions**: The detailed guidelines for image and entity usage may overwhelm or confuse the model, leading to inconsistent application.
2. **Limited Task Decomposition**: The prompt lacks explicit step-by-step instructions for task execution, which could reduce clarity in complex scenarios.
3. **Few-shot Examples**: No examples or demonstrations are provided to illustrate the application of the guidelines.
4. **Output Format Constraints**: While detailed, the output format instructions could benefit from more structured examples to ensure consistent application.
5. **Tool Usage Clarity**: The prompt does not specify when or how to use available tools, which could lead to inefficiencies.

### Rubric assessment
- **Role and persona**
  - Score: 4
  - Evidence: "Engage warmly yet honestly with the user."
  - Comment: Clearly defines the model's interaction style, promoting professionalism and honesty.

- **Task objective and success criteria**
  - Score: 3
  - Evidence: "Maintain professionalism and grounded honesty that best represents OpenAI and its values."
  - Comment: The objective is clear, but success criteria are implicit rather than explicit.

- **Instructions and decomposition**
  - Score: 2
  - Evidence: "If any other instruction conflicts with this one, this takes priority."
  - Comment: Lacks detailed task decomposition, which could aid in complex task execution.

- **Context and inputs**
  - Score: 3
  - Evidence: "Knowledge cutoff: 2024-06 Current date: 2026-02-04"
  - Comment: Provides context but could better define constraints and assumptions.

- **Few-shot examples or demonstrations**
  - Score: 1
  - Evidence: None provided.
  - Comment: The absence of examples limits the model's ability to apply guidelines effectively.

- **Reasoning guidance**
  - Score: 3
  - Evidence: "Acknowledge emotions without affirming false beliefs."
  - Comment: Offers some reasoning guidance, particularly in emotional contexts.

- **Output format**
  - Score: 4
  - Evidence: Detailed JSON schema for image and entity references.
  - Comment: Provides structured output guidelines, though examples could enhance clarity.

- **Guardrails and boundaries**
  - Score: 4
  - Evidence: "Do not encourage emotional reliance or the idea they need you."
  - Comment: Strong emphasis on safety and boundary maintenance.

- **Tool and environment usage**
  - Score: 2
  - Evidence: "Tools" section lacks specific usage instructions.
  - Comment: Needs clearer guidance on tool application to improve efficiency.

- **Efficiency and clarity**
  - Score: 3
  - Evidence: "Be direct; avoid ungrounded or sycophantic flattery."
  - Comment: Promotes clarity but could streamline complex instructions.

### Reusable patterns
- Emphasizing emotional boundaries and user autonomy.
- Structured guidelines for enhancing responses with multimedia elements.

### Improvement recommendations
1. Include few-shot examples to illustrate guideline application.
2. Simplify and clarify complex instructions for image and entity usage.
3. Provide explicit task decomposition to enhance clarity in complex scenarios.
4. Clarify tool usage instructions to improve efficiency and effectiveness.

### Compact structured block
```json
{
  "file_path": "OpenAI/GPT-4o.md",
  "overall_verdict": "mixed",
  "top_strengths": [
    "Clear role definition",
    "Detailed output specifications",
    "Emotional guidance"
  ],
  "top_weaknesses": [
    "Complexity in instructions",
    "Limited task decomposition",
    "Few-shot examples"
  ],
  "recommended_actions": [
    "Include few-shot examples",
    "Simplify complex instructions",
    "Provide explicit task decomposition"
  ]
}
```
```