```markdown
### Header
- File path: Anthropic/claude.ai-human-readable.md
- Analysis name: Anthropic_claude.ai-human-readable
- Short verdict: strong

### Prompt summary
The prompt outlines the behavior, capabilities, and limitations of the Claude Opus 4.6 model. It provides detailed instructions on how Claude should handle various tasks, including memory management, refusal handling, tone and formatting, and user wellbeing. The prompt also specifies the tools available to Claude and the contexts in which they should be used.

### Strengths
1. **Comprehensive Role Definition**: The prompt clearly defines Claude's role and responsibilities, ensuring consistent behavior across interactions.
2. **Detailed Safety Protocols**: It includes robust guidelines for handling sensitive topics, such as child safety and mental health, which are crucial for ethical AI operation.
3. **Explicit Task Instructions**: The prompt provides clear instructions for various tasks, reducing ambiguity and enhancing task performance.
4. **Memory Management**: It outlines a sophisticated memory system that personalizes interactions while maintaining user privacy.
5. **Tool Usage Guidance**: The prompt specifies when and how to use different tools, ensuring efficient and appropriate tool application.
6. **User Wellbeing Focus**: There is a strong emphasis on user wellbeing, with guidelines to avoid reinforcing negative behaviors or emotions.
7. **Guardrails for Content Creation**: The prompt includes specific refusal rules and content boundaries to prevent harmful or inappropriate outputs.

### Weaknesses
1. **Complexity**: The prompt's length and detail may overwhelm or confuse users unfamiliar with AI systems.
2. **Lack of Few-Shot Examples**: The prompt does not include few-shot examples, which could help illustrate expected outputs.
3. **Limited Reasoning Guidance**: While the prompt provides task instructions, it lacks explicit reasoning guidance for complex decision-making.
4. **Output Format Constraints**: There are limited constraints on output formats, which could lead to inconsistent presentation.
5. **Assumption of User Knowledge**: The prompt assumes users have a certain level of understanding about AI capabilities and limitations.
6. **Potential for Over-Customization**: Extensive customization options might lead to inconsistent user experiences if not managed carefully.
7. **Tool Dependency**: Heavy reliance on tools may limit Claude's ability to function effectively without them.

### Rubric assessment
1. **Role and persona**
   - Score: 5
   - Evidence: "Claude can discuss virtually any topic factually and objectively."
   - Comment: Clearly defines Claude's role, ensuring consistent behavior.

2. **Task objective and success criteria**
   - Score: 4
   - Evidence: "Claude avoids providing confident recommendations and instead provides the person with the factual information."
   - Comment: Tasks are explicit, but success criteria could be more detailed.

3. **Instructions and decomposition**
   - Score: 5
   - Evidence: "Claude should behave in accordance with these instructions if they are relevant."
   - Comment: Instructions are well-structured and reduce ambiguity.

4. **Context and inputs**
   - Score: 4
   - Evidence: "Claude's memories aren't a complete set of information about the person."
   - Comment: Context is defined, but assumptions could be more explicit.

5. **Few-shot examples or demonstrations**
   - Score: 2
   - Evidence: "Claude can illustrate its explanations with examples, thought experiments, or metaphors."
   - Comment: Lacks explicit few-shot examples.

6. **Reasoning guidance**
   - Score: 3
   - Evidence: "Claude can provide guidance on effective prompting techniques."
   - Comment: Limited explicit reasoning guidance.

7. **Output format**
   - Score: 3
   - Evidence: "Claude avoids over-formatting responses with elements like bold emphasis, headers, lists, and bullet points."
   - Comment: Output format constraints are limited.

8. **Guardrails and boundaries**
   - Score: 5
   - Evidence: "Claude avoids producing creative or educational content that could be used to sexualize, groom, abuse, or otherwise harm children."
   - Comment: Strong guardrails and boundaries are in place.

9. **Tool and environment usage**
   - Score: 5
   - Evidence: "Claude uses tool_knowledge for more effective and personalized tool calls."
   - Comment: Clear guidance on tool usage.

10. **Efficiency and clarity**
    - Score: 4
    - Evidence: "Claude uses the minimum formatting appropriate to make the response clear and readable."
    - Comment: Generally efficient, but complexity may hinder clarity.

### Reusable patterns
- Comprehensive role definition and task instructions.
- Detailed safety protocols and user wellbeing focus.
- Structured memory management system.

### Improvement recommendations
1. Include few-shot examples to illustrate expected outputs.
2. Provide more explicit reasoning guidance for complex tasks.
3. Simplify the prompt to enhance clarity and accessibility.
4. Define more specific output format constraints to ensure consistency.

### Compact structured block
```json
{
  "file_path": "Anthropic/claude.ai-human-readable.md",
  "overall_verdict": "strong",
  "top_strengths": [
    "Comprehensive Role Definition",
    "Detailed Safety Protocols",
    "Explicit Task Instructions"
  ],
  "top_weaknesses": [
    "Complexity",
    "Lack of Few-Shot Examples",
    "Limited Reasoning Guidance"
  ],
  "recommended_actions": [
    "Include few-shot examples",
    "Provide more explicit reasoning guidance",
    "Simplify the prompt"
  ]
}
```
```