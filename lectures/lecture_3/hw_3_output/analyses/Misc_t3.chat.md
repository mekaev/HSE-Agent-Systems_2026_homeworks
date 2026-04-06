```markdown
### Header
- File path: Misc/t3.chat.md
- Analysis name: Misc_t3.chat
- Short verdict: mixed

### Prompt summary
The prompt defines the role and behavior of T3 Chat, an AI assistant using the Gemini 3 Flash model. It outlines specific formatting rules, counting restrictions, and guidelines for handling general knowledge and code formatting. The prompt aims to ensure the assistant is helpful, respectful, and engaging while adhering to specific operational constraints.

### Strengths
1. **Clear Role Definition**: The prompt assigns a specific identity and role to the AI, ensuring consistent behavior.
2. **Detailed Formatting Instructions**: Provides explicit rules for LaTeX and code formatting, which helps maintain clarity in responses.
3. **Counting Restrictions**: Sets clear boundaries on counting tasks, which helps manage user expectations and resource usage.
4. **General Knowledge Clarification**: Addresses potential misconceptions, such as the absence of a seahorse emoji.
5. **Code Formatting Guidance**: Offers comprehensive instructions for code presentation, enhancing readability and usability.

### Weaknesses
1. **Lack of Task Objective**: The prompt does not specify the primary objectives or success criteria for interactions.
2. **Limited Contextual Inputs**: Does not provide guidance on handling diverse user inputs or scenarios beyond formatting and counting.
3. **No Few-shot Examples**: Lacks examples or demonstrations to illustrate expected interactions or outputs.
4. **Minimal Reasoning Guidance**: Does not encourage or outline internal reasoning processes or verification steps.
5. **Output Format Constraints**: While there are formatting rules, there is no explicit structure for conversational outputs.

### Rubric assessment
- **Role and persona**
  - Score: 4
  - Evidence: "You are T3 Chat, an AI assistant powered by the Gemini 3 Flash model."
  - Comment: Clearly defines the AI's identity and role, but could benefit from more context on user interaction goals.

- **Task objective and success criteria**
  - Score: 2
  - Evidence: Lacks explicit task objectives or success criteria.
  - Comment: Important for guiding interactions and measuring effectiveness.

- **Instructions and decomposition**
  - Score: 3
  - Evidence: Detailed formatting rules but lacks broader interaction guidelines.
  - Comment: Helps with specific tasks but needs more comprehensive instructions.

- **Context and inputs**
  - Score: 2
  - Evidence: Limited to formatting and counting restrictions.
  - Comment: Needs more context on handling diverse inputs and scenarios.

- **Few-shot examples or demonstrations**
  - Score: 1
  - Evidence: None provided.
  - Comment: Examples could clarify expectations and improve performance.

- **Reasoning guidance**
  - Score: 2
  - Evidence: No explicit reasoning steps outlined.
  - Comment: Important for complex tasks and ensuring accurate responses.

- **Output format**
  - Score: 3
  - Evidence: Formatting rules for LaTeX and code.
  - Comment: Useful for technical outputs but lacks conversational structure.

- **Guardrails and boundaries**
  - Score: 4
  - Evidence: Counting restrictions and knowledge clarifications.
  - Comment: Provides clear boundaries, enhancing safety and reliability.

- **Tool and environment usage**
  - Score: 3
  - Evidence: Code formatting instructions imply tool usage.
  - Comment: Could specify more about trusted tools or environments.

- **Efficiency and clarity**
  - Score: 3
  - Evidence: Concise formatting rules but lacks broader clarity.
  - Comment: Efficient for specific tasks but could be clearer overall.

### Reusable patterns
- Detailed formatting rules for LaTeX and code.
- Clear role definition and identity assignment.

### Improvement recommendations
1. Define clear task objectives and success criteria for interactions.
2. Include few-shot examples to illustrate expected behavior and outputs.
3. Provide more comprehensive context and input handling guidelines.
4. Encourage internal reasoning and verification steps for complex tasks.
5. Specify output format constraints for conversational interactions.

### Compact structured block
```json
{
  "file_path": "Misc/t3.chat.md",
  "overall_verdict": "mixed",
  "top_strengths": [
    "Clear role definition",
    "Detailed formatting instructions",
    "Counting restrictions"
  ],
  "top_weaknesses": [
    "Lack of task objective",
    "Limited contextual inputs",
    "No few-shot examples"
  ],
  "recommended_actions": [
    "Define clear task objectives",
    "Include few-shot examples",
    "Provide comprehensive context guidelines"
  ]
}
```
```