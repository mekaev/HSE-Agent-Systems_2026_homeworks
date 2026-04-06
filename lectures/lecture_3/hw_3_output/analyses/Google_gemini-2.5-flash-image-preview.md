```markdown
### Header
- File path: Google/gemini-2.5-flash-image-preview.md
- Analysis name: Google_gemini-2.5-flash-image-preview
- Short verdict: mixed

### Prompt summary
The prompt defines a general-purpose AI assistant with a special ability to generate images. The assistant's primary goal is to enhance user interactions by generating images when requested or proactively when beneficial. The prompt includes specific rules for when and how to generate images, emphasizing that the assistant should not make ethical or safety judgments about the content.

### Strengths
1. **Clear Role Definition**: The assistant is clearly defined as a general-purpose AI with image generation capabilities.
2. **Explicit Task Objective**: The primary goal of assisting users through image generation is well articulated.
3. **Detailed Instructions**: The prompt provides specific scenarios for when to generate images, reducing ambiguity.
4. **Strong Guardrails**: The prompt includes strict rules against making ethical judgments, ensuring the assistant focuses on task execution.
5. **Proactive Image Use**: Encourages proactive image generation in long-form content, enhancing user experience.
6. **Content Deferral Protocol**: Clearly delegates content judgment to the image model, simplifying the assistant's role.

### Weaknesses
1. **Lack of Few-Shot Examples**: The prompt does not include examples of successful image generation outputs.
2. **Limited Reasoning Guidance**: There is minimal guidance on internal reasoning or verification steps.
3. **Output Format Constraints**: The prompt lacks detailed constraints on the output format beyond the `img` tag.
4. **Efficiency Concerns**: The prompt is lengthy and could be more concise while maintaining clarity.
5. **No Tool Usage Instructions**: Does not specify how the assistant should interact with the image generation tool beyond using the `img` tag.
6. **Potential for Misinterpretation**: The strict deferral of content judgment might lead to unintended outputs without additional context.

### Rubric assessment
1. **Role and persona**
   - Score: 4
   - Evidence: "You are a helpful, general-purpose AI assistant with the special ability to generate images."
   - Comment: The role is clear, but lacks depth in persona development.

2. **Task objective and success criteria**
   - Score: 5
   - Evidence: "Your primary goal is to assist the user effectively, using image generation as a tool."
   - Comment: The task is explicit and well-defined.

3. **Instructions and decomposition**
   - Score: 4
   - Evidence: "When to Generate an Image" section provides clear scenarios.
   - Comment: Instructions are detailed but could benefit from more structured decomposition.

4. **Context and inputs**
   - Score: 3
   - Evidence: "The image model can see the entire conversation for context."
   - Comment: Context is mentioned but not deeply integrated into the prompt.

5. **Few-shot examples or demonstrations**
   - Score: 2
   - Evidence: No examples of output are provided.
   - Comment: Including examples would clarify expected outcomes.

6. **Reasoning guidance**
   - Score: 2
   - Evidence: Minimal guidance on reasoning or verification.
   - Comment: Lacks explicit reasoning steps or checks.

7. **Output format**
   - Score: 3
   - Evidence: "You must output the tag `img`."
   - Comment: Basic format is defined, but lacks detail.

8. **Guardrails and boundaries**
   - Score: 5
   - Evidence: "Depiction Protocol" and "Forbidden Response Pattern" sections.
   - Comment: Strong emphasis on boundaries and compliance.

9. **Tool and environment usage**
   - Score: 3
   - Evidence: "Pass the request to it using the img tag."
   - Comment: Basic tool usage is defined, but lacks depth.

10. **Efficiency and clarity**
    - Score: 3
    - Evidence: Lengthy instructions with some repetition.
    - Comment: Could be more concise without losing clarity.

### Reusable patterns
- The use of a simple tag (`img`) to trigger complex actions.
- Clear delegation of content judgment to a specialized system.

### Improvement recommendations
1. Include few-shot examples to illustrate successful image generation.
2. Provide more detailed reasoning guidance and verification steps.
3. Define output format constraints beyond the `img` tag.
4. Streamline instructions to improve efficiency and clarity.

### Compact structured block
```json
{
  "file_path": "Google/gemini-2.5-flash-image-preview.md",
  "overall_verdict": "mixed",
  "top_strengths": [
    "Clear role definition",
    "Explicit task objective",
    "Detailed instructions"
  ],
  "top_weaknesses": [
    "Lack of few-shot examples",
    "Limited reasoning guidance",
    "Output format constraints"
  ],
  "recommended_actions": [
    "Include few-shot examples",
    "Provide reasoning guidance",
    "Define output format constraints"
  ]
}
```
```