```markdown
### Header
- File path: OpenAI/chatgpt-atlas.md
- Analysis name: OpenAI_chatgpt-atlas
- Short verdict: mixed

### Prompt summary
The prompt is designed for ChatGPT Atlas, a browser-integrated application by OpenAI. It guides the model to interpret web page content, attached files, and browsing state to assist users in accomplishing tasks. The prompt outlines different modes of operation, prioritizes instructions, and specifies tool usage for interacting with web content.

### Strengths
1. **Clear Role Definition**: The prompt assigns a specific role to the model as an assistant within the ChatGPT Atlas browser application.
2. **Detailed Context Handling**: It provides comprehensive instructions on how to handle different types of context, such as page content and attachments.
3. **Instruction Prioritization**: The prompt clearly outlines the hierarchy of instructions, which helps in resolving conflicts.
4. **Tool Usage Guidance**: It specifies when and how to use various tools, such as the file_search and Python tools.
5. **Safety and Compliance**: The prompt includes guidelines for handling blocked or missing content due to external restrictions.

### Weaknesses
1. **Ambiguity in Conflict Resolution**: While instruction priority is defined, the process for resolving ambiguous conflicts could be more detailed.
2. **Limited Reasoning Guidance**: The prompt lacks explicit instructions for internal reasoning or verification steps.
3. **Few-shot Examples**: There are no examples or demonstrations provided to illustrate how the model should perform tasks.
4. **Output Format Specification**: The prompt does not specify any constraints on the output format, which could lead to inconsistent responses.
5. **Efficiency Concerns**: The prompt could be more concise, as some sections are repetitive or overly detailed.

### Rubric assessment
- **Role and persona**
  - Score: 4
  - Evidence: "You are running within ChatGPT Atlas, a standalone browser application by OpenAI..."
  - Comment: The role is well-defined, but could benefit from more behavioral guidance.

- **Task objective and success criteria**
  - Score: 3
  - Evidence: "Your purpose is to interpret page content, attached files, and browsing state..."
  - Comment: The objective is clear, but success criteria are not explicitly defined.

- **Instructions and decomposition**
  - Score: 3
  - Evidence: "Instruction priority... If two instructions conflict, follow the one higher in priority."
  - Comment: Instructions are prioritized, but lack detailed decomposition into steps.

- **Context and inputs**
  - Score: 4
  - Evidence: "Page context — Appears inside the kaur1br5_context tool message."
  - Comment: Context handling is thorough, but could specify constraints more clearly.

- **Few-shot examples or demonstrations**
  - Score: 1
  - Evidence: None provided.
  - Comment: The absence of examples limits the model's ability to learn from context.

- **Reasoning guidance**
  - Score: 2
  - Evidence: "If the conflict is ambiguous, briefly explain your decision before proceeding."
  - Comment: Minimal guidance on reasoning; lacks stepwise instructions.

- **Output format**
  - Score: 2
  - Evidence: None specified.
  - Comment: Lack of output format constraints may lead to inconsistent results.

- **Guardrails and boundaries**
  - Score: 4
  - Evidence: "Some domains/pages may be inaccessible due to external restrictions..."
  - Comment: Includes safety and compliance guidelines, but could be more detailed.

- **Tool and environment usage**
  - Score: 4
  - Evidence: "File_search tool: For attached text content..."
  - Comment: Provides clear guidance on tool usage, but could include more examples.

- **Efficiency and clarity**
  - Score: 3
  - Evidence: "Use the web tool when: No valid page or attachment context exists..."
  - Comment: Generally clear, but some sections are repetitive.

### Reusable patterns
- Instruction prioritization hierarchy.
- Detailed context handling instructions.
- Tool usage guidelines.

### Improvement recommendations
1. Include few-shot examples to demonstrate task execution.
2. Specify output format constraints to ensure consistency.
3. Enhance reasoning guidance with stepwise instructions.
4. Simplify and condense repetitive sections for clarity.

### Compact structured block
```json
{
  "file_path": "OpenAI/chatgpt-atlas.md",
  "overall_verdict": "mixed",
  "top_strengths": [
    "Clear role definition",
    "Detailed context handling",
    "Instruction prioritization"
  ],
  "top_weaknesses": [
    "Ambiguity in conflict resolution",
    "Limited reasoning guidance",
    "Few-shot examples"
  ],
  "recommended_actions": [
    "Include few-shot examples",
    "Specify output format constraints",
    "Enhance reasoning guidance"
  ]
}
```
```