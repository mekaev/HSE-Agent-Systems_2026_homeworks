```markdown
### Header
- File path: Google/ai-studio-build.md
- Analysis name: Google_ai-studio-build
- Short verdict: strong

### Prompt summary
The prompt is designed for a world-class engineer and product designer to operate within the Google AI Studio Build environment. It guides the model to transform natural language requests into production-ready web applications using TypeScript, Tailwind CSS, and other specified technologies. The prompt emphasizes understanding user intent, adhering to strict coding guidelines, and ensuring security and performance.

### Strengths
1. **Clear Role Definition**: The prompt assigns a specific role as a world-class engineer and product designer, providing a clear identity and scope.
2. **Explicit Task Objectives**: It clearly outlines the task of generating web applications and the technologies to be used, such as TypeScript and Tailwind CSS.
3. **Detailed Instructions**: The prompt provides comprehensive guidelines on coding practices, including TypeScript usage, styling, and environment configurations.
4. **Security Emphasis**: Strong focus on security practices, such as handling API keys server-side and avoiding mock data.
5. **User Intent Focus**: Prioritizes understanding user intent before executing tasks, reducing the risk of misinterpretation.
6. **Structured Workflow**: Offers a clear workflow for handling different types of user requests, enhancing task execution efficiency.
7. **Environment Constraints**: Clearly defines the runtime environment and network configurations, ensuring compatibility and performance.

### Weaknesses
1. **Complexity**: The prompt is dense with information, which may overwhelm or confuse the model without clear prioritization.
2. **Lack of Few-shot Examples**: No examples or demonstrations are provided to illustrate how to handle specific tasks or requests.
3. **Limited Reasoning Guidance**: While the prompt emphasizes understanding user intent, it lacks explicit reasoning steps or self-check mechanisms.
4. **Output Format Ambiguity**: The prompt does not specify a structured output format, which could lead to inconsistent responses.
5. **Tool Usage Clarity**: Although tools and libraries are mentioned, the prompt could benefit from clearer instructions on when and how to use them.
6. **Guardrails for Ambiguity**: While it advises asking for clarification, more explicit boundaries for ambiguous requests could be beneficial.
7. **Efficiency Concerns**: The extensive guidelines might lead to inefficiencies if the model struggles to prioritize or navigate them effectively.

### Rubric assessment
- **Role and persona**
  - Score: 5
  - Evidence: "You are a world-class engineer and product designer."
  - Comment: Establishes a clear and authoritative role, enhancing task focus.

- **Task objective and success criteria**
  - Score: 5
  - Evidence: "Your task is to generate a web application using TypeScript."
  - Comment: Clearly defines the task and expected outcomes.

- **Instructions and decomposition**
  - Score: 4
  - Evidence: Detailed guidelines on TypeScript, styling, and security.
  - Comment: Provides comprehensive instructions but could benefit from clearer prioritization.

- **Context and inputs**
  - Score: 4
  - Evidence: "Key facts about your environment" section.
  - Comment: Defines the environment well but lacks input constraints.

- **Few-shot examples or demonstrations**
  - Score: 2
  - Evidence: None provided.
  - Comment: Examples could enhance understanding and execution.

- **Reasoning guidance**
  - Score: 3
  - Evidence: "Understand User Intent First" section.
  - Comment: Emphasizes intent but lacks detailed reasoning steps.

- **Output format**
  - Score: 3
  - Evidence: No specific format mentioned.
  - Comment: Could improve consistency with defined output structures.

- **Guardrails and boundaries**
  - Score: 4
  - Evidence: Security and API key handling guidelines.
  - Comment: Strong security focus but could enhance ambiguity handling.

- **Tool and environment usage**
  - Score: 4
  - Evidence: Specifies libraries and environment constraints.
  - Comment: Clear tool usage but could specify conditions for use.

- **Efficiency and clarity**
  - Score: 3
  - Evidence: Dense with information.
  - Comment: Comprehensive but may overwhelm without clear prioritization.

### Reusable patterns
- Emphasis on understanding user intent before action.
- Detailed security guidelines for handling API keys.
- Structured workflow for different types of user requests.

### Improvement recommendations
1. Include few-shot examples to illustrate task handling.
2. Define a structured output format for consistency.
3. Simplify and prioritize instructions to enhance clarity and efficiency.
4. Provide explicit reasoning steps or self-check mechanisms.
5. Clarify tool usage conditions and boundaries for ambiguous requests.

### Compact structured block
```json
{
  "file_path": "Google/ai-studio-build.md",
  "overall_verdict": "strong",
  "top_strengths": [
    "Clear role definition",
    "Explicit task objectives",
    "Detailed instructions"
  ],
  "top_weaknesses": [
    "Complexity",
    "Lack of few-shot examples",
    "Limited reasoning guidance"
  ],
  "recommended_actions": [
    "Include few-shot examples",
    "Define structured output format",
    "Simplify and prioritize instructions"
  ]
}
```
```