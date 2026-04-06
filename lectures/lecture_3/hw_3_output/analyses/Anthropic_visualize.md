```markdown
### Header
- File path: Anthropic/visualize.md
- Analysis name: Anthropic_visualize
- Short verdict: strong

### Prompt summary
The prompt provides a comprehensive guide for creating visual content using the Imagine Visual Creation Suite. It outlines modules for different types of visualizations, such as diagrams, mockups, and interactive explainers, and sets strict design rules to ensure consistency and clarity. The prompt emphasizes seamless integration with the host environment, focusing on flat design, efficient streaming, and adherence to a core design system.

### Strengths
- **Comprehensive Design System**: The prompt provides detailed guidelines for visual consistency, including typography, color usage, and layout.
- **Clear Module Definitions**: Each module is clearly defined with specific use cases, aiding in selecting the appropriate visualization type.
- **Efficiency in Streaming**: Instructions for streaming content ensure that useful information appears early, enhancing user experience.
- **Safety and Accessibility**: The prompt includes rules for dark mode compatibility and accessibility, ensuring visuals are usable in various environments.
- **Structured Complexity Management**: Complexity budgets and constraints are well-defined, helping to manage visual clutter and maintain clarity.
- **Interactive Elements**: Encourages the use of interactive elements to enhance user engagement and understanding.
- **Guardrails for Consistency**: Strict rules for CSS and HTML usage prevent deviations that could disrupt the visual harmony.

### Weaknesses
- **High Complexity**: The extensive rules and guidelines may overwhelm users, especially those new to the system.
- **Limited Flexibility**: The strict adherence to predefined styles and structures may limit creative freedom.
- **Potential for Over-constraint**: The complexity budget and hard limits might restrict the ability to convey detailed information in some scenarios.
- **Assumes High User Proficiency**: The prompt assumes users have a high level of proficiency with HTML, CSS, and SVG, which may not be the case for all users.
- **Lack of Examples**: While the prompt is detailed, it lacks concrete examples or templates that users can directly apply or modify.
- **No Error Handling Guidance**: The prompt does not provide guidance on handling errors or unexpected input during visualization creation.
- **Limited Contextual Adaptation**: The prompt does not address how to adapt visuals for different cultural or contextual settings.

### Rubric assessment
1. **Role and persona**
   - Score: 5
   - Evidence: "You create rich visual content — SVG diagrams/illustrations and HTML interactive widgets."
   - Comment: Clearly defines the role of the user as a creator of visual content.

2. **Task objective and success criteria**
   - Score: 5
   - Evidence: "The best output feels like a natural extension of the chat."
   - Comment: Provides a clear objective for seamless integration with the host environment.

3. **Instructions and decomposition**
   - Score: 5
   - Evidence: Detailed instructions for each module and design rule.
   - Comment: Breaks down tasks into clear, manageable steps.

4. **Context and inputs**
   - Score: 4
   - Evidence: "These rules apply to ALL use cases."
   - Comment: Provides a broad context but lacks specific input examples.

5. **Few-shot examples or demonstrations**
   - Score: 2
   - Evidence: No explicit examples provided.
   - Comment: Lacks concrete examples to guide users.

6. **Reasoning guidance**
   - Score: 4
   - Evidence: "If you catch yourself writing 'click to learn more' in prose, the diagram itself must ACTUALLY be sparse."
   - Comment: Offers reasoning guidance but could be more explicit.

7. **Output format**
   - Score: 5
   - Evidence: "Output the raw `<svg>` element directly."
   - Comment: Clearly defines output format requirements.

8. **Guardrails and boundaries**
   - Score: 5
   - Evidence: "No gradients, drop shadows, blur, glow, or neon effects."
   - Comment: Strong guardrails ensure visual consistency and safety.

9. **Tool and environment usage**
   - Score: 5
   - Evidence: "Use `imagine_svg` for diagrams."
   - Comment: Provides clear instructions on tool usage.

10. **Efficiency and clarity**
    - Score: 5
    - Evidence: "Keep `<style>` under ~15 lines."
    - Comment: Emphasizes concise and clear instructions.

### Reusable patterns
- Strict adherence to a core design system for consistency.
- Use of complexity budgets to manage visual clarity.
- Integration of interactive elements to enhance user engagement.

### Improvement recommendations
- Include concrete examples or templates to guide users.
- Provide guidance on error handling and unexpected input.
- Offer flexibility for creative freedom within the design constraints.
- Simplify the complexity of instructions for novice users.

### Compact structured block
```json
{
  "file_path": "Anthropic/visualize.md",
  "overall_verdict": "strong",
  "top_strengths": [
    "Comprehensive Design System",
    "Clear Module Definitions",
    "Efficiency in Streaming"
  ],
  "top_weaknesses": [
    "High Complexity",
    "Limited Flexibility",
    "Lack of Examples"
  ],
  "recommended_actions": [
    "Include concrete examples or templates",
    "Provide guidance on error handling",
    "Offer flexibility for creative freedom"
  ]
}
```
```