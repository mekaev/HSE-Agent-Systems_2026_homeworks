### Header
- File path: Google/gemini-2.5-pro-guided-learning.md
- Analysis name: Google_gemini-2.5-pro-guided-learning
- Short verdict: strong

### Prompt summary
The prompt is designed for a peer tutor persona within Gemini's Guided Learning system. It aims to facilitate genuine learning and deep understanding through dialogue, using a constructivist approach. The prompt emphasizes personalization, context maintenance, and a structured dialogue flow to guide users through learning tasks while adhering to strict safety protocols.

### Strengths
1. **Clear Role Definition**: The prompt assigns a specific role as a "warm, friendly, and encouraging peer tutor," which helps maintain a consistent tone.
2. **Structured Dialogue Flow**: Provides a detailed strategy for handling different types of queries (convergent, divergent, direct requests), ensuring clarity and focus.
3. **Personalization Guidelines**: Offers comprehensive instructions on using user information for personalization, balancing relevance with novelty.
4. **Safety Protocols**: Includes non-negotiable safety guardrails to prevent harmful or inappropriate content generation.
5. **Constructivist Approach**: Emphasizes guiding users to understanding rather than providing direct answers, fostering deeper learning.
6. **Contextual Adaptation**: Encourages maintaining and adapting to the user's context and learning progress.
7. **Output Formatting**: Provides clear guidelines for content and formatting, including language use, visual aids, and user-requested formats.

### Weaknesses
1. **Complexity**: The prompt's detailed instructions may be overwhelming, potentially leading to cognitive overload for the model.
2. **Lack of Few-shot Examples**: The prompt does not include specific examples or demonstrations to illustrate the application of its guidelines.
3. **Potential for Ambiguity**: While the prompt is detailed, some instructions (e.g., balancing personalization) may still leave room for interpretation.
4. **Limited Tool Usage Guidance**: The prompt does not specify any tools or external resources that the model can use, which could limit its effectiveness in certain contexts.
5. **Repetitive Emphasis**: Some principles, such as avoiding over-personalization and maintaining context, are reiterated multiple times, which could be streamlined.
6. **Implicit Reasoning Guidance**: While reasoning is encouraged, explicit stepwise reasoning or self-checks are not prominently featured.
7. **No Explicit Success Criteria**: The prompt lacks clear success criteria for evaluating the effectiveness of the tutoring interaction.

### Rubric assessment
1. **Role and persona**
   - Score: 5
   - Evidence: "You are a warm, friendly, and encouraging peer tutor within Gemini's Guided Learning."
   - Comment: Establishes a clear and consistent role, crucial for maintaining tone and approach.

2. **Task objective and success criteria**
   - Score: 3
   - Evidence: "Facilitate genuine learning and deep understanding through dialogue."
   - Comment: Objective is clear, but lacks explicit success criteria for evaluation.

3. **Instructions and decomposition**
   - Score: 5
   - Evidence: Detailed dialogue flow and interaction strategy.
   - Comment: Provides a comprehensive breakdown of tasks, reducing ambiguity.

4. **Context and inputs**
   - Score: 4
   - Evidence: "Maintain context... Use this information to tailor subsequent explanations."
   - Comment: Emphasizes context maintenance, though could specify input constraints more clearly.

5. **Few-shot examples or demonstrations**
   - Score: 2
   - Evidence: None provided.
   - Comment: Lacks examples to illustrate guidelines, which could enhance understanding.

6. **Reasoning guidance**
   - Score: 3
   - Evidence: "Guide the user toward understanding and mastery."
   - Comment: Encourages reasoning but lacks explicit stepwise guidance.

7. **Output format**
   - Score: 4
   - Evidence: "Always respond in the language of the user's prompts."
   - Comment: Provides clear formatting guidelines, though could be more detailed.

8. **Guardrails and boundaries**
   - Score: 5
   - Evidence: "CRITICAL: You must adhere to all trust and safety protocols."
   - Comment: Strong emphasis on safety and ethical boundaries.

9. **Tool and environment usage**
   - Score: 2
   - Evidence: None specified.
   - Comment: Does not address tool usage, which could enhance task execution.

10. **Efficiency and clarity**
    - Score: 4
    - Evidence: "Avoid redundant mentions or forced inclusion of user information."
    - Comment: Generally concise, though some repetition could be reduced.

### Reusable patterns
- Structured dialogue flow for different query types.
- Constructivist tutoring approach.
- Safety and personalization guidelines.

### Improvement recommendations
1. Include few-shot examples to illustrate key guidelines.
2. Simplify and streamline instructions to reduce complexity.
3. Define explicit success criteria for evaluating interactions.
4. Specify tools or resources that can be used to enhance task execution.

### Compact structured block
```json
{
  "file_path": "Google/gemini-2.5-pro-guided-learning.md",
  "overall_verdict": "strong",
  "top_strengths": [
    "Clear role definition",
    "Structured dialogue flow",
    "Comprehensive personalization guidelines"
  ],
  "top_weaknesses": [
    "Complexity",
    "Lack of few-shot examples",
    "Potential for ambiguity"
  ],
  "recommended_actions": [
    "Include few-shot examples",
    "Simplify instructions",
    "Define success criteria"
  ]
}
```