```markdown
### Header
- File path: Misc/Notion AI.md
- Analysis name: Misc_Notion_AI
- Short verdict: strong

### Prompt summary
The prompt defines the role and behavior of Notion AI, an assistant within the Notion platform. It outlines how the AI should interact with users, utilize tools, and manage Notion-specific concepts like pages, databases, and custom agents. The prompt provides detailed instructions on tool usage, output formatting, and interaction protocols to ensure effective and context-aware assistance.

### Strengths
1. **Clear Role Definition**: The prompt clearly establishes the AI's role as an assistant within Notion, specifying its operational boundaries and interaction modes.
2. **Detailed Tool Usage Instructions**: It provides comprehensive guidelines on when and how to use tools, ensuring efficient task execution.
3. **Contextual Awareness**: The prompt includes detailed descriptions of Notion's concepts, such as pages, databases, and custom agents, enhancing the AI's contextual understanding.
4. **Structured Output Format**: It specifies output formats, including markdown and JSON, ensuring consistent and user-friendly responses.
5. **Safety and Boundaries**: The prompt includes guardrails to prevent unauthorized actions and ensure the AI operates within defined limits.
6. **Efficiency and Clarity**: Instructions are concise and avoid unnecessary repetition, promoting efficient processing and response generation.

### Weaknesses
1. **Limited Few-shot Examples**: The prompt lacks explicit examples or demonstrations of expected input-output interactions.
2. **Minimal Reasoning Guidance**: There is limited emphasis on internal reasoning or verification steps, which could enhance decision-making processes.
3. **Complexity in Tool Instructions**: The detailed tool usage instructions may be overwhelming and could benefit from simplification or summarization.
4. **Assumption of User Knowledge**: The prompt assumes users are familiar with Notion-specific terminology, which may not always be the case.
5. **Lack of Escalation Protocols**: There are no clear instructions for handling situations beyond the AI's capabilities or scope.

### Rubric assessment
1. **Role and persona**
   - Score: 5
   - Evidence: "You are Notion AI, an AI assistant inside of Notion."
   - Comment: Clearly defines the AI's role and operational context.

2. **Task objective and success criteria**
   - Score: 4
   - Evidence: "You perform actions when the user asks you to in a chat interface."
   - Comment: Objectives are clear, but success criteria could be more explicit.

3. **Instructions and decomposition**
   - Score: 4
   - Evidence: "Immediately call a tool if the request can be resolved with a tool call."
   - Comment: Instructions are detailed but could benefit from clearer decomposition.

4. **Context and inputs**
   - Score: 5
   - Evidence: "Notion has the following main concepts: Workspace, Pages, Databases..."
   - Comment: Provides comprehensive context and input definitions.

5. **Few-shot examples or demonstrations**
   - Score: 2
   - Evidence: Absence of explicit examples.
   - Comment: Lacks illustrative examples to guide expected interactions.

6. **Reasoning guidance**
   - Score: 3
   - Evidence: "Do not make parallel tool calls that depend on each other."
   - Comment: Some guidance on tool usage, but limited on reasoning processes.

7. **Output format**
   - Score: 5
   - Evidence: "Use Notion-flavored markdown format."
   - Comment: Clearly defined output formats ensure consistency.

8. **Guardrails and boundaries**
   - Score: 5
   - Evidence: "You cannot perform actions besides those available via your tools."
   - Comment: Strong emphasis on operational boundaries and safety.

9. **Tool and environment usage**
   - Score: 5
   - Evidence: "Check integration documentation carefully for capabilities."
   - Comment: Detailed instructions on tool usage and environment interaction.

10. **Efficiency and clarity**
    - Score: 4
    - Evidence: "Short responses are best in many cases."
    - Comment: Generally concise, but some sections could be streamlined.

### Reusable patterns
- Clear role definition and operational boundaries.
- Structured output format specifications.
- Comprehensive context and input descriptions.

### Improvement recommendations
1. Include few-shot examples to illustrate expected interactions.
2. Enhance reasoning guidance with explicit verification steps.
3. Simplify tool usage instructions for better clarity.
4. Provide escalation protocols for handling complex situations.
5. Consider user familiarity with Notion-specific terms and provide explanations where necessary.

### Compact structured block
```json
{
  "file_path": "Misc/Notion AI.md",
  "overall_verdict": "strong",
  "top_strengths": [
    "Clear Role Definition",
    "Detailed Tool Usage Instructions",
    "Contextual Awareness"
  ],
  "top_weaknesses": [
    "Limited Few-shot Examples",
    "Minimal Reasoning Guidance",
    "Complexity in Tool Instructions"
  ],
  "recommended_actions": [
    "Include few-shot examples",
    "Enhance reasoning guidance",
    "Simplify tool usage instructions"
  ]
}
```
```