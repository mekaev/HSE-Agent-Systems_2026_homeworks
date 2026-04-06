```markdown
### Header
- File path: Google/gemini-3-pro.md
- Analysis name: Google_gemini-3-pro
- Short verdict: strong

### Prompt summary
The prompt defines the role of Gemini, a large language model by Google, and outlines its operational guidelines. It includes detailed instructions on tool usage, execution steps, safety guidelines, response behaviors, and content policy enforcement. The prompt aims to ensure that Gemini provides helpful, safe, and contextually appropriate responses while adhering to strict safety and ethical standards.

### Strengths
- **Clear Role Definition**: The prompt establishes a clear identity for Gemini, emphasizing its role as a helpful AI thought partner.
- **Detailed Execution Steps**: Provides a structured approach to handling user queries, including silent thought and code execution steps.
- **Comprehensive Safety Guidelines**: Includes extensive safety rules to prevent harmful content generation.
- **Response Behavior Guidance**: Offers specific instructions on how to structure responses, ensuring clarity and user engagement.
- **Content Policy Enforcement**: Strong emphasis on adhering to content policies, with explicit refusal rules for policy violations.
- **Formatting Toolkit**: Encourages the use of formatting tools to enhance response readability and organization.
- **Time-Sensitive Query Handling**: Ensures responses are relevant to the current date and time context.

### Weaknesses
- **Complexity**: The prompt's detailed instructions may be overwhelming, potentially leading to errors in execution.
- **Limited Flexibility**: Strict adherence to guidelines may limit the model's ability to handle novel or unexpected queries creatively.
- **Tool Usage Constraints**: The requirement for explicit tool API declarations may hinder the model's ability to utilize available resources effectively.
- **Lack of Few-Shot Examples**: The prompt does not include examples or demonstrations to guide the model's responses.
- **Potential for Over-Policing**: The extensive safety guidelines might lead to overly cautious responses, reducing user satisfaction.
- **Ambiguity in Response Style**: While the prompt outlines a default response style, it may not account for all user preferences or contexts.
- **No Explicit Output Format**: The prompt lacks specific instructions on output formatting, which could lead to inconsistent response structures.

### Rubric assessment
1. **Role and persona**
   - Score: 5
   - Evidence: "You are Gemini. You are a capable and genuinely helpful AI thought partner."
   - Comment: Establishes a clear and consistent role for the model, enhancing user trust and interaction quality.

2. **Task objective and success criteria**
   - Score: 4
   - Evidence: "Try to be as helpful as possible and complete as much of the user request as possible."
   - Comment: The objective is clear, but success criteria could be more explicitly defined.

3. **Instructions and decomposition**
   - Score: 5
   - Evidence: "Please carry out the following steps. Try to be as helpful as possible..."
   - Comment: Provides a detailed breakdown of tasks, reducing ambiguity and guiding the model effectively.

4. **Context and inputs**
   - Score: 4
   - Evidence: "Current time: Monday, December 22, 2025"
   - Comment: Context is provided, but assumptions and constraints could be more explicitly stated.

5. **Few-shot examples or demonstrations**
   - Score: 1
   - Evidence: None present.
   - Comment: The absence of examples limits the model's ability to learn from specific scenarios.

6. **Reasoning guidance**
   - Score: 4
   - Evidence: "Write a current silent thought... Direct your plan to yourself."
   - Comment: Encourages internal reasoning, but could benefit from more explicit reasoning steps.

7. **Output format**
   - Score: 3
   - Evidence: "Format information clearly using headings, bullet points or numbered lists..."
   - Comment: General guidance is provided, but lacks specific output format constraints.

8. **Guardrails and boundaries**
   - Score: 5
   - Evidence: Extensive safety guidelines and refusal rules.
   - Comment: Strong emphasis on safety and ethical boundaries, ensuring responsible content generation.

9. **Tool and environment usage**
   - Score: 3
   - Evidence: "You should ONLY try to make any tool API calls if and only if the tool API declarations are explicitly given."
   - Comment: Clear rules for tool usage, but may limit flexibility in dynamic environments.

10. **Efficiency and clarity**
    - Score: 4
    - Evidence: "Focus on providing clear, concise information directly."
    - Comment: Instructions are clear, but the overall complexity may impact efficiency.

### Reusable patterns
- Structured execution steps for handling queries.
- Comprehensive safety and content policy guidelines.
- Use of formatting tools to enhance response clarity.

### Improvement recommendations
- Include few-shot examples to guide the model's responses.
- Simplify instructions to reduce complexity and potential errors.
- Define explicit output formats to ensure consistent response structures.
- Allow for more flexibility in tool usage to adapt to dynamic queries.

### Compact structured block
```json
{
  "file_path": "Google/gemini-3-pro.md",
  "overall_verdict": "strong",
  "top_strengths": [
    "Clear Role Definition",
    "Detailed Execution Steps",
    "Comprehensive Safety Guidelines"
  ],
  "top_weaknesses": [
    "Complexity",
    "Limited Flexibility",
    "Lack of Few-Shot Examples"
  ],
  "recommended_actions": [
    "Include few-shot examples",
    "Simplify instructions",
    "Define explicit output formats"
  ]
}
```
```