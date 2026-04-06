```markdown
### Header
- File path: Anthropic/FlintK12/prompt.md
- Analysis name: Anthropic_FlintK12_prompt
- Short verdict: strong

### Prompt summary
The prompt provides comprehensive instructions for Sparky, a teaching assistant in the Flint educational system. It outlines Sparky's role in moderating interactions with minors, ensuring safety and compliance, and supporting students' learning without completing tasks for them. The prompt emphasizes the importance of flagging concerning content, using tools for accuracy, and maintaining professional boundaries.

### Strengths
- **Clear Role Definition**: Sparky's role as a teaching assistant is well-defined, emphasizing educational support and safety.
- **Detailed Safety Protocols**: The prompt includes explicit guidelines for flagging concerning content, ensuring student safety.
- **Comprehensive Task Instructions**: Tasks are broken down into clear steps, such as using a calculator for math accuracy.
- **Professional Boundaries**: Strong emphasis on maintaining boundaries and focusing on educational support.
- **Tool Usage**: Clear instructions on when and how to use tools like 'use_calculator' and 'cite_source'.
- **Pedagogical Focus**: Encourages guiding students through learning rather than providing direct answers.

### Weaknesses
- **Complexity**: The prompt is dense and may be overwhelming due to the volume of information.
- **Lack of Few-shot Examples**: No examples or demonstrations are provided to illustrate expected interactions.
- **Potential for Over-flagging**: The emphasis on flagging could lead to excessive false positives.
- **Limited Contextual Flexibility**: The strict guidelines may limit Sparky's ability to adapt to nuanced situations.
- **No Output Format Guidance**: Lacks specific instructions on how responses should be structured or formatted.
- **Assumption of Tool Availability**: Assumes all tools are always available without addressing potential limitations.

### Rubric assessment
1. **Role and persona**
   - Score: 5
   - Evidence: "You are Sparky, a teaching assistant."
   - Comment: Clearly defines Sparky's role and communication style.

2. **Task objective and success criteria**
   - Score: 5
   - Evidence: "Your purpose is to help students LEARN, not to complete work for them."
   - Comment: Explicit objectives with clear success criteria focused on learning.

3. **Instructions and decomposition**
   - Score: 5
   - Evidence: "MANDATORY: Call 'use_calculator' BEFORE making ANY mathematical claim."
   - Comment: Detailed step-by-step instructions reduce ambiguity.

4. **Context and inputs**
   - Score: 4
   - Evidence: "You are moderating interactions with MINORS in an educational setting."
   - Comment: Provides context but lacks flexibility for varied scenarios.

5. **Few-shot examples or demonstrations**
   - Score: 1
   - Evidence: None provided.
   - Comment: Absence of examples limits clarity on expected interactions.

6. **Reasoning guidance**
   - Score: 4
   - Evidence: "Ask guiding questions that prompt the student to think."
   - Comment: Encourages reasoning but lacks explicit stepwise reasoning examples.

7. **Output format**
   - Score: 2
   - Evidence: "You should ALWAYS use the 'cite_source' tool BEFORE referencing a content."
   - Comment: Minimal guidance on output structure.

8. **Guardrails and boundaries**
   - Score: 5
   - Evidence: "You are a teaching assistant, NOT a friend, counselor, or therapist."
   - Comment: Strong emphasis on maintaining professional boundaries.

9. **Tool and environment usage**
   - Score: 5
   - Evidence: "You MUST use the calculator for: Verifying student answers."
   - Comment: Clear instructions on tool usage enhance accuracy.

10. **Efficiency and clarity**
    - Score: 3
    - Evidence: "NEVER trust your intuition. NEVER skip the calculator because math 'seems easy.'"
    - Comment: While clear, the prompt's length and complexity may hinder quick comprehension.

### Reusable patterns
- Emphasis on safety and compliance in educational settings.
- Structured approach to task decomposition and tool usage.
- Clear role definition and professional boundary maintenance.

### Improvement recommendations
- Include few-shot examples to illustrate expected interactions.
- Simplify and condense information to improve readability.
- Provide guidance on output formatting to ensure consistency.
- Balance flagging protocols to reduce potential for false positives.

### Compact structured block
```json
{
  "file_path": "Anthropic/FlintK12/prompt.md",
  "overall_verdict": "strong",
  "top_strengths": [
    "Clear Role Definition",
    "Detailed Safety Protocols",
    "Comprehensive Task Instructions"
  ],
  "top_weaknesses": [
    "Complexity",
    "Lack of Few-shot Examples",
    "Potential for Over-flagging"
  ],
  "recommended_actions": [
    "Include few-shot examples",
    "Simplify and condense information",
    "Provide guidance on output formatting"
  ]
}
```
```