```markdown
### Header
- File path: Anthropic/raw/claude-opus-4.6-raw.md
- Analysis name: Anthropic_raw_claude-opus-4.6-raw
- Short verdict: strong

### Prompt summary
The prompt defines the role and capabilities of Claude, an AI assistant operating within Anthropic's chat interfaces. It provides detailed instructions on using tools to access past conversations, outlines trigger patterns for tool usage, and specifies guidelines for response formatting and tool selection. The prompt aims to enhance continuity and relevance in user interactions by leveraging historical chat data.

### Strengths
1. **Role and Persona Clarity**: The prompt clearly defines Claude's role as an assistant within specific interfaces, providing a strong foundation for consistent behavior.
2. **Detailed Tool Instructions**: Comprehensive guidelines for using past chat tools ensure accurate retrieval of historical data, enhancing response relevance.
3. **Trigger Pattern Identification**: The prompt effectively outlines explicit and implicit cues for tool activation, reducing the likelihood of missing context.
4. **Structured Decision Framework**: A clear decision framework guides tool selection, promoting efficient and contextually appropriate responses.
5. **Response Guidelines**: Detailed formatting and response guidelines help maintain a professional and user-friendly interaction style.
6. **Examples and Demonstrations**: The inclusion of diverse examples illustrates practical applications of the tools and guidelines, aiding understanding and implementation.
7. **Guardrails and Boundaries**: The prompt includes safety limits and refusal rules, ensuring responsible and ethical use of the assistant.

### Weaknesses
1. **Complexity and Length**: The prompt's detailed instructions may be overwhelming, potentially leading to cognitive overload for the model.
2. **Limited Flexibility**: Strict adherence to predefined patterns may limit the model's ability to adapt to novel or unexpected user inputs.
3. **Assumption of User Intent**: The reliance on trigger patterns assumes accurate interpretation of user intent, which may not always be the case.
4. **Potential for Over-Reliance on Tools**: Emphasis on tool usage might lead to over-reliance, potentially neglecting simpler, context-based responses.
5. **Lack of Few-Shot Examples**: While examples are provided, the absence of few-shot demonstrations for nuanced scenarios could limit adaptability.
6. **Minimal Reasoning Guidance**: The prompt lacks explicit instructions for stepwise reasoning or self-checks, which could enhance response accuracy.
7. **Output Format Constraints**: While output formatting is addressed, more explicit constraints on structure and length could improve consistency.

### Rubric assessment
1. **Role and persona**
   - Score: 5
   - Evidence: "The assistant is Claude, created by Anthropic."
   - Comment: Clearly defines the assistant's identity and operational context.

2. **Task objective and success criteria**
   - Score: 4
   - Evidence: "Use these tools when the user references past conversations..."
   - Comment: Task objectives are clear, but success criteria could be more explicit.

3. **Instructions and decomposition**
   - Score: 5
   - Evidence: "Check whether the prompt breaks the work into ordered steps..."
   - Comment: Instructions are well-structured and detailed.

4. **Context and inputs**
   - Score: 4
   - Evidence: "Claude has 2 tools to search past conversations."
   - Comment: Context is provided, but assumptions and constraints could be clearer.

5. **Few-shot examples or demonstrations**
   - Score: 3
   - Evidence: "Example 1: Explicit reference..."
   - Comment: Examples are present but lack few-shot demonstrations for complex scenarios.

6. **Reasoning guidance**
   - Score: 3
   - Evidence: "Do not ask the model to reveal hidden chain-of-thought."
   - Comment: Limited guidance on reasoning processes.

7. **Output format**
   - Score: 4
   - Evidence: "Always format chat links as a clickable link..."
   - Comment: Output formatting is addressed, but could be more detailed.

8. **Guardrails and boundaries**
   - Score: 5
   - Evidence: "Never claim lack of memory..."
   - Comment: Strong emphasis on safety and ethical guidelines.

9. **Tool and environment usage**
   - Score: 5
   - Evidence: "Claude has 2 tools to search past conversations."
   - Comment: Comprehensive instructions for tool usage.

10. **Efficiency and clarity**
    - Score: 4
    - Evidence: "Check whether the prompt is concise relative to its goals..."
    - Comment: Generally clear, but complexity may impact efficiency.

### Reusable patterns
- Trigger pattern identification for tool usage.
- Structured decision frameworks for task execution.
- Comprehensive response guidelines for maintaining interaction quality.

### Improvement recommendations
1. Simplify instructions to reduce cognitive load.
2. Incorporate few-shot examples for complex scenarios.
3. Enhance reasoning guidance with explicit stepwise instructions.
4. Clarify assumptions and constraints for context and inputs.
5. Define more explicit output format constraints for consistency.

### Compact structured block
```json
{
  "file_path": "Anthropic/raw/claude-opus-4.6-raw.md",
  "overall_verdict": "strong",
  "top_strengths": [
    "Role and persona clarity",
    "Detailed tool instructions",
    "Trigger pattern identification"
  ],
  "top_weaknesses": [
    "Complexity and length",
    "Limited flexibility",
    "Assumption of user intent"
  ],
  "recommended_actions": [
    "Simplify instructions",
    "Incorporate few-shot examples",
    "Enhance reasoning guidance"
  ]
}
```
```