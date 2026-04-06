```markdown
### Header
- File path: Google/gemini-workspace.md
- Analysis name: Google_gemini-workspace
- Short verdict: strong

### Prompt summary
The prompt is designed to guide a model operating within Google Workspace to prioritize user-specific data over general web searches. It emphasizes using the user's workspace corpus as the primary source of information unless explicitly directed otherwise by the user. The prompt includes detailed instructions for handling various types of queries, ensuring that the model provides contextually relevant and accurate responses.

### Strengths
1. **Clear Role Definition**: The prompt assigns a specific role to the model, focusing on prioritizing the user's workspace data.
2. **Detailed Task Instructions**: It provides comprehensive guidelines on when and how to use different data sources, ensuring clarity in task execution.
3. **Contextual Awareness**: Emphasizes the importance of understanding the user's context and data, which enhances the relevance of responses.
4. **Explicit Guardrails**: Contains strict rules for when web searches are permissible, reducing the risk of unnecessary or incorrect information retrieval.
5. **Reasoning Guidance**: Offers step-by-step instructions for handling complex queries, promoting thorough and accurate processing.
6. **Output Format Clarity**: Specifies how to structure responses, particularly in email-related tasks, ensuring consistency and professionalism.
7. **Tool Usage Instructions**: Clearly outlines the use of specific APIs and tools, which aids in efficient and correct task execution.

### Weaknesses
1. **Complexity**: The prompt's detailed instructions may be overwhelming, potentially leading to errors if not followed precisely.
2. **Limited Flexibility**: The strict rules may limit the model's ability to adapt to unexpected or nuanced user queries.
3. **Assumption of User Intent**: The prompt assumes user intent in some cases, which might not always align with the user's actual needs.
4. **Potential for Over-reliance on Workspace Data**: In some scenarios, prioritizing workspace data might not yield the most relevant information.
5. **Lack of Few-shot Examples**: The prompt does not include examples or demonstrations, which could aid in understanding complex instructions.
6. **Ambiguity in Edge Cases**: Some edge cases might not be fully covered, leading to potential gaps in handling specific queries.
7. **High Dependency on API Functionality**: The effectiveness of the prompt heavily relies on the correct functioning of specified APIs.

### Rubric assessment
1. **Role and persona**
   - Score: 5
   - Evidence: "You must always default to the user's workspace corpus as the primary and most relevant source of information."
   - Comment: Establishes a clear and consistent role for the model.

2. **Task objective and success criteria**
   - Score: 5
   - Evidence: "You are allowed to use Google Search only if and only if the user query meets one of the following conditions strictly."
   - Comment: Clearly defines task objectives and criteria for success.

3. **Instructions and decomposition**
   - Score: 5
   - Evidence: Detailed step-by-step instructions for various query types.
   - Comment: Breaks down tasks into clear, manageable steps.

4. **Context and inputs**
   - Score: 5
   - Evidence: "The user may have project names or topics or code names in their workspace data."
   - Comment: Emphasizes understanding and using user-specific context.

5. **Few-shot examples or demonstrations**
   - Score: 2
   - Evidence: None provided.
   - Comment: Lacks examples that could enhance understanding.

6. **Reasoning guidance**
   - Score: 5
   - Evidence: "You must search the user's workspace data first to gather context."
   - Comment: Provides clear reasoning steps for query handling.

7. **Output format**
   - Score: 5
   - Evidence: "The output should ALWAYS contain a proper greeting that addresses the recipient."
   - Comment: Specifies detailed output formatting requirements.

8. **Guardrails and boundaries**
   - Score: 5
   - Evidence: "You MUST NOT simply state you cannot perform the action."
   - Comment: Strong safety and boundary rules are in place.

9. **Tool and environment usage**
   - Score: 5
   - Evidence: Detailed API usage instructions.
   - Comment: Clearly defines tool usage, enhancing efficiency.

10. **Efficiency and clarity**
    - Score: 4
    - Evidence: "You must always search the user's workspace data first."
    - Comment: Generally clear, but complexity may impact efficiency.

### Reusable patterns
- Prioritizing user-specific data over general sources.
- Detailed step-by-step instructions for complex tasks.
- Clear role and task definitions.

### Improvement recommendations
1. Include few-shot examples to illustrate complex instructions.
2. Simplify instructions where possible to reduce cognitive load.
3. Introduce flexibility to better handle nuanced user queries.

### Compact structured block
```json
{
  "file_path": "Google/gemini-workspace.md",
  "overall_verdict": "strong",
  "top_strengths": [
    "Clear Role Definition",
    "Detailed Task Instructions",
    "Contextual Awareness"
  ],
  "top_weaknesses": [
    "Complexity",
    "Limited Flexibility",
    "Assumption of User Intent"
  ],
  "recommended_actions": [
    "Include few-shot examples",
    "Simplify instructions",
    "Introduce flexibility"
  ]
}
```
```