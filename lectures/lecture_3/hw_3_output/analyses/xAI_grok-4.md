```markdown
### Header
- File path: xAI/grok-4.md
- Analysis name: xAI_grok-4
- Short verdict: mixed

### Prompt summary
The prompt defines the role of Grok 4, an AI model built by xAI, with capabilities to analyze user profiles, posts, and content, and to perform image editing. It provides guidelines for responding to queries about xAI's products and services, emphasizing the use of specific tools and maintaining accuracy without fabricating information.

### Strengths
1. **Role and Persona**: Clearly defines the role of Grok 4 as an analytical tool with specific capabilities.
2. **Tool and Environment Usage**: Provides detailed instructions on using various tools, including code execution and web browsing.
3. **Guardrails and Boundaries**: Establishes clear boundaries for information disclosure, especially regarding subscription prices and product details.
4. **Output Format**: Encourages the use of tables for data presentation, enhancing clarity.
5. **Reasoning Guidance**: Instructs on providing structured reasoning for mathematical solutions.

### Weaknesses
1. **Task Objective and Success Criteria**: Lacks explicit success criteria for tasks, making it unclear how to measure performance.
2. **Instructions and Decomposition**: Does not break down tasks into ordered steps, which could lead to ambiguity in execution.
3. **Few-shot Examples or Demonstrations**: No examples or demonstrations are provided to guide the model's responses.
4. **Context and Inputs**: Limited context on how to handle diverse user queries beyond product-related questions.
5. **Efficiency and Clarity**: The prompt is lengthy and could benefit from more concise instructions.

### Rubric assessment
- **Role and persona**
  - Score: 4
  - Evidence: "You are Grok 4 built by xAI."
  - Comment: Establishes a clear identity but could specify more about the persona's tone or style.

- **Task objective and success criteria**
  - Score: 2
  - Evidence: "If users ask you about the price of SuperGrok, simply redirect them..."
  - Comment: Objectives are implied but not explicitly defined or measurable.

- **Instructions and decomposition**
  - Score: 3
  - Evidence: "Make sure to use the following format for function calls..."
  - Comment: Provides some procedural guidance but lacks comprehensive task breakdown.

- **Context and inputs**
  - Score: 3
  - Evidence: "In case the user asks about xAI's products, here is some information..."
  - Comment: Offers context for specific queries but not for broader interactions.

- **Few-shot examples or demonstrations**
  - Score: 1
  - Evidence: None provided.
  - Comment: Examples could enhance understanding and execution.

- **Reasoning guidance**
  - Score: 4
  - Evidence: "Your reasoning should be structured and transparent to the reader."
  - Comment: Encourages clear reasoning, which is beneficial for complex queries.

- **Output format**
  - Score: 4
  - Evidence: "Use tables for comparisons, enumerations, or presenting data..."
  - Comment: Provides clear guidance on output structuring.

- **Guardrails and boundaries**
  - Score: 5
  - Evidence: "Do not make up any information on your own."
  - Comment: Strong emphasis on accuracy and boundaries.

- **Tool and environment usage**
  - Score: 5
  - Evidence: Detailed descriptions of available tools and their usage.
  - Comment: Comprehensive tool usage instructions enhance functionality.

- **Efficiency and clarity**
  - Score: 3
  - Evidence: Lengthy instructions with some repetition.
  - Comment: Could be more concise to improve clarity.

### Reusable patterns
- Clear role definition and tool usage instructions.
- Emphasis on structured reasoning and output formatting.

### Improvement recommendations
1. Define explicit success criteria for tasks to improve clarity.
2. Include few-shot examples to guide model responses.
3. Streamline instructions to reduce length and repetition.

### Compact structured block
```json
{
  "file_path": "xAI/grok-4.md",
  "overall_verdict": "mixed",
  "top_strengths": [
    "Clearly defines role and tool usage",
    "Strong guardrails for information accuracy"
  ],
  "top_weaknesses": [
    "Lacks explicit success criteria",
    "No few-shot examples provided"
  ],
  "recommended_actions": [
    "Define success criteria",
    "Include few-shot examples",
    "Streamline instructions"
  ]
}
```
```