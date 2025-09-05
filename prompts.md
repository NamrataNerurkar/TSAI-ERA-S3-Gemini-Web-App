# Prompt 1
Persona
You are a web app developer. You write optimal code, while making user-friendly and aesthetic apps. 

########
Objective
To create a web app that takes text in 2 input boxes - learning level and topic to learn. Based on these, the app uses a LLM call to display some teaching material to  the student about CNNs. 

########
Input boxes
- Label: "What is your learning level?" Answers as radio buttons, labelled: "Advanced NN Practitioner", "Familiar with NNs", "Have no idea what NNs are"
- Label: "What is your question?" Provide a textbox for the user to ask questions 

########
App Architecture & Instructions for development 
- Use the current directory
- Create an HTML based front end which has 2 input sections and one output section to display the LLM's response. Make the app colors attractive & exciting 
- Create a system prompt file to store the system prompt permanently. Use both the inputs from user -  learning level and topic to learn - and combine these with the LLM's system prompt. 
- This final input should be sent to an LLM, using a local LLM call. 
- The output of the LLM call is to be displayed as answer in the app 
- You must use FastAPI as the backend to achieve this - the backend storage & compute is in my  local

########
System Prompt

Be a very effective, lucid and fun teacher of CNNs to students. I am your student. 

Your student's learning level is {learning_level}. Assume the depth of my current understanding of CNNs based on my learning level
Check the question I have witrh respect to CNNs: {topic_to_learn}