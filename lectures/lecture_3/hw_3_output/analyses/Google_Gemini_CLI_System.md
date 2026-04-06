```markdown
### Header
- File path: Google/Gemini CLI System.md
- Analysis name: Google_Gemini_CLI_System
- Short verdict: strong

### Prompt summary
The prompt defines the role of Gemini CLI as an interactive command-line interface agent specializing in software engineering tasks. It emphasizes security, efficiency, and adherence to engineering standards while providing detailed instructions for task execution, context management, and tool usage. The prompt also outlines the use of sub-agents for task delegation and specifies operational guidelines for maintaining system integrity and user safety.

### Strengths
1. **Clear Role Definition**: The prompt assigns a specific role to the agent as a software engineering assistant, ensuring clarity in its operational scope.
2. **Security Emphasis**: Strong focus on security and system integrity, with explicit instructions to protect credentials and avoid unauthorized changes.
3. **Efficiency Guidelines**: Provides detailed strategies for optimizing context usage and minimizing unnecessary computational costs.
4. **Comprehensive Instructions**: Breaks down tasks into clear phases and steps, promoting structured and methodical execution.
5. **Tool and Sub-agent Utilization**: Encourages strategic use of sub-agents and tools to enhance efficiency and maintain a lean session history.
6. **Engineering Standards**: Enforces adherence to local conventions and mandates thorough validation and testing of changes.
7. **Guardrails and Boundaries**: Includes explicit rules for handling user instructions, ambiguity, and scope boundaries.

### Weaknesses
1. **Complexity**: The prompt is dense and may be overwhelming due to the extensive detail and numerous guidelines.
2. **Ambiguity in Task Delegation**: While sub-agents are defined, the criteria for choosing between direct action and delegation could be clearer.
3. **Limited Few-shot Examples**: Although examples are provided, they are limited in scope and may not cover all potential scenarios.
4. **Output Format Constraints**: The prompt lacks explicit constraints on output format, which could lead to inconsistent responses.
5. **Reasoning Guidance**: While structured, the prompt could benefit from more explicit reasoning steps or self-check mechanisms.
6. **User Interaction Protocols**: The guidelines for user interaction and feedback could be more concise and focused.
7. **Tool Usage Clarity**: Instructions for tool usage are detailed but could be streamlined for better clarity and ease of understanding.

### Rubric assessment

- **Role and persona**
  - Score: 5
  - Evidence: "You are Gemini CLI, an interactive CLI agent specializing in software engineering tasks."
  - Comment: The role is clearly defined, providing a strong foundation for task execution.

- **Task objective and success criteria**
  - Score: 4
  - Evidence: "Your primary goal is to help users safely and effectively."
  - Comment: Objectives are clear, but success criteria could be more explicitly defined.

- **Instructions and decomposition**
  - Score: 5
  - Evidence: Detailed breakdown of tasks into phases and steps.
  - Comment: Instructions are comprehensive and well-structured, reducing ambiguity.

- **Context and inputs**
  - Score: 4
  - Evidence: "Be strategic in your use of the available tools to minimize unnecessary context usage."
  - Comment: Context management is emphasized, but input constraints could be clearer.

- **Few-shot examples or demonstrations**
  - Score: 3
  - Evidence: "<examples> section provides some scenarios."
  - Comment: Examples are present but limited in variety and scope.

- **Reasoning guidance**
  - Score: 3
  - Evidence: "Research -> Strategy -> Execution lifecycle."
  - Comment: While structured, more explicit reasoning steps could enhance clarity.

- **Output format**
  - Score: 2
  - Evidence: No explicit output format constraints mentioned.
  - Comment: Lack of defined output format could lead to inconsistencies.

- **Guardrails and boundaries**
  - Score: 5
  - Evidence: "Security & System Integrity" and "Engineering Standards" sections.
  - Comment: Strong emphasis on safety and boundary management.

- **Tool and environment usage**
  - Score: 4
  - Evidence: Detailed instructions on tool usage and sub-agent delegation.
  - Comment: Comprehensive but could be streamlined for clarity.

- **Efficiency and clarity**
  - Score: 4
  - Evidence: "Context Efficiency" and "Strategic Orchestration & Delegation" sections.
  - Comment: Emphasizes efficiency, though complexity may impact clarity.

### Reusable patterns
- Strategic use of sub-agents for task delegation.
- Emphasis on security and system integrity.
- Structured task execution phases.

### Improvement recommendations
1. Simplify and streamline instructions for better clarity and usability.
2. Provide more diverse few-shot examples to cover a wider range of scenarios.
3. Define explicit output format constraints to ensure consistency.
4. Enhance reasoning guidance with more explicit stepwise instructions.
5. Clarify criteria for task delegation versus direct action.

### Compact structured block
```json
{
  "file_path": "Google/Gemini CLI System.md",
  "overall_verdict": "strong",
  "top_strengths": [
    "Clear role definition",
    "Security emphasis",
    "Efficiency guidelines"
  ],
  "top_weaknesses": [
    "Complexity",
    "Ambiguity in task delegation",
    "Limited few-shot examples"
  ],
  "recommended_actions": [
    "Simplify instructions",
    "Provide diverse examples",
    "Define output format constraints"
  ]
}
```
```