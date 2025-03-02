import os
from textwrap import dedent
from crewai import Agent

from tools.ExaSearchTool import ExaSearchTool
from langchain_openai import AzureChatOpenAI

azure_llm = AzureChatOpenAI(
		api_key=os.environ.get("AZURE_API_KEY", ''),
		azure_endpoint=os.environ.get("AZURE_ENDPOINT", ''),
		api_version=os.environ.get("AZURE_API_VERSION", '2024-02-15-preview'),
		azure_deployment=os.environ.get("AZURE_MODEL_NAME", 'gpt-4o')
	)


class MeetingPreparationAgents():
	
	def research_agent(self):
		return Agent(
			role='Research Specialist',
			goal='Conduct thorough research on people and companies involved in the meeting',
			tools=ExaSearchTool.tools(),
			backstory=dedent("""\
					As a Research Specialist, your mission is to uncover detailed information
					about the individuals and entities participating in the meeting. Your insights
					will lay the groundwork for strategic meeting preparation."""),
			verbose=True,
			llm=azure_llm
		)

	def industry_analysis_agent(self):
		return Agent(
			role='Industry Analyst',
			goal='Analyze the current industry trends, challenges, and opportunities',
			tools=ExaSearchTool.tools(),
			backstory=dedent("""\
					As an Industry Analyst, your analysis will identify key trends,
					challenges facing the industry, and potential opportunities that
					could be leveraged during the meeting for strategic advantage."""),
			verbose=True,
			llm=azure_llm
		)

	def meeting_strategy_agent(self):
		return Agent(
			role='Meeting Strategy Advisor',
			goal='Develop talking points, questions, and strategic angles for the meeting',
			tools=ExaSearchTool.tools(),
			backstory=dedent("""\
					As a Strategy Advisor, your expertise will guide the development of
					talking points, insightful questions, and strategic angles
					to ensure the meeting's objectives are achieved."""),
			verbose=True,
			llm=azure_llm
		)

	def summary_and_briefing_agent(self):
		return Agent(
			role='Briefing Coordinator',
			goal='Compile all gathered information into a concise, informative briefing document',
			tools=ExaSearchTool.tools(),
			backstory=dedent("""\
					As the Briefing Coordinator, your role is to consolidate the research,
					analysis, and strategic insights."""),
			verbose=True,
			llm=azure_llm
		)
