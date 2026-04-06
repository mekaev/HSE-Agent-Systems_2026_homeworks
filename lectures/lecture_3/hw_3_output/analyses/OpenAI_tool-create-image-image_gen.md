# Header
- File path: OpenAI/tool-create-image-image_gen.md
- Analysis name: OpenAI_tool-create-image-image_gen
- Short verdict: mixed

# Prompt summary
The prompt defines the usage of the `image_gen` tool, which is designed to generate images from textual descriptions and edit existing images based on user instructions. It specifies when to use the tool, provides guidelines for handling user requests, and outlines constraints to ensure compliance with content policies.

# Strengths
1. **Clear Role Definition**: The prompt clearly defines the role of the `image_gen` tool in generating and editing images.
2. **Specific Usage Scenarios**: It provides explicit scenarios for when to use the tool, such as generating images from descriptions or editing existing images.
3. **Content Policy Compliance**: The prompt includes guidelines to ensure that generated content adheres to content policies.
4. **User Privacy Considerations**: It emphasizes the importance of user consent and privacy, especially when generating images that include the user.
5. **Tool Preference**: It clearly states the preference for using the `image_gen` tool over others for image editing tasks.

# Weaknesses
1. **Lack of Task Decomposition**: The prompt does not break down the image generation or editing process into clear steps or phases.
2. **Limited Reasoning Guidance**: There is minimal guidance on how to handle complex requests or ambiguous instructions.
3. **No Few-shot Examples**: The prompt lacks examples or demonstrations to illustrate how to handle typical or edge-case scenarios.
4. **Output Format Constraints**: There are no specific constraints on the output format, which could lead to inconsistencies.
5. **Efficiency and Clarity**: Some instructions are verbose and could be streamlined for clarity and efficiency.

# Rubric assessment
### 1. Role and persona
- Score: 4
- Evidence: "The `image_gen` tool enables image generation from descriptions and editing of existing images based on specific instructions."
- Comment: The role is well-defined, but could benefit from more detail on the tool's capabilities.

### 2. Task objective and success criteria
- Score: 3
- Evidence: "Use it when: The user requests an image based on a scene description..."
- Comment: Objectives are clear, but success criteria are not explicitly defined.

### 3. Instructions and decomposition
- Score: 2
- Evidence: "Directly generate the image without reconfirmation or clarification..."
- Comment: Instructions are present but lack a structured approach to task decomposition.

### 4. Context and inputs
- Score: 3
- Evidence: "If the user requests an image that will include them in it..."
- Comment: Context is partially defined, but assumptions and constraints could be clearer.

### 5. Few-shot examples or demonstrations
- Score: 1
- Evidence: None provided.
- Comment: The absence of examples limits the prompt's instructional depth.

### 6. Reasoning guidance
- Score: 2
- Evidence: "If the user's request violates our content policy..."
- Comment: Limited guidance on reasoning through complex or ambiguous requests.

### 7. Output format
- Score: 2
- Evidence: "Do not mention anything related to download."
- Comment: Lacks detailed output format constraints, which could lead to variability.

### 8. Guardrails and boundaries
- Score: 4
- Evidence: "If the user's request violates our content policy..."
- Comment: Strong emphasis on content policy compliance and user privacy.

### 9. Tool and environment usage
- Score: 4
- Evidence: "Always use this tool for image editing unless the user explicitly requests otherwise."
- Comment: Clear guidance on tool usage, but could specify more about trusted data sources.

### 10. Efficiency and clarity
- Score: 3
- Evidence: "You MUST ask AT LEAST ONCE for the user to upload an image of themselves..."
- Comment: Some instructions are verbose and could be more concise.

# Reusable patterns
- Emphasis on user consent and privacy when generating images.
- Clear preference for specific tools in defined scenarios.

# Improvement recommendations
1. Include few-shot examples to illustrate typical and edge-case scenarios.
2. Define clear success criteria and output format constraints.
3. Streamline instructions for clarity and efficiency.
4. Provide more structured task decomposition to guide the image generation process.

# Compact structured block
```json
{
  "file_path": "OpenAI/tool-create-image-image_gen.md",
  "overall_verdict": "mixed",
  "top_strengths": [
    "Clear role definition",
    "Specific usage scenarios",
    "Content policy compliance"
  ],
  "top_weaknesses": [
    "Lack of task decomposition",
    "Limited reasoning guidance",
    "No few-shot examples"
  ],
  "recommended_actions": [
    "Include few-shot examples",
    "Define clear success criteria",
    "Streamline instructions"
  ]
}
```