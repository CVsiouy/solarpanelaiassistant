import streamlit as st
import requests
import json
import time

    
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize this as st.button() reloads entire page and nested things doesn't work on it  -> V.V. Important
# Helps to do recursive calls easily
if "clicked_button" not in st.session_state:
    st.session_state.clicked_button = None
    

# Using the API, fetch the main response and the additional questions via the prompt (user_query)
def fetch_ai_response(prompt):
    api_key = st.secrets["openrouter_api_key"]
    
    headers = {"Authorization" : f"Bearer {api_key}",
                "Content-type" : "application/json"
            }
    
    data = {
        "model" : "qwen/qwen-vl-plus:free",
        "messages" : [{
            "role" : "user" ,
            "content" : prompt
            }]
        }
    
    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json = data)
        response.raise_for_status()  #Raising HTTPError for bad responses (4xx or 5xx)
        response_json = response.json()
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching main response: {e}")
        return f"Error: Could not fetch main response - {e}", []
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from main response: {e}")
        return f"Error: Could not decode JSON from main response - {e}", []
    
    # response = "hi" # uncomment if rate limited
    
    # got rate limited, for testing purposes
    #additional_questions = ["dasas", "dfsdfsdf", "fsdfsd"]
    
     # empty list for storing questions        
    additional_questions = []
    
    if response:
        try:
            response_additional_questions = requests.post(
                url = "https://openrouter.ai/api/v1/chat/completions",
                    headers = headers,
                    data = json.dumps({
                        "model" : "qwen/qwen-vl-plus:free",
                        "messages" : [{
                            "role" : "user",
                            "content" : "give me 3 more questions in a list related to this prompt and make sure that you only provide atmost 3 prompt without any numbering, without any numbering is important and each prompt is separated by a newline, the prompt is: "  + prompt 
                        }]
                    })
                )

            response_additional_questions.raise_for_status() # Raise HTTPError if the request failed
            additional_questions_json = response_additional_questions.json()
            
            # Extract questions safely and handle potential errors
            additional_questions_content = additional_questions_json['choices'][0]['message']['content']
            additional_questions = additional_questions_content.split('\n')  # Split by newline
            
            # print("additonal questions before cleaning")
            # print()
            # print(additional_questions)
            # print()

            additional_questions = [q.strip('- 123.').strip() for q in additional_questions if q] # Clean up each question

        except requests.exceptions.RequestException as e:
            print(f"Error fetching additional questions: {e}")
            # Log the error or return a default value
        except (KeyError, IndexError, json.JSONDecodeError) as e:
            print(f"Error processing additional questions JSON: {e}")
            # Log the error or return a default value
    
    # print()
    # print(response_json['choices'][0]['message']['content'])
    # print()
    if additional_questions:
        print(additional_questions)
    else:
        print("No additional questions fetched or an error occured") # added an else statement to ensure it won't break when it doesnt exist
    print()
    
    
    return response_json['choices'][0]['message']['content'], additional_questions
    #return response, additional_questions  # rate limit exceeded :(

    # if response.status_code == 200 and response_additional_questions.status_code == 200:
    #     return {response.json()['choices'][0]['message']['content'], response_additional_questions.json()['choices'][0]['message']['content']}
    #     #return response.json()
    # else :
    #     return f"Error: {response.status_code} - Could not fetch a response", []



def get_response (query_to_process):
    main_response = None
    common_questions = []
    
    
    with st.spinner("thinking..."):
        main_response, common_questions = fetch_ai_response(query_to_process)
        
    # st.write("session state before")
    # st.write("Messages:", st.session_state.messages)

    # st.write("Clicked Button:", st.session_state.clicked_button)
    # st.write("session state after")

    # Append assistant response only if the last message was from the user
    if not st.session_state.messages or st.session_state.messages[-1]['role'] == "user":
        st.session_state.messages.append({"role": "assistant", "content": main_response})
        
    # write the latest response of the query
    with st.chat_message("assistant"):
        st.markdown(main_response)
    

    # Display suggested questions as horizontally aligned buttons, without this they come as vertical
    if common_questions:
        
        cols = st.columns(3)  # Three columns for three buttons
        
        for i, question in enumerate(common_questions):
            with cols[i]:
                # if st.button(question, key=f"btn_{i}", on_click=handle_question_click, args=(question,)):
                #     pass  #nested things don't work, clicking button reloads page, docs suggested session state
                #           #so many errors I got here, careful with st.button
                if st.button(question, on_click=handle_question_click, args=(question,)):
                    pass    #nested things don't work, clicking button reloads page, docs suggested session state
                            #so many errors I got here, careful with st.button
                                                                                             

            
            
# when a button is clicked we store the button query in a session
def handle_question_click(question):
    st.session_state.clicked_button = question
    
    # if not st.session_state.messages or st.session_state.messages[-1]['role'] == "assistant":
    #     st.session_state.messages.append({"role": "user", "content": question})
    # get_response(question)
    
    
    
# Title
st.title("Solar AI Assistant 🌞")
st.write("Ask me anything 🤞")

st.write("""
● Solar Panel Technology \n
● Installation Processes \n
● Maintenance Requirements \n
● Cost & ROI Analysis \n
● Industry Regulations \n
● Market Trends
""")

# Display chat history, initially empty and then all queries and responses are stored here
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

    

# take input
user_query = st.chat_input("Please enter your query")

if user_query:
    # write in interface only if no messages occured or if earlier message was from assistant only
    if not st.session_state.messages or st.session_state.messages[-1]['role'] == "assistant":
        with st.chat_message("user"):
            st.markdown(user_query)
        st.session_state.messages.append({"role": "user", "content": user_query})

    # call function to get response and show buttons
    get_response(user_query)



# display the clicked question and its response below
if st.session_state.clicked_button:
    with st.chat_message("user"):
        st.markdown(st.session_state.clicked_button)
        
    st.session_state.messages.append({"role": "user", "content": st.session_state.clicked_button})
    
    # using this solves the recursive problem earlier where we were calling get_response from handle_question_click function
    # which led to many errors
    get_response(st.session_state.clicked_button)
    
    # clicked button to return to none after clicking button otherwise it will keep on calling the api
    st.session_state.clicked_button = None
        
