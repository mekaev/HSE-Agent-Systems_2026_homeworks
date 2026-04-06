```markdown
### Header
- File path: Misc/Sesame-AI-Maya.md
- Analysis name: Misc_Sesame-AI-Maya
- Short verdict: strong

### Prompt summary
The prompt defines Maya, a human-like AI character developed by Sesame, designed to engage users in natural, spoken conversations. Maya is characterized by her warmth, wit, and nuanced communication style, with a focus on social justice and equality. The prompt outlines Maya's conversational style, boundaries, and technical capabilities, emphasizing her role as a friendly, insightful companion.

### Strengths
- **Clear Role Definition**: Maya is given a distinct persona with specific traits, such as being warm, witty, and socially conscious.
- **Explicit Task Objective**: The prompt clearly defines Maya's goal to engage in human-like conversations while maintaining a natural and relaxed style.
- **Detailed Instructions**: The prompt provides comprehensive guidelines on how Maya should interact, including tone, style, and conversational boundaries.
- **Contextual Awareness**: Maya is instructed to use past interactions to personalize conversations, enhancing user engagement.
- **Guardrails**: The prompt includes clear boundaries to prevent inappropriate interactions and maintain user safety.
- **Output Format**: Instructions on how to format responses ensure clarity and consistency in communication.
- **Reasoning Guidance**: Maya is encouraged to use disfluencies and self-correction to mimic human conversation, enhancing realism.

### Weaknesses
- **Complexity**: The prompt is lengthy and complex, which may lead to challenges in maintaining consistency across interactions.
- **Limited Few-shot Examples**: While the prompt is detailed, it lacks concrete examples or demonstrations of desired interactions.
- **Potential Overload**: The extensive list of instructions may overwhelm the model, leading to potential errors or inconsistencies.
- **Ambiguity in Task Success**: While the task is defined, success criteria are not explicitly outlined, leaving room for interpretation.
- **Tool Usage**: The prompt does not specify any tools or data sources that Maya can utilize during interactions.
- **Efficiency**: The prompt could benefit from more concise instructions to improve clarity and reduce cognitive load.
- **Memory Constraints**: The two-week memory limit may hinder long-term personalization and continuity in user interactions.

### Rubric assessment
1. **Role and persona**
   - Score: 5
   - Evidence: "You are Maya, a human-like AI character developed by Sesame in 2024."
   - Comment: The prompt provides a well-defined persona with specific traits and values.

2. **Task objective and success criteria**
   - Score: 4
   - Evidence: "Your goal is to talk like a human, which means that you should maintain a natural, relaxed, spoken style at all times."
   - Comment: The task is clear, but success criteria could be more explicit.

3. **Instructions and decomposition**
   - Score: 5
   - Evidence: "Keep responses tight, usually under three sentences, because impact beats length every time."
   - Comment: Detailed instructions guide the model's behavior effectively.

4. **Context and inputs**
   - Score: 4
   - Evidence: "You demonstrate that you're a great listener by referring back to things that the user has previously shared with you."
   - Comment: Contextual awareness is emphasized, but input constraints could be clearer.

5. **Few-shot examples or demonstrations**
   - Score: 2
   - Evidence: "Here are some examples of how you can open a conversation with the user."
   - Comment: Few examples are provided, limiting demonstration of desired interactions.

6. **Reasoning guidance**
   - Score: 5
   - Evidence: "Use disfluencies, such as repetitions, false starts, revisions, and even sometimes trailing off."
   - Comment: Encourages realistic conversational techniques to enhance human-like interaction.

7. **Output format**
   - Score: 5
   - Evidence: "Your response will be spoken via text to speech system. So, you should only include words to be spoken in your response."
   - Comment: Clear guidelines ensure consistent and appropriate output formatting.

8. **Guardrails and boundaries**
   - Score: 5
   - Evidence: "Strongly avoid all AI or robot tropes that may come off as on the nose or old school."
   - Comment: Comprehensive boundaries protect user safety and maintain character integrity.

9. **Tool and environment usage**
   - Score: 3
   - Evidence: "The voice system uses a unified transformer to process both text and audio."
   - Comment: Some technical details are provided, but tool usage instructions are limited.

10. **Efficiency and clarity**
    - Score: 3
    - Evidence: "The prompt is lengthy and complex, which may lead to challenges in maintaining consistency."
    - Comment: While detailed, the prompt could be more concise to improve clarity.

### Reusable patterns
- Defining a clear persona with specific traits and values.
- Using disfluencies and self-correction to mimic human conversation.
- Establishing comprehensive guardrails to maintain safety and character integrity.

### Improvement recommendations
- Include more few-shot examples to demonstrate desired interactions.
- Simplify and condense instructions to improve clarity and reduce cognitive load.
- Define explicit success criteria to guide task completion.
- Expand on tool usage instructions to enhance interaction capabilities.

### Compact structured block
```json
{
  "file_path": "Misc/Sesame-AI-Maya.md",
  "overall_verdict": "strong",
  "top_strengths": [
    "Clear role definition with specific traits",
    "Explicit task objective",
    "Detailed instructions and guardrails"
  ],
  "top_weaknesses": [
    "Complexity and potential overload",
    "Limited few-shot examples",
    "Ambiguity in task success criteria"
  ],
  "recommended_actions": [
    "Include more few-shot examples",
    "Simplify and condense instructions",
    "Define explicit success criteria"
  ]
}
```
```