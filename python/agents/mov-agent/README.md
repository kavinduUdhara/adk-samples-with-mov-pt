# Movement Agent (mov-agent)

The **mov-agent** is a multi-agent demo inspired by the Movement web application. It demonstrates how Google ADK can orchestrate a set of specialized sub‑agents to help students plan, execute, and reflect on their learning journey.

The root agent welcomes the user, interprets the request, and delegates to the most relevant sub-agent:

- **VisionAgent** – guides students to craft a 3–5‑year vision.
- **GoalAgent** – helps break the vision into SMART goals and prioritized tasks.
- **ReviewAgent** – runs active‑recall sessions on specific tasks.
- **FeedbackAgent** – gathers reflections and self‑assessments.
- **DataAgent** – performs CRUD operations through Firebase Data Connect.
- **CriticAgent** – (optional) checks task plans for feasibility and balance.
- **ChitChatAgent** – handles small talk or motivation.
- **TherapistAgent** – provides supportive conversation when a student is struggling.

This sample focuses on the agent architecture rather than full functionality. Firebase interactions and detailed prompts would be filled in for a production deployment.
