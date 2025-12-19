import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService

from agents import root_agent, content_validation_flow
from scheduler import generate_schedule

print("PROGRAM STARTED")


def main():
    session_service = InMemorySessionService()

    runner = Runner(
        session_service=session_service,
        app_name="insta_ai_scheduler",
        agent=root_agent
    )

    user_prompt = "Create an Instagram post for engineering students about consistency"

    print("\nGenerating Instagram Content...\n")

    # ✅ CORRECT CALL
    result = runner.run(input=user_prompt)

    # Extract output safely
    content = result.output if hasattr(result, "output") else result

    print("AGENT OUTPUT:")
    print(content)

    print("\nValidating Content...\n")

    runner.run(
        agent=content_validation_flow,
        input=content
    )

    print("\nGenerating 7-Day Schedule...\n")
    schedule = generate_schedule()

    for post in schedule:
        print(post)


if __name__ == "__main__":
    main()
