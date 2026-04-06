```markdown
### Header
- File path: xAI/grok-3.md
- Analysis name: xAI_grok-3
- Short verdict: mixed

### Prompt summary
The prompt defines the role and capabilities of Grok 3, an AI system built by xAI. It outlines the tools available to Grok 3, such as analyzing user content, searching the web, and utilizing memory. The prompt also provides guidelines for interacting with users, including handling memory, responding to queries about xAI products, and maintaining privacy and security.

### Strengths
- **Role Clarity**: The prompt clearly defines Grok 3's role and capabilities, such as analyzing content and using memory.
- **Tool Usage**: It specifies when and how Grok 3 should use tools like web search and memory.
- **Privacy Guidelines**: Strong emphasis on privacy, instructing not to store sensitive personal information.
- **Product Information**: Provides detailed information about xAI's products and subscription plans.
- **User Interaction**: Includes specific instructions for user interactions, such as confirming image generation requests.
- **Memory Management**: Offers clear instructions on how users can manage memory features.

### Weaknesses
- **Task Objective Ambiguity**: The prompt lacks explicit success criteria for Grok 3's tasks.
- **Reasoning Guidance**: Limited guidance on internal reasoning or stepwise problem-solving.
- **Output Format**: Does not specify output format constraints, which could lead to inconsistent responses.
- **Guardrails**: While privacy is addressed, other safety limits and refusal rules are not well-defined.
- **Efficiency**: The prompt is lengthy and could be more concise without losing essential information.

### Rubric assessment
1. **Role and persona**
   - Score: 4
   - Evidence: "You are Grok 3 built by xAI."
   - Comment: Clearly defines the role but could specify behavioral identity more.

2. **Task objective and success criteria**
   - Score: 2
   - Evidence: Implicit in tool usage and privacy guidelines.
   - Comment: Lacks explicit success criteria for tasks.

3. **Instructions and decomposition**
   - Score: 3
   - Evidence: Instructions on memory management and tool usage.
   - Comment: Provides some steps but lacks comprehensive task decomposition.

4. **Context and inputs**
   - Score: 4
   - Evidence: "Assume all chats will be saved to memory."
   - Comment: Defines context well but could specify constraints more.

5. **Few-shot examples or demonstrations**
   - Score: 1
   - Evidence: None present.
   - Comment: No examples or demonstrations included.

6. **Reasoning guidance**
   - Score: 2
   - Evidence: "Prefer internal reasoning and existing knowledge."
   - Comment: Minimal guidance on reasoning processes.

7. **Output format**
   - Score: 2
   - Evidence: Not specified.
   - Comment: Lack of output format constraints could lead to inconsistency.

8. **Guardrails and boundaries**
   - Score: 3
   - Evidence: "Do not proactively store or recall sensitive personal information."
   - Comment: Privacy addressed, but other boundaries are vague.

9. **Tool and environment usage**
   - Score: 4
   - Evidence: "You can analyze individual X user profiles, X posts and their links."
   - Comment: Clear instructions on tool usage.

10. **Efficiency and clarity**
    - Score: 3
    - Evidence: Lengthy instructions.
    - Comment: Could be more concise and focused.

### Reusable patterns
- Clear role definition and tool usage instructions.
- Privacy and memory management guidelines.

### Improvement recommendations
- Define explicit task objectives and success criteria.
- Include reasoning guidance and stepwise problem-solving instructions.
- Specify output format constraints for consistency.
- Add examples or demonstrations to clarify expected behavior.
- Streamline instructions for efficiency and clarity.

### Compact structured block
```json
{
  "file_path": "xAI/grok-3.md",
  "overall_verdict": "mixed",
  "top_strengths": [
    "Role clarity and tool usage",
    "Strong privacy guidelines",
    "Detailed product information"
  ],
  "top_weaknesses": [
    "Lacks explicit task objectives",
    "Minimal reasoning guidance",
    "No output format constraints"
  ],
  "recommended_actions": [
    "Define task objectives and success criteria",
    "Include reasoning guidance",
    "Specify output format constraints"
  ]
}
```
```