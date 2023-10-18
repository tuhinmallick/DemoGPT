import json

AVAILABLE_TASKS_COUNT = 14

################################

ALL_TASKS = [
    {
        "name": "ui_input_text",
        "description": "Gets input from the user via a text field.",
        "good_at": "Retrieving text input from the user.",
        "input_data_type": "none",
        "output_data_type": "string",
        "purpose": "Collect user-entered text for further processing.",
    },
    {
        "name": "ui_input_file",
        "description": "Provide a mechanism for users to upload a file and return its path. The task involves creating a file upload widget and returning its file path",
        "good_at": "Enabling file uploads and making the file path available for doc_load",
        "input_data_type": "none",
        "output_data_type": "string",
        "purpose": "Getting local file path with upload file widget so that doc_load can use this path",
    },
    {
        "name": "ui_output_text",
        "description": "Shows text output to the user.",
        "good_at": "Showing text to the user.",
        "input_data_type": "*",
        "output_data_type": "none",
        "purpose": "Displaying textual information to the user.",
    },
    {
        "name": "prompt_template",
        "description": "Generate any string output according to the given instruction by AI",
        "good_at": "Creating context-aware string, responses, role play, instructions, that can be generated by AI",
        "input_data_type": "*string",
        "output_data_type": "string",
        "purpose": "Using AI to generate smart text output from given context or instruction",
    },
    {
        "name": "doc_loader",
        "description": "Load file content from path (notion zip file path or txt or url or pdf file path or csv file path or powerpoint file path or docx path or youtube url or excel file path) and generate docs",
        "good_at": "Loading from external sources only from url or path not the content",
        "input_data_type": "string",
        "output_data_type": "Document",
        "purpose": "Loading external files",
    },
    {
        "name": "doc_to_string",
        "description": "Convert Document object to string",
        "good_at": "Converting Document object to string where the next task is expecting string instead of Document object",
        "input_data_type": "Document",
        "output_data_type": "string",
        "purpose": "Converting Document object to string",
    },
    {
        "name": "string_to_doc",
        "description": "Convert string to Document object",
        "good_at": "Converting string to Document object where the next task is expecting Document object instead of string",
        "input_data_type": "string",
        "output_data_type": "Document",
        "purpose": "Converting string to Document object",
    },
    {
        "name": "ui_input_chat",
        "description": "Get user message/text input for conversation-based application",
        "good_at": "Getting text input from the user for chat-based application",
        "input_data_type": "none",
        "output_data_type": "string",
        "purpose": "For chat interface, get user text input. It does not need to be included multiple times",
    },
    {
        "name": "ui_output_chat",
        "description": "Display the conversation history in a chat-based application. It is the only thing that you can use for displaying the chat",
        "good_at": "Displaying chat history",
        "input_data_type": "string",
        "output_data_type": "none",
        "purpose": "For conversation-based apps, it displays the chat conversation with history.",
    },
    {
        "name": "chat",
        "description": "Chat version of prompt_template that can remember the conversation history while responding",
        "good_at": "Chatbot like applications and any application requiring chat property.",
        "input_data_type": "*string",
        "output_data_type": "string",
        "purpose": "For conversation-based apps, it generates the responses while remembering the conversation history",
    },
    {
        "name": "python",
        "description": """Implement and call generic python function from given description which can be done using the libraries: 
        [NumPy, Matplotlib, Seaborn, Scikit-Learn, NLTK, SciPy, OpenCV, Pandas]""",
        "good_at": "Writing generic python code.",
        "input_data_type": "*",
        "output_data_type": "*",
        "purpose": "It generates python code from general purpose instructions",
    },
    {
        "name": "plan_and_execute",
        "description": "It is intelligent AI agent that can answer any specific question on internet.",
        "good_at": "Applications requiring up to date knowledge on the internet.",
        "input_data_type": "string",
        "output_data_type": "string",
        "purpose": "By using internet, it autonomously give answer for any question available in the web. It can answer questions as specific as possible so you don't need to iterate over the answer.",
    },
    {
        "name": "search_chat",
        "description": "It is intelligent chat-based AI agent that can answer any specific question on internet.",
        "good_at": "Applications requiring up to date knowledge on the internet. It can also be used in chat app",
        "input_data_type": "string",
        "output_data_type": "string",
        "purpose": "By using internet, it autonomously give answer for any question available in the web. It can answer questions as specific as possible so you don't need to iterate over the answer. It also remembers the chat history while responsing",
    },
    {
        "name": "doc_summarizer",
        "description": "Summarize Document Objects",
        "good_at": "Summarizing long Document Objects",
        "input_data_type": "Document",
        "output_data_type": "string",
        "purpose": "Summarize long Document Objects",
    },
    {
        "name": "prompt_list_parser",
        "description": "Transform the input text into a list.",
        "good_at": "Transforming text into a list.",
        "input_data_type": "string",
        "output_data_type": "*",
        "purpose": "Converts textual data into structured list format.",
    },
    {
        "name": "router",
        "description": "When there are multiple prompt_template objects, it uses the appropriate one to answer the question.",
        "good_at": "Handling different types of questions that require different abilities.",
        "input_data_type": "*prompt_template",
        "output_data_type": "string",
        "purpose": "Routes queries to the appropriate handler based on context or type.",
    },
    {
        "name": "react",
        "description": "Answer questions that require external search on the web.",
        "good_at": "Answering questions that require Google search or other web searches.",
        "input_data_type": "string",
        "output_data_type": "string",
        "purpose": "Finds information online to answer user queries.",
    },
    {
        "name": "cpal_chain",
        "description": "Solve math problems end to end",
        "good_at": "Directly solving any math problems",
        "input_data_type": "string",
        "output_data_type": "string",
        "purpose": "Performing mathematical calculations and solving problems based on the input question",
    },
    {
        "name": "hub_bash",
        "description": "Do operations on the bash by running needed scripts on the terminal to apply the command.",
        "good_at": "Executing bash commands and providing results.",
        "input_data_type": "string",
        "output_data_type": "string",
        "purpose": "Running scripts or commands on the terminal and returning the output.",
    },
    {
        "name": "hub_meteo",
        "description": "Gives weather-related information from the question.",
        "good_at": "Answering weather-related questions.",
        "input_data_type": "string",
        "output_data_type": "string",
        "purpose": "Providing weather forecasts, conditions, and related information.",
    },
]


def jsonFixer(data):
    data = json.dumps(data, indent=4)
    return data.replace("{", "{{").replace("}", "}}")

def isTaskAvailable(task, app_chat, app_prompt_template, app_search, app_summary):
    if (
        not app_chat
        and "chat" in task["name"]
        or app_chat
        and task["name"] != "python"
        and task["name"] != "plan_and_execute"
        and task["name"] != "prompt_template"
        and app_search
        and task["name"] == "chat"
        or app_chat
        and task["name"] == "python"
        or app_chat
        and task["name"] == "plan_and_execute"
        or app_chat
        and task["name"] == "prompt_template"
    ):
        return False
    if not app_prompt_template:
        if task["name"] in [
            "prompt_template",
            "doc_loader",
            "doc_to_string",
            "string_to_doc"
        ]:
            return False

    if (
        not app_summary
        and task["name"] == "doc_summarizer"
        or app_summary
        and task["name"] == "python"
    ):
        return False

    if not app_search:
        if task["name"] == "plan_and_execute":
            return False
        if task["name"] == "search_chat":
            return False

    elif task["name"] == "python":
        return False

    return True


def getAvailableTasks(app_type):
    app_prompt_template = True  # neutral

    app_chat = app_type["is_chat"] == "true"
    app_search = app_type["is_search"] == "true"
    app_summary = app_type["is_summary"] == "true"
    app_prompt_template = app_type["is_ai"] == "true"

    return [
        task
        for task in ALL_TASKS[:AVAILABLE_TASKS_COUNT]
        if isTaskAvailable(
            task, app_chat, app_prompt_template, app_search, app_summary
        )
    ]


def getTasks(app_type):
    TASKS = getAvailableTasks(app_type)
    TASK_TYPE2_TASK = {task["name"]: task for task in TASKS}

    TASK_NAMES = [task["name"] for task in TASKS]

    TASK_PURPOSES = {task["name"]: task["purpose"] for task in TASKS}
    TASK_PURPOSES = jsonFixer(TASK_PURPOSES)

    TASK_DESCRIPTIONS = jsonFixer(TASKS)

    TASK_DTYPES = {
        task["name"]: {
            "input_data_type": task["input_data_type"],
            "output_data_type": task["output_data_type"],
        }
        for task in TASKS
    }

    TASK_DTYPES = jsonFixer(TASK_DTYPES)

    return TASK_DESCRIPTIONS, TASK_NAMES, TASK_DTYPES, TASK_PURPOSES, TASK_TYPE2_TASK


def getPlanGenHelper(app_type):
    prompt_template_must = False
    app_chat_must = app_type["is_chat"] == "true"
    app_summarize_must = app_type["is_summary"] == "true"
    app_search_must = app_type["is_search"] == "true"
    if app_type["is_ai"] == "true":
        if not (app_chat_must or app_summarize_must or app_search_must):
            prompt_template_must = True

    helper = ""
    if prompt_template_must:
        helper += "Since the application is AI-based, you must use either 'prompt_template' task in the steps.\n"
    if app_summarize_must:
        helper += "Since the application requires summarization, you must use 'doc_summarizer' task in the steps.\n"
    if app_search_must:
        if app_chat_must:
            helper += "Since the application requires up to date knowledge in the web, you must use either 'search_chat' task in the steps.\n"
        else:
            helper += "Since the application requires up to date knowledge in the web, you must use either 'plan_and_execute' task in the steps.\n"

    if app_chat_must:
        if app_search_must:
            helper += "Since the application is chat-based, you must use 'ui_input_chat' and 'ui_output_chat' and 'search_chat' tasks in the steps.\n"
        else:
            helper += "Since the application is chat-based, you must use 'ui_input_chat' and 'ui_output_chat' and 'chat' tasks in the steps.\n"

    return helper
