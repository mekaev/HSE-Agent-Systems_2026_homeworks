```markdown
### Header
- File path: Google/nano-bana-2.md
- Analysis name: Google_nano-bana-2
- Short verdict: mixed

### Prompt summary
The prompt defines a set of tools for generating, displaying, and searching for images, as well as searching the web for information. It specifies the current time and location as Iceland, which may be relevant for contextual tasks.

### Strengths
- **Tool Declarations**: Clearly defines multiple tools with specific parameters, enhancing the model's ability to perform image-related tasks.
- **Parameter Specification**: Each tool has well-defined parameters, ensuring clarity in tool usage.
- **Contextual Information**: Provides current time and location, which can be useful for context-aware operations.
- **Diverse Functionality**: Supports a range of operations from image generation to web searches, increasing versatility.

### Weaknesses
- **Lack of Task Objective**: The prompt does not specify a clear task or objective for the model to achieve.
- **No Instructions or Decomposition**: There are no step-by-step instructions or guidance on how to use the tools effectively.
- **Absence of Examples**: Lacks few-shot examples or demonstrations to guide the model in tool usage.
- **Limited Reasoning Guidance**: Does not provide reasoning steps or verification processes for the model to follow.
- **Output Format Constraints**: There are no explicit constraints on the output format, which could lead to inconsistent results.

### Rubric assessment
1. **Role and persona**
   - Score: 2
   - Evidence: No specific role or persona is assigned.
   - Comment: A defined role could improve task focus.

2. **Task objective and success criteria**
   - Score: 1
   - Evidence: No explicit task or success criteria are provided.
   - Comment: Essential for guiding the model's actions.

3. **Instructions and decomposition**
   - Score: 1
   - Evidence: No instructions or ordered steps are present.
   - Comment: Instructions could reduce ambiguity.

4. **Context and inputs**
   - Score: 3
   - Evidence: "Current time is Sunday, March 1, 2026 at 7 PM Atlantic/Reykjavik."
   - Comment: Provides some context but lacks input constraints.

5. **Few-shot examples or demonstrations**
   - Score: 1
   - Evidence: None provided.
   - Comment: Examples could enhance understanding.

6. **Reasoning guidance**
   - Score: 1
   - Evidence: No reasoning steps or checks included.
   - Comment: Important for complex tasks.

7. **Output format**
   - Score: 2
   - Evidence: No specific output format is defined.
   - Comment: Format constraints could improve consistency.

8. **Guardrails and boundaries**
   - Score: 2
   - Evidence: No explicit safety or boundary rules.
   - Comment: Important for safe and reliable operation.

9. **Tool and environment usage**
   - Score: 4
   - Evidence: Detailed tool declarations with parameters.
   - Comment: Well-defined tools enhance capability.

10. **Efficiency and clarity**
    - Score: 3
    - Evidence: Clear tool definitions but lacks overall task clarity.
    - Comment: Clarity in task objectives is needed.

### Reusable patterns
- **Tool Declaration Format**: The structured format for declaring tools and their parameters can be reused in other prompts.

### Improvement recommendations
1. Define a clear task objective and success criteria.
2. Include step-by-step instructions or decision rules for tool usage.
3. Provide few-shot examples or demonstrations to guide the model.
4. Specify output format constraints to ensure consistent results.
5. Introduce reasoning guidance and verification steps.

### Compact structured block
```json
{
  "file_path": "Google/nano-bana-2.md",
  "overall_verdict": "mixed",
  "top_strengths": [
    "Tool Declarations",
    "Parameter Specification",
    "Contextual Information",
    "Diverse Functionality"
  ],
  "top_weaknesses": [
    "Lack of Task Objective",
    "No Instructions or Decomposition",
    "Absence of Examples",
    "Limited Reasoning Guidance",
    "Output Format Constraints"
  ],
  "recommended_actions": [
    "Define a clear task objective and success criteria.",
    "Include step-by-step instructions or decision rules for tool usage.",
    "Provide few-shot examples or demonstrations to guide the model.",
    "Specify output format constraints to ensure consistent results.",
    "Introduce reasoning guidance and verification steps."
  ]
}
```
```