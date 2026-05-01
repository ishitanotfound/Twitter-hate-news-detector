from crewai import Crew

from agents import hate_speech_detector
from tasks import hate_speech_detection_task

# Define the Crew with agents and tasks
crew = Crew(
    agents=[hate_speech_detector],
    tasks=[hate_speech_detection_task],
    verbose=False,
)# do we need this if we have openrouter_api_key? maybe not, but let's keep it for now. We can remove it later if we want to simplify the code.

# Kickoff the Crew with the input query
# Text = "Public libraries are important resources for everyone in the city."
# Text = "That country is less intelligent and incapable of contributing to society."
Text = "People from that race are all untrustworthy and should not be allowed to work in public sector."

result = crew.kickoff(inputs={"text": Text})

print("Response:", result)