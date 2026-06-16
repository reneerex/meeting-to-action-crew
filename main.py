from crewai import Crew,Process
from agents import meeting_summarizer, action_item_extractor, owner_assigner, deadline_agent, report_generator
from tasks import summary_task, action_task, ownership_task, deadline_task, report_task

crew = Crew(
  agents=[meeting_summarizer, action_item_extractor, owner_assigner, deadline_agent, report_generator],
  tasks=[summary_task, action_task, ownership_task, deadline_task, report_task],
  process=Process.sequential,
  #memory=True,
  cache=True,
  max_rpm=100,
  share_crew=True
)

result=crew.kickoff()
print(result)