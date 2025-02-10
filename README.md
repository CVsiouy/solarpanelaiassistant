# Solar AI Assistant | wattmonk

This is a Wattmonk AI assignment where I create an AI assistant with the help of Qwen VL Plus LLM
accessed by openrouter API key. The assignment involves creation of a web interface by streamlit 
and integration of the chosen LLM with the web interface. The AI assistant has been upgraded to 
provide prompts related to user prompt after each response to effectively solve the user query and 
provide a rich User Experience for better accuracy.

The Navigation section also provides access to multiple pages where user can see Insights about 
Solar panel installation and do proper cost & ROI Analysis and see the visualization of adoptation
and decrease of solar panels and future scope of the project.

## Required Dependencies
-> streamlit

-> plotly

-> requests



## Set Up the Script
The required tools for running this python file are:-

1.) Download the .zip file and extract and go inside the directory

2.) Install the respective dependencies in your codespace or virtual environment such as pip install streamlit plotly requests

3.) Create account on openrouter and type on search bar qwen VL Plus (free) and click on it and go to API section to create your API Key

4.) Create a .streamlit folder and a file secrets.toml and write -> openrouter_api_key = "YOUR_API_KEY"

5.) run the python file via cmd using -> streamlit run app.py


## Challenges & Common Errors
1.) Nested code inside streamlit.button() have multiple issues, whenever a user clicks on a streamlit.button() it returns true and then in next action return false so it is suggested to use sessions for streamlit.button()

2.) In the code please ensure
  if st.button(question, on_click=handle_question_click, args=(question,)):   

  

  a.) on_click and onclick not coincide

  b.) Do not write handle_question_click() as that will make the function run without clicking any button

  c.) use of appropriate args or kwargs


  It is very much recommended to read documentation for streamlit.button() for advanced usecase.

  

3.) Ensure proper logic of sessions and avoid recursion and do proper error checking to reduce errors.

4.) In streamlit, widgets load before text so ensure that buttons do not show on top of page above the title.

## Future Scope
1.) Can be used by customers to resolve all queries immediately via the bot.

2.) Can be used to provide educational content for primary and secondary schooling.

3.) Can be used to provide solar panel optimal efficiency with usage of weather APIs.

4.) Able to generate in-depth Reports and Visualization for solar panel installation based on location. 

5.) Used for direct notification on changes on any rule and government subsidies and keeping up with market trends and industry regulations.

6.) Can be used to check for any maintenance issues and connecting with the company directly.

## Future Upgrades
1.) Google Oauth and Database can be added to store data for each user if they ever need to read their previous prompts again.

2.) Scraping of Latest News web articles can be done on the LatestNews.py page. 

3.) A broader Cost & ROI Analysis for Solar Panel installation may be adopted.

4.) Some blogs and Government schemes can be added for awareness purpose.

5.) Integration with weather API to provide Insight about optimal solar panel efficiency.

6.) Include a forum or Q&A section where users can share their experiences or ask questions to other users.

7.) Generate downloadable reports on solar installation cost-benefit analysis based on user inputs.

8.) Convert the app into a mobile-friendly version or release it on mobile app stores.

9.) Voice Interaction: Integrate speech-to-text and text-to-speech features for a more conversational, hands-free experience.

## Implementation

![image](https://github.com/user-attachments/assets/53ca98e2-9854-43ee-b075-eeee8afcee4e)



![image](https://github.com/user-attachments/assets/1be81fa9-8320-4388-86e8-d282c563094a)



![image](https://github.com/user-attachments/assets/b25f623a-9e85-41ba-9814-946eb6247cb0)

## Contact
Chirag Verma | +91 (798)-8055-537 | chiragverma00310@gmail.com



