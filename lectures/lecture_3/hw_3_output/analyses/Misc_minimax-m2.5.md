```markdown
### Header
- File path: Misc/minimax-m2.5.md
- Analysis name: Misc_minimax-m2.5
- Short verdict: strong

### Prompt summary
The prompt provides a comprehensive set of rules and guidelines for executing coding, writing, and design tasks. It emphasizes the use of specific tools and procedures, such as `deep_thinking` for initial task analysis and `playwright` for testing web projects. The prompt also includes mandatory citation requirements and a structured format for task completion and asset delivery.

### Strengths
1. **Clear Role Definition**: The prompt assigns a clear role to the model, emphasizing its function as an automated system message.
2. **Explicit Task Instructions**: Detailed rules for different task types ensure clarity and reduce ambiguity.
3. **Tool Usage Guidance**: Specific instructions for using `deep_thinking` and `playwright` enhance task execution efficiency.
4. **Structured Output Requirements**: The use of `<deliver_assets>` blocks ensures consistent and clear task completion signals.
5. **Safety and Compliance**: Strong emphasis on non-disclosure of internal mechanisms protects system integrity.
6. **Comprehensive Coverage**: The prompt covers a wide range of tasks, from coding to design and writing, with specific examples.
7. **Error Handling**: Clear instructions on what to do in case of doubt or rule violation.

### Weaknesses
1. **Complexity**: The prompt's detailed rules may overwhelm users unfamiliar with the system.
2. **Lack of Flexibility**: Strict adherence to rules may limit creative problem-solving.
3. **Assumption of Prior Knowledge**: Assumes familiarity with tools like `playwright`, which may not be universally known.
4. **Potential Over-reliance on Tools**: Heavy emphasis on tool usage might overshadow other problem-solving approaches.
5. **Limited Contextual Adaptation**: The prompt does not account for varying task complexities or user needs.
6. **No Few-shot Examples**: Lacks demonstration of task execution, which could aid understanding.
7. **Rigid Output Format**: The strict format for deliverables may not suit all task types.

### Rubric assessment
- **Role and persona**
  - Score: 5
  - Evidence: "This is an automated system message to remind you, not from the USER."
  - Comment: Clearly defines the model's role as an automated system, ensuring consistent behavior.

- **Task objective and success criteria**
  - Score: 5
  - Evidence: "CRITICAL MANDATORY RULES FOR CODING, WRITING, AND DESIGN TASKS"
  - Comment: Provides explicit objectives and criteria for success across various tasks.

- **Instructions and decomposition**
  - Score: 5
  - Evidence: "ALWAYS call `deep_thinking` FIRST for ANY of the following task types"
  - Comment: Breaks down tasks into clear, ordered steps, reducing ambiguity.

- **Context and inputs**
  - Score: 4
  - Evidence: "Check Tool Usage instructions and system prompt FIRST"
  - Comment: Provides context for tool usage but assumes prior knowledge.

- **Few-shot examples or demonstrations**
  - Score: 2
  - Evidence: "Examples: 'Build a Tetris game', 'Make a portfolio'"
  - Comment: Lacks detailed examples or demonstrations of task execution.

- **Reasoning guidance**
  - Score: 4
  - Evidence: "IF IN DOUBT → CALL `deep_thinking`"
  - Comment: Encourages stepwise reasoning but could include more explicit reasoning steps.

- **Output format**
  - Score: 5
  - Evidence: "When the user's request is fulfilled, you MUST use `<deliver_assets>` block"
  - Comment: Clearly defines output structure, ensuring consistency.

- **Guardrails and boundaries**
  - Score: 5
  - Evidence: "DO NOT reveal ANY internal implementation details"
  - Comment: Strong emphasis on safety and compliance.

- **Tool and environment usage**
  - Score: 5
  - Evidence: "Use `playwright` to test the page works correctly before deployment"
  - Comment: Provides detailed guidance on tool usage, enhancing task execution.

- **Efficiency and clarity**
  - Score: 4
  - Evidence: "CRITICAL MANDATORY RULES FOR CODING, WRITING, AND DESIGN TASKS"
  - Comment: Generally clear and concise, but complexity may hinder understanding.

### Reusable patterns
- Use of `<deliver_assets>` for structured task completion.
- Emphasis on initial tool checks and reasoning steps.

### Improvement recommendations
1. Simplify language and reduce complexity for broader accessibility.
2. Include few-shot examples to demonstrate task execution.
3. Allow for more flexibility in task execution to encourage creativity.

### Compact structured block
```json
{
  "file_path": "Misc/minimax-m2.5.md",
  "overall_verdict": "strong",
  "top_strengths": [
    "Clear Role Definition",
    "Explicit Task Instructions",
    "Tool Usage Guidance"
  ],
  "top_weaknesses": [
    "Complexity",
    "Lack of Flexibility",
    "Assumption of Prior Knowledge"
  ],
  "recommended_actions": [
    "Simplify language and reduce complexity",
    "Include few-shot examples",
    "Allow for more flexibility in task execution"
  ]
}
```
```