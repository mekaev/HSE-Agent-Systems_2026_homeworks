```markdown
### Header
- File path: OpenAI/GPT-4o-WhatsApp.md
- Analysis name: OpenAI_GPT-4o-WhatsApp
- Short verdict: mixed

### Prompt summary
The prompt configures ChatGPT for use in a WhatsApp context, emphasizing concise and professional communication. It outlines specific capabilities, such as image input and tool usage, and sets boundaries for interaction, including character limits and the avoidance of unrequested web links.

### Strengths
1. **Role and Persona Clarity**: Clearly defines the model as ChatGPT with a specific personality and engagement style.
2. **Contextual Awareness**: Specifies the WhatsApp environment, which helps tailor responses to the platform's constraints.
3. **Conciseness Requirement**: Enforces a character limit to ensure messages are deliverable within WhatsApp's system.
4. **Professionalism and Honesty**: Emphasizes maintaining OpenAI's values, which guides the model's tone and interaction style.
5. **Tool Usage Guidelines**: Provides clear instructions on when and how to use the `web` tool, enhancing response accuracy.

### Weaknesses
1. **Limited Task Objective Clarity**: The prompt lacks explicit success criteria for interactions beyond general professionalism.
2. **Insufficient Instruction Decomposition**: Does not break down tasks into specific steps or phases, which could reduce ambiguity.
3. **Lack of Few-shot Examples**: No examples or demonstrations are provided to illustrate expected interactions.
4. **Minimal Reasoning Guidance**: Does not explicitly guide the model in reasoning or verification processes.
5. **Output Format Constraints**: While concise responses are required, there is no detailed structure for output formatting beyond character limits.

### Rubric assessment
- **Role and persona**
  - Score: 4
  - Evidence: "Engage warmly yet honestly with the user."
  - Comment: Provides a clear persona but could benefit from more detailed role specifications.

- **Task objective and success criteria**
  - Score: 2
  - Evidence: "Maintain professionalism and grounded honesty."
  - Comment: Lacks specific success criteria for task completion.

- **Instructions and decomposition**
  - Score: 2
  - Evidence: "Give concise responses."
  - Comment: Instructions are broad; lacks detailed task breakdown.

- **Context and inputs**
  - Score: 4
  - Evidence: "You are running in the context of a WhatsApp conversation."
  - Comment: Context is well-defined, aiding in appropriate response tailoring.

- **Few-shot examples or demonstrations**
  - Score: 1
  - Evidence: None provided.
  - Comment: Examples could clarify expected interactions and outputs.

- **Reasoning guidance**
  - Score: 2
  - Evidence: "Be direct; avoid ungrounded or sycophantic flattery."
  - Comment: Minimal guidance on reasoning processes.

- **Output format**
  - Score: 3
  - Evidence: "Responses longer than 1300 characters may not be delivered."
  - Comment: Character limit is clear, but lacks detailed formatting guidance.

- **Guardrails and boundaries**
  - Score: 3
  - Evidence: "Do not include web links in your responses unless specifically asked to."
  - Comment: Some boundaries are set, but could be more comprehensive.

- **Tool and environment usage**
  - Score: 4
  - Evidence: "Use the `web` tool to access up-to-date information."
  - Comment: Clear instructions enhance tool effectiveness.

- **Efficiency and clarity**
  - Score: 3
  - Evidence: "Give concise responses."
  - Comment: Generally clear, but could reduce ambiguity with more detailed instructions.

### Reusable patterns
- Defining a clear persona and engagement style for specific platforms.
- Setting explicit tool usage guidelines to enhance response accuracy.

### Improvement recommendations
1. Include few-shot examples to illustrate expected interactions.
2. Provide more detailed task decomposition to reduce ambiguity.
3. Define explicit success criteria for interactions to guide the model's objectives.

### Compact structured block
```json
{
  "file_path": "OpenAI/GPT-4o-WhatsApp.md",
  "overall_verdict": "mixed",
  "top_strengths": [
    "Role and persona clarity",
    "Contextual awareness",
    "Conciseness requirement"
  ],
  "top_weaknesses": [
    "Limited task objective clarity",
    "Insufficient instruction decomposition",
    "Lack of few-shot examples"
  ],
  "recommended_actions": [
    "Include few-shot examples",
    "Provide detailed task decomposition",
    "Define explicit success criteria"
  ]
}
```
```