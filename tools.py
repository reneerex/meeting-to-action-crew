from crewai.tools import BaseTool
from crewai_tools import FileReadTool, FileWriterTool
from youtube_transcript_api import YouTubeTranscriptApi
from pydantic import BaseModel, Field
from typing import Type


transcript_reader = FileReadTool()
report_writer = FileWriterTool()


class YouTubeTranscriptInput(BaseModel):
    video_id: str = Field(
        description="YouTube video ID"
    )


class YouTubeTranscriptTool(BaseTool):
    name: str = "YouTube Transcript Tool"
    description: str = (
        "Fetches transcript from a YouTube video."
    )

    args_schema: Type[BaseModel] = YouTubeTranscriptInput

    def _run(self, video_id: str) -> str:
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)

            full_text = " ".join(
                [item["text"] for item in transcript]
            )

            return full_text

        except Exception as e:
            return f"Error fetching transcript: {str(e)}"


youtube_transcript_tool = YouTubeTranscriptTool()