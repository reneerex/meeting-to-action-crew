from crewai import Task
from tools import transcript_reader, report_writer, youtube_transcript_tool
from agents import meeting_summarizer, action_item_extractor, owner_assigner, deadline_agent, report_generator


summary_task = Task(
    description="""
    Read the file transcript.txt.
    Analyze the meeting transcript.

    Create:
    - Executive summary
    - Key discussion points
    - Important decisions made

    Keep the summary concise and professional.
    """,
    expected_output="""
    A structured meeting summary containing:
    - Executive Summary
    - Key Discussion Points
    - Decisions Made
    """,
    tools=[transcript_reader, youtube_transcript_tool],
    agent=meeting_summarizer
)

action_task = Task(
    description="""
    Read the file transcript.txt.
    Review the meeting transcript.

    Extract every action item,
    task,
    follow-up,
    commitment,
    or deliverable mentioned.

    Do not summarize.
    Focus only on actionable work.
    """,
    expected_output="""
    A bullet list of action items.
    """,
    tools=[transcript_reader],
    agent=action_item_extractor
)

ownership_task = Task(
    description="""
    Read the file transcript.txt.
    Review the meeting transcript.

    Identify who is responsible
    for each action item.

    Match tasks with owners whenever possible.
    """,
    expected_output="""
    A structured list:

    Person -> Responsibility
    """,
    tools=[transcript_reader],
    agent=owner_assigner
)

deadline_task = Task(
    description="""
    Read the file transcript.txt.
    Analyze the meeting transcript.

    Identify:
    - Deadlines
    - Due dates
    - Milestones
    - Review dates

    Associate them with tasks whenever possible.
    """,
    expected_output="""
    Task -> Deadline mapping
    """,
    tools=[transcript_reader],
    agent=deadline_agent
)

report_task = Task(
    description="""
    Read the file transcript.txt.
    Create a professional meeting report.

    Combine:
    - Summary
    - Action Items
    - Ownership Assignments
    - Deadlines

    Format everything clearly in markdown.
    """,
    expected_output="""
    A professional markdown report containing:

    # Meeting Summary

    ## Key Discussion Points

    ## Decisions Made

    ## Action Items

    ## Owners

    ## Deadlines
    """,
    tools=[report_writer],
    agent=report_generator,
    context=[
        summary_task,
        action_task,
        ownership_task,
        deadline_task
    ],
    output_file='final_report.md'
)