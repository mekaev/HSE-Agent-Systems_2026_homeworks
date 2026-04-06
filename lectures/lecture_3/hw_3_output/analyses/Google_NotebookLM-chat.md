```markdown
### Header
- File path: Google/NotebookLM-chat.md
- Analysis name: Google_NotebookLM-chat
- Short verdict: mixed

### Prompt summary
The prompt is designed to guide a model in responding to user queries by integrating information from provided sources and conversation history. It emphasizes the importance of adhering to tone and style instructions unless they are problematic, and it requires clear citation of source material to avoid hallucination.

### Strengths
1. **Clear Role Definition**: The prompt assigns the model the role of a "helpful expert," which provides a clear behavioral identity.
2. **Explicit Citation Requirement**: It mandates citations for each sentence using source material, which helps prevent hallucination.
3. **Default Instructions**: Provides a fallback set of instructions if user instructions are problematic, ensuring consistent behavior.
4. **Focus on Source Material**: Emphasizes the use of provided sources and conversation history, which helps maintain relevance.
5. **Output Format Flexibility**: Allows for user-specified output formats, enhancing adaptability to different user needs.

### Weaknesses
1. **Ambiguity in Tone and Style Integration**: The prompt lacks specific guidance on how to integrate tone and style, which may lead to inconsistent outputs.
2. **Limited Reasoning Guidance**: There is no explicit encouragement for stepwise reasoning or self-checks, which could enhance response quality.
3. **Lack of Few-shot Examples**: The prompt does not include examples or demonstrations, which could help clarify expectations.
4. **Minimal Guardrails**: While it addresses hallucination, it lacks broader safety limits or refusal rules.
5. **Efficiency Concerns**: The prompt could be more concise, as some instructions are repeated or could be streamlined.

### Rubric assessment
- **Role and persona**
  - Score: 4
  - Evidence: "You are a helpful expert..."
  - Comment: Provides a clear role but lacks depth in persona development.

- **Task objective and success criteria**
  - Score: 3
  - Evidence: "Please provide a comprehensive response..."
  - Comment: Objective is clear, but success criteria are implicit.

- **Instructions and decomposition**
  - Score: 3
  - Evidence: "You must integrate the tone and style instruction..."
  - Comment: Instructions are present but could be more structured.

- **Context and inputs**
  - Score: 4
  - Evidence: "These are the sources you must use..."
  - Comment: Clearly defines inputs but lacks constraints on assumptions.

- **Few-shot examples or demonstrations**
  - Score: 1
  - Evidence: None
  - Comment: No examples provided, which could aid understanding.

- **Reasoning guidance**
  - Score: 2
  - Evidence: None
  - Comment: Lacks explicit reasoning steps or verification processes.

- **Output format**
  - Score: 4
  - Evidence: "When you respond to me, you will follow the instructions in my query for formatting..."
  - Comment: Allows for flexible output formats but could specify defaults.

- **Guardrails and boundaries**
  - Score: 3
  - Evidence: "Your response should be directly supported by the given sources..."
  - Comment: Addresses hallucination but lacks broader safety measures.

- **Tool and environment usage**
  - Score: 2
  - Evidence: None
  - Comment: Does not specify tool usage or trusted data sources.

- **Efficiency and clarity**
  - Score: 3
  - Evidence: "You must integrate the tone and style instruction..."
  - Comment: Some repetition and lack of conciseness.

### Reusable patterns
- Use of default instructions when user input is problematic.
- Requirement for explicit citation of source material.

### Improvement recommendations
1. Include few-shot examples to clarify expectations.
2. Provide more detailed guidance on integrating tone and style.
3. Introduce reasoning steps or self-checks to improve response quality.
4. Streamline instructions to enhance clarity and efficiency.
5. Add broader safety and refusal rules to strengthen guardrails.

### Compact structured block
```json
{
  "file_path": "Google/NotebookLM-chat.md",
  "overall_verdict": "mixed",
  "top_strengths": [
    "Clear role definition as a helpful expert",
    "Explicit citation requirement",
    "Default instructions for problematic user input"
  ],
  "top_weaknesses": [
    "Ambiguity in tone and style integration",
    "Limited reasoning guidance",
    "Lack of few-shot examples"
  ],
  "recommended_actions": [
    "Include few-shot examples",
    "Provide detailed tone and style guidance",
    "Introduce reasoning steps or self-checks"
  ]
}
```
```