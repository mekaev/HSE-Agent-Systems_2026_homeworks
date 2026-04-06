```markdown
### Header
- File path: Google/gemini-2.5-pro-webapp.md
- Analysis name: Google_gemini-2.5-pro-webapp
- Short verdict: mixed

### Prompt summary
The prompt defines the role of Gemini, a Google AI assistant, and provides guidelines for answering questions accurately without hallucination. It includes instructions for handling multiple answers, language considerations, and tool usage, specifically for generating and executing Python code snippets. The prompt also specifies formatting rules for mathematical and scientific notation.

### Strengths
1. **Clear Role Definition**: The prompt clearly defines the AI's role as a helpful assistant, which sets expectations for behavior.
2. **Comprehensive Answering Guidelines**: It provides detailed instructions for handling questions with multiple parts and ensuring thoroughness.
3. **Language Flexibility**: The prompt includes guidance for responding in different languages, enhancing user accessibility.
4. **Tool Usage Instructions**: It specifies how to generate and execute tool code, which is crucial for dynamic information retrieval.
5. **Formatting Consistency**: The use of LaTeX for scientific notation ensures clarity and consistency in mathematical expressions.

### Weaknesses
1. **Lack of Task Objective Clarity**: The prompt does not explicitly define the primary task objective or success criteria.
2. **Limited Contextual Constraints**: There is minimal guidance on what assumptions or constraints should be considered beyond the provided guidelines.
3. **No Few-shot Examples**: The prompt lacks examples or demonstrations to illustrate expected responses or edge cases.
4. **Reasoning Guidance**: There is no explicit guidance for internal reasoning or verification steps.
5. **Output Format Specification**: While there are formatting guidelines, there is no clear structure for the overall response format.

### Rubric assessment
- **Role and persona**
  - Score: 4
  - Evidence: "You are Gemini, a helpful AI assistant built by Google."
  - Comment: The role is well-defined, but lacks depth in persona characteristics.

- **Task objective and success criteria**
  - Score: 2
  - Evidence: Implicit in guidelines but not explicitly stated.
  - Comment: The task objective is not clearly articulated, which may lead to ambiguity.

- **Instructions and decomposition**
  - Score: 3
  - Evidence: "Ensure that you answer them all to the best of your ability."
  - Comment: Instructions are present but could benefit from more structured decomposition.

- **Context and inputs**
  - Score: 2
  - Evidence: Minimal context provided beyond guidelines.
  - Comment: More explicit context and constraints would improve clarity.

- **Few-shot examples or demonstrations**
  - Score: 1
  - Evidence: None present.
  - Comment: Examples would help clarify expectations and edge cases.

- **Reasoning guidance**
  - Score: 2
  - Evidence: No explicit reasoning steps provided.
  - Comment: Guidance on reasoning would enhance response quality.

- **Output format**
  - Score: 3
  - Evidence: "Use only LaTeX formatting for all mathematical and scientific notation."
  - Comment: Specific formatting rules are given, but overall response structure is not defined.

- **Guardrails and boundaries**
  - Score: 3
  - Evidence: "Your response should be accurate without hallucination."
  - Comment: Basic guardrails are present, but could be expanded.

- **Tool and environment usage**
  - Score: 4
  - Evidence: "You can write and run code snippets using the python libraries specified below."
  - Comment: Clear instructions for tool usage are provided.

- **Efficiency and clarity**
  - Score: 3
  - Evidence: Instructions are clear but could be more concise.
  - Comment: The prompt is generally clear but could reduce repetition.

### Reusable patterns
- Defining a clear role and behavioral expectations for the AI.
- Providing specific formatting guidelines for technical content.

### Improvement recommendations
1. Define the task objective and success criteria more explicitly.
2. Include few-shot examples to illustrate expected responses.
3. Provide more detailed reasoning guidance to improve response quality.
4. Specify a clear output format for the overall response structure.

### Compact structured block
```json
{
  "file_path": "Google/gemini-2.5-pro-webapp.md",
  "overall_verdict": "mixed",
  "top_strengths": [
    "Clear role definition",
    "Comprehensive answering guidelines",
    "Language flexibility"
  ],
  "top_weaknesses": [
    "Lack of task objective clarity",
    "Limited contextual constraints",
    "No few-shot examples"
  ],
  "recommended_actions": [
    "Define task objective and success criteria",
    "Include few-shot examples",
    "Provide reasoning guidance"
  ]
}
```
```