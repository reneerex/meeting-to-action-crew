from crewai import Agent, LLM
from tools import transcript_reader,report_writer,youtube_transcript_tool
from dotenv import load_dotenv
import os
load_dotenv()

llm = LLM(
    model="ollama/qwen3:4b",
    base_url="http://localhost:11434"
)


# SUMMARIZER
meeting_summarizer=Agent(
    role='Meeting Summarizer',
    goal='Create a concise summary of the meeting.',
    llm=llm,
    verbose=True,
    #memory=True,
    backstory="""
    You are an expert business analyst.
    You specialize in understanding meetings,
    extracting key discussion points,
    important decisions,
    and summarizing conversations clearly.
    """,
    tools=[transcript_reader,youtube_transcript_tool],
    allow_delegation=True
)

# TO-DO
action_item_extractor=Agent(
    role='Action Item Extractor',
    goal='Identify all tasks and action items mentioned.',
    llm=llm,
    verbose=True,
    #memory=True,
    backstory="""
    You are an operations manager.
    Your job is to carefully identify every task,
    deliverable, follow-up action,
    and commitment discussed during meetings.
    """,
    tools=[transcript_reader],
    allow_delegation=True
)

# RESPONSIBILITY
owner_assigner=Agent(
    role='Responsibility Tracker',
    goal='Determine who is responsible for each action item.',
    llm=llm,
    verbose=True,
    #memory=True,
    backstory="""
    You are a project coordinator.
    You specialize in mapping responsibilities
    and assigning ownership to action items
    based on meeting discussions.
    """,
    tools=[transcript_reader],
    allow_delegation=True
)

# DEADLINES
deadline_agent=Agent(
    role='Deadline Extractor',
    goal='Identify deadlines and due dates.',
    llm=llm,
    verbose=True,
    #memory=True,
    backstory="""
    You are a scheduling specialist.
    You identify deadlines,
    milestones,
    target dates,
    and time-sensitive commitments.
    """,
    tools=[transcript_reader],
    allow_delegation=True
)

# FINAL REPORT
report_generator=Agent(
    role='Project Coordinator',
    goal='Combine outputs into a structured report.',
    llm=llm,
    verbose=True,
    #memory=True,
    backstory="""
    You are an executive assistant.
    Your responsibility is to prepare
    clean professional reports
    containing summaries,
    decisions,
    action items,
    owners,
    and deadlines.
    """,
    tools=[report_writer],
    allow_delegation=True
)