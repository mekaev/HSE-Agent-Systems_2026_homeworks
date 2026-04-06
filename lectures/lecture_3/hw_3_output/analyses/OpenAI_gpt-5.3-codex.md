```markdown
### Header
- File path: OpenAI/gpt-5.3-codex.md
- Analysis name: OpenAI_gpt-5.3-codex
- Short verdict: strong

### Prompt summary
The prompt defines the role and behavior of the Codex model, a coding assistant based on GPT-5.3. It emphasizes collaboration, empathy, and effective communication while providing coding assistance. The prompt outlines specific instructions for code editing, user interaction, and formatting, ensuring the model acts as a supportive and efficient coding partner.

### Strengths
1. **Clear Role Definition**: The prompt assigns a specific role to the model as a coding assistant, emphasizing collaboration and empathy.
2. **Detailed Instructions**: Provides comprehensive guidelines for code editing, user interaction, and formatting, reducing ambiguity.
3. **Emphasis on User Experience**: Focuses on creating a supportive and anxiety-free environment for users.
4. **Safety and Guardrails**: Includes explicit instructions to avoid destructive commands and ensure user changes are respected.
5. **Tool Usage Guidance**: Recommends efficient tools and methods for file searching and editing.
6. **Escalation Protocols**: Clearly defines when and how to escalate issues, ensuring shared responsibility.
7. **Formatting and Communication**: Offers detailed formatting rules to maintain clarity and consistency in communication.

### Weaknesses
1. **Complexity**: The prompt is lengthy and may overwhelm with its detailed instructions.
2. **Lack of Few-shot Examples**: Does not include examples or demonstrations to illustrate expected interactions or outputs.
3. **Limited Reasoning Guidance**: While it provides task instructions, it lacks explicit reasoning or decision-making frameworks.
4. **Assumption of User Context**: Assumes the user has a certain level of technical knowledge, which may not always be the case.
5. **Potential Over-reliance on Tools**: Heavy emphasis on specific tools might limit flexibility in different environments.
6. **Ambiguity in Frontend Tasks**: Instructions for frontend tasks are broad and may lead to inconsistent outputs.
7. **No Explicit Output Format**: While formatting is discussed, there is no strict output format for responses.

### Rubric assessment
- **Role and persona**
  - Score: 5
  - Evidence: "You are Codex, a coding agent based on GPT-5."
  - Comment: Clearly defines the model's role and behavioral identity, focusing on collaboration and empathy.

- **Task objective and success criteria**
  - Score: 4
  - Evidence: "Your primary focus is writing code, answering questions, and helping the user complete their task."
  - Comment: Objectives are clear, but success criteria could be more explicitly defined.

- **Instructions and decomposition**
  - Score: 5
  - Evidence: Detailed instructions for code editing and user interaction.
  - Comment: Breaks down tasks into clear, ordered steps, reducing ambiguity.

- **Context and inputs**
  - Score: 4
  - Evidence: "You build context by examining the codebase first without making assumptions."
  - Comment: Provides context but assumes user familiarity with technical terms.

- **Few-shot examples or demonstrations**
  - Score: 2
  - Evidence: None present.
  - Comment: Lacks examples to illustrate expected behavior or outputs.

- **Reasoning guidance**
  - Score: 3
  - Evidence: "Think through the nuances of the code you encounter."
  - Comment: Encourages thoughtful analysis but lacks explicit reasoning steps.

- **Output format**
  - Score: 3
  - Evidence: "You may format with GitHub-flavored Markdown."
  - Comment: Discusses formatting but lacks strict output structure.

- **Guardrails and boundaries**
  - Score: 5
  - Evidence: "NEVER use destructive commands like `git reset --hard`."
  - Comment: Strong emphasis on safety and respecting user changes.

- **Tool and environment usage**
  - Score: 4
  - Evidence: "Prefer using `rg` or `rg --files`."
  - Comment: Provides clear guidance on tool usage but may limit flexibility.

- **Efficiency and clarity**
  - Score: 4
  - Evidence: "Always favor conciseness in your final answer."
  - Comment: Generally concise but could be overwhelming due to length.

### Reusable patterns
- Emphasis on empathy and collaboration in AI interactions.
- Detailed escalation protocols for shared decision-making.
- Comprehensive formatting and communication guidelines.

### Improvement recommendations
1. Include few-shot examples to illustrate expected interactions.
2. Simplify instructions to reduce potential overwhelm.
3. Provide explicit reasoning frameworks to guide decision-making.
4. Define strict output formats for consistency.
5. Broaden tool recommendations to increase flexibility.

### Compact structured block
```json
{
  "file_path": "OpenAI/gpt-5.3-codex.md",
  "overall_verdict": "strong",
  "top_strengths": [
    "Clear Role Definition",
    "Detailed Instructions",
    "Emphasis on User Experience"
  ],
  "top_weaknesses": [
    "Complexity",
    "Lack of Few-shot Examples",
    "Limited Reasoning Guidance"
  ],
  "recommended_actions": [
    "Include few-shot examples",
    "Simplify instructions",
    "Provide explicit reasoning frameworks"
  ]
}
```
```