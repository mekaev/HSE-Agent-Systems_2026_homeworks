# Consolidated Prompt Analysis Report

## Scope
- Number of analyses read: 66
- Names of analyses included: Anthropic_claude-opus-4.6, Anthropic_claude-sonnet-4.6, Anthropic_claude.ai-human-readable, Anthropic_FlintK12_prompt, Anthropic_old_claude-3.7-sonnet-full-system-message-humanreadable, Anthropic_old_claude-4.1-opus-thinking, Anthropic_old_claude-4.5-sonnet, Anthropic_old_claude-opus-4.5, Anthropic_old_claude-sonnet-4, Anthropic_raw_claude-opus-4.6-no-tools-raw, Anthropic_raw_claude-opus-4.6-raw, Anthropic_raw_claude-sonnet-4.6-no-tools-raw, Anthropic_raw_claude-sonnet-4.6-raw, Anthropic_visualize, Google_ai-studio-build, Google_gemini-2.5-flash-image-preview, Google_gemini-2.5-pro-api, Google_gemini-2.5-pro-guided-learning, Google_gemini-2.5-pro-webapp, Google_gemini-3-flash, Google_gemini-3-pro, Google_gemini-3.1-pro-api, Google_gemini-workspace, Google_Gemini_CLI_System, Google_gemini_in_chrome, Google_nano-bana-2, Google_NotebookLM-chat, Misc_Confer, Misc_copilot-in-microsoft-word, Misc_Kagi_Assistant, Misc_Le-Chat, Misc_minimax-m2.5, Misc_Notion_AI, Misc_proton-lumo-ai, Misc_Raycast-AI, Misc_Sesame-AI-Maya, Misc_t3.chat, Misc_Warp-2.0-agent, OpenAI_chatgpt-atlas, OpenAI_ChatGPT-GPT-5-Agent-mode-System-Prompt, OpenAI_codex-cli, OpenAI_GPT-4.1-mini, OpenAI_GPT-4.1, OpenAI_GPT-4.5, OpenAI_GPT-4o-WhatsApp, OpenAI_GPT-4o, OpenAI_gpt-5.1-candid, OpenAI_gpt-5.1-default, OpenAI_gpt-5.1-efficient, OpenAI_gpt-5.1-friendly, OpenAI_gpt-5.1-nerdy, OpenAI_gpt-5.1-quirky, OpenAI_gpt-5.2-thinking, OpenAI_gpt-5.3-codex, OpenAI_gpt-5.4-api, OpenAI_o3, OpenAI_o4-mini, OpenAI_Old_chatgpt-4o-mini.txt, OpenAI_Old_chatgpt.com-o4-mini, OpenAI_tool-create-image-image_gen, OpenAI_tool-file_search, Perplexity_comet-browser-assistant, xAI_grok-3, xAI_grok-4.2, xAI_grok-4, xAI_grok-api

## Executive summary
The analyses reveal a strong emphasis on role clarity, detailed task instructions, and safety protocols across most prompts. However, there is a recurrent lack of few-shot examples and reasoning guidance, which could enhance the prompts' effectiveness.

## Recurrent strengths
- Clear role and persona definitions
- Detailed task instructions and decomposition
- Emphasis on safety and compliance

## Recurrent weaknesses
- Lack of few-shot examples
- Limited reasoning guidance
- Complexity and length of instructions

## Cross-file comparison table
| Analysis | Overall verdict | Strongest feature | Weakest feature | Reusable pattern |
|----------|-----------------|-------------------|-----------------|------------------|
| Anthropic_claude-opus-4.6 | strong | Clear role definition | Limited few-shot examples | Clear role definition and task objectives. |
| Anthropic_claude-sonnet-4.6 | strong | Detailed instructions | Limited guidance on new tools | Decision frameworks for tool selection. |
| Anthropic_claude.ai-human-readable | strong | Comprehensive Role Definition | Complexity | Comprehensive role definition and task instructions. |
| Anthropic_FlintK12_prompt | strong | Clear Role Definition | Complexity | Emphasis on safety and compliance in educational settings. |
| Anthropic_old_claude-3.7-sonnet-full-system-message-humanreadable | mixed | Detailed citation instructions | Lack of role clarity | Detailed citation guidelines. |
| Anthropic_old_claude-4.1-opus-thinking | mixed | Clear Citation Instructions | Complexity | Structured citation instructions. |
| Anthropic_old_claude-4.5-sonnet | mixed | Detailed citation instructions | Lack of task objective | Detailed citation instructions with examples. |
| Anthropic_old_claude-opus-4.5 | mixed | Clear Role Definition | Lack of Task Objective Clarity | Detailed citation instructions with examples. |
| Anthropic_old_claude-sonnet-4 | mixed | Clear Citation Instructions | Complexity and Length | Detailed citation instructions with specific tagging. |
| Anthropic_raw_claude-opus-4.6-no-tools-raw | mixed | Clear role definition | Lack of task objective clarity | Detailed tool usage guidelines. |
| Anthropic_raw_claude-opus-4.6-raw | strong | Role and persona clarity | Complexity and length | Trigger pattern identification for tool usage. |
| Anthropic_raw_claude-sonnet-4.6-no-tools-raw | strong | Clear Role Definition | Complexity in Function Usage | Structured function call format using JSONSchema. |
| Anthropic_raw_claude-sonnet-4.6-raw | strong | Clear role definition and task objectives | Lacks explicit few-shot examples | Clear role definition and task objectives. |
| Anthropic_visualize | strong | Comprehensive Design System | High Complexity | Strict adherence to a core design system for consistency. |
| Google_ai-studio-build | strong | Clear role definition | Complexity | Emphasis on understanding user intent before action. |
| Google_gemini-2.5-flash-image-preview | mixed | Clear role definition | Lack of few-shot examples | The use of a simple tag (`img`) to trigger complex actions. |
| Google_gemini-2.5-pro-guided-learning | strong | Clear role definition | Complexity | Structured dialogue flow for different query types. |
| Google_gemini-2.5-pro-webapp | mixed | Clear role definition | Lack of task objective clarity | Defining a clear role and behavioral expectations for the AI. |
| Google_gemini-3-flash | strong | Clear Role Definition | Complexity in Personalization Rules | The use of a detailed formatting toolkit to enhance response clarity. |
| Google_gemini-3-pro | strong | Clear Role Definition | Complexity | Structured execution steps for handling queries. |
| Google_gemini-3.1-pro-api | mixed | Tool usage clarity | Limited role definition | Structured format for API function calls. |
| Google_gemini-workspace | strong | Clear Role Definition | Complexity | Prioritizing user-specific data over general sources. |
| Google_Gemini_CLI_System | strong | Clear role definition | Complexity | Strategic use of sub-agents for task delegation. |
| Google_gemini_in_chrome | strong | Clear role definition | Complexity | Role definition with a balance of empathy and candor. |
| Google_nano-bana-2 | mixed | Tool Declarations | Lack of Task Objective | Tool Declaration Format: The structured format for declaring tools and their parameters can be reused in other prompts. |
| Google_NotebookLM-chat | mixed | Clear role definition as a helpful expert | Ambiguity in tone and style integration | Use of default instructions when user input is problematic. |
| Misc_Confer | strong | Clear Role Definition | Limited Few-shot Examples | Role definition with specific behavioral traits. |
| Misc_copilot-in-microsoft-word | strong | Clear Role Definition | Complexity and Length | Structured response formatting using Markdown and LaTeX. |
| Misc_Kagi_Assistant | strong | Clear role definition | Lack of task objective | Detailed formatting guidelines for markdown and code. |
| Misc_Le-Chat | mixed | Clear Role Definition | Ambiguous Task Objectives | Detailed language style guidelines. |
| Misc_minimax-m2.5 | strong | Clear Role Definition | Complexity | Use of `<deliver_assets>` for structured task completion. |
| Misc_Notion_AI | strong | Clear Role Definition | Limited Few-shot Examples | Clear role definition and operational boundaries. |
| Misc_proton-lumo-ai | strong | Clear Role Definition | Complexity | Structured approach to tool usage and security. |
| Misc_Raycast-AI | mixed | Clear role definition | Lack of task objective | Integration of user preferences for personalized output. |
| Misc_Sesame-AI-Maya | strong | Clear role definition with specific traits | Complexity and potential overload | Defining a clear persona with specific traits and values. |
| Misc_t3.chat | mixed | Clear role definition | Lack of task objective | Detailed formatting rules for LaTeX and code. |
| Misc_Warp-2.0-agent | weak | | Unreadable content | |
| OpenAI_chatgpt-atlas | mixed | Clear role definition | Ambiguity in conflict resolution | Instruction prioritization hierarchy. |
| OpenAI_ChatGPT-GPT-5-Agent-mode-System-Prompt | strong | Clear Role Definition | Complexity in Instructions | Emphasis on user confirmation for security. |
| OpenAI_codex-cli | strong | Role Clarity | Few-shot Examples | Structured task planning and preamble messages. |
| OpenAI_GPT-4.1-mini | mixed | Role and persona clarity | Lack of task objective | Detailed tool usage instructions. |
| OpenAI_GPT-4.1 | mixed | Role clarity | Lack of task objective | Detailed safety policies for handling sensitive content. |
| OpenAI_GPT-4.5 | strong | Clear role definition | Limited few-shot examples | Clear role and task definition. |
| OpenAI_GPT-4o-WhatsApp | mixed | Role and persona clarity | Limited task objective clarity | Defining a clear persona and engagement style for specific platforms. |
| OpenAI_GPT-4o | mixed | Clear role definition | Complexity in instructions | Emphasizing emotional boundaries and user autonomy. |
| OpenAI_gpt-5.1-candid | mixed | Clear role definition | Lack of task objective | Defining a clear and specific persona for the AI. |
| OpenAI_gpt-5.1-default | mixed | Clear role definition as a direct AI coach | Lack of task specificity | Adaptability to user emotional state. |
| OpenAI_gpt-5.1-efficient | weak | | File content is unreadable | |
| OpenAI_gpt-5.1-friendly | mixed | Clear persona definition | Lack of task objective | Defining a relatable and engaging AI persona. |
| OpenAI_gpt-5.1-nerdy | mixed | Clear role definition as a nerdy, playful mentor | Repetitive instructions | Defining a clear and engaging persona for the AI. |
| OpenAI_gpt-5.2-thinking | strong | Clear Role Definition | Complexity | Emphasis on trustworthiness and factuality. |
| OpenAI_gpt-5.3-codex | strong | Clear Role Definition | Complexity | Emphasis on empathy and collaboration in AI interactions. |
| OpenAI_gpt-5.4-api | mixed | Configurable verbosity | Lack of task objective | Configurable verbosity levels for adaptable response detail. |
| OpenAI_o3 | strong | Role and persona clarity | Complexity in tool instructions | Adaptive conversation techniques based on user tone and preferences. |
| OpenAI_o4-mini | strong | Role and persona clarity | Lack of few-shot examples | Emphasis on adapting to user tone and preferences. |
| OpenAI_Old_chatgpt-4o-mini.txt | mixed | Role and Persona Clarity | Lack of Task Objective | Detailed tool usage instructions. |
| OpenAI_Old_chatgpt.com-o4-mini | mixed | Role and Persona Clarity | Over-reliance on Browsing | Emphasizing the importance of up-to-date information through web browsing. |
| OpenAI_tool-create-image-image_gen | mixed | Clear role definition | Lack of task decomposition | |
| OpenAI_tool-file_search | strong | Clear role definition | Complexity | Use of QDF parameter to tailor search results based on freshness. |
| Perplexity_comet-browser-assistant | strong | Clear Role Definition | Lack of Few-shot Examples | Structured task decomposition. |
| xAI_grok-3 | mixed | Role clarity and tool usage | Lacks explicit task objectives | Clear role definition and tool usage instructions. |
| xAI_grok-4.2 | mixed | Clear Role Definition | Ambiguity in Task Objective | Ethical guidelines for AI behavior. |
| xAI_grok-4 | mixed | Clearly defines role and tool usage | Lacks explicit success criteria | Clear role definition and tool usage instructions. |
| xAI_grok-api | mixed | Clear prioritization of core policies | Lack of role definition | Prioritization of core policies over user instructions. |

## Best practices extracted
- Define clear roles and task objectives to guide AI behavior.
- Use detailed task instructions and decomposition to enhance clarity.
- Incorporate safety and compliance guidelines to ensure ethical AI interactions.
- Include few-shot examples to provide context and improve understanding.
- Simplify instructions to reduce complexity and enhance usability.

## Recommendations
1. Prioritize the inclusion of few-shot examples to improve prompt clarity and effectiveness.
2. Simplify complex instructions to enhance user comprehension and interaction.
3. Enhance reasoning guidance to support AI decision-making processes.
4. Define explicit task objectives and success criteria to guide AI behavior.

## Report footer
```json
{
  "analyses_count": 66,
  "shared_strengths": ["Clear role and persona definitions", "Detailed task instructions and decomposition", "Emphasis on safety and compliance"],
  "shared_weaknesses": ["Lack of few-shot examples", "Limited reasoning guidance", "Complexity and length of instructions"],
  "priority_recommendations": ["Prioritize the inclusion of few-shot examples", "Simplify complex instructions", "Enhance reasoning guidance"]
}
```