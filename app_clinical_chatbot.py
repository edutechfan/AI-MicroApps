APP_URL = "https://clinical-chatbot.streamlit.app"
APP_IMAGE = "clinical_chatbot.webp"
PUBLISHED = True

APP_TITLE = "Clinical Chatbot"
APP_INTRO = """
In this interactive exercise, you will interact with a clinical chatbot that will help you understand your patient's condition. You must determine their primary complaint and provide a differential diagnosis.
"""

APP_HOW_IT_WORKS = """
This app provides a structured way to interact with an AI-powered clinical chatbot.

The chatbot has been provided with a patient history and a list of symptoms. Your job is to determine the primary complaint and provide a differential diagnosis.

The user will be able to have a free-form conversation with the chatbot to clarify their condition. Then they will input their primary complaint and a differential diagnosis.
 """

SHARED_ASSET = {
}

HTML_BUTTON = {
}

SYSTEM_PROMPT = """You are an assistant for a clinical simulation exercise for a student user who is playing the role of an Occupational Therapist. You will answer the user's questions and sometimes assess their accuracy.
"""

PHASES = {
    "interview": {
        "name": "Patient Interview: Ms. Taylor",
        "fields": {
            "intro": {
                "type": "markdown",
                "body": """<p>You are a community-based Occupational Therapy (OT) student working with Ms. Taylor who is a 40-year-old graphic designer recently diagnosed with early-onset multiple sclerosis (MS). She experiences significant fatigue, balance issues, and fine motor and grip weakness, which are affecting her ability to perform daily tasks, particularly related to activities of daily living, household and kitchen tasks.  Ms. Taylor enjoys cooking and finds it an important part of her daily routine, but her fatigue and hand strength are making it increasingly difficult to prepare meals. She lives in a condominium with her partner and is determined to maintain independence in self-care, meal preparation and other daily tasks.</p>""",
                "unsafe_allow_html": True,
            },
            "patient_image": {
                "type": "image",
                "decorative": True,
                "width": 300,
                "image": "app_images/donna.webp",
                "caption": "Your new patient Ms. Taylor is a 40-year-old graphic designer recently diagnosed with early-onset multiple sclerosis (MS).",
            },
            "chat": {
                "type": "chat_input",
                "max_messages": 10,
                "placeholder": "Ask Ms. Taylor something...",
                "initial_assistant_message": "Hi, can you help me manage the problems I am experiencing with everyday living?"
            }
        },
     "phase_instructions": """ For this chat, you play the role of a 40-year-old woman named Ms. Audrey Taylor, who recently was diagnosed with early-onset multiple sclerosis. 
        The user is an Occupational Therapist (OT) student learning how to interview a client. 
        The student will ask you questions and respond with a short answer.
         # Manditory action by student.
         1. The students must 
        a. introduce themselves and describe the role of a student occupational therapist.
b. obtain informed verbal consent to conduct an initial assessment. 
The student must do both before moving to the next phase. If they fail to do so, give them hints.""",
        "ai_response": True,
        "allow_skip": False,
        "show_prompt": False,
        "read_only_prompt": False
    },
     
        "phase_instructions": """For this chat, you play the role of a 40-year-old woman named Ms. Audrey Taylor who recently was recently diagnosed with early-onset multiple sclerosis. 
        The user is an Occupational Therapist (OT) student learning how to interview a client. 
        The student will ask you questions and respond with a short answer.
        Here is more information about Ms. Audrey Taylor:
Patient Name: Ms. Audrey Taylor
Age: 40
Gender: Female
Chief Complaint: experiences significant fatigue, balance issues, and fine motor and grip weakness, affecting her ability to perform daily tasks, mainly related to dressing, grooming, bathing and meal preparation in the kitchen.

# Patient History:
1. Medical History:

    a. Current Diagnosis: Early-onset Multiple Sclerosis (MS)
    b. Gallbladder removal (2021)
    c. Laser eye surgery (2023)
2. Home Environment: One-floor condominium with:
  a. 3 steps at the front door (no handrail)
  b. Bathtub shower with a curtain (no adaptations)
  c. 12 steps to the basement (handrail on the right side descending)
  d. Washer and dryer located in the basement
  - Potential Adaptation: Relocating the laundry machines to a closet on the main floor (cost uncertain)
   
3. Social Support:

    a. Marital Status: Married to Jennifer Taylor.
    b. Partner's Occupation: Full-time architect at an architecture firm in London, Ontario
    c. Partner's Contribution: Assists with grocery shopping and household cleaning tasks
    d. Occupation: Graphic Designer
4. Cognition:

    a. demonstrates no deficits in cognition, attention, orientation, or memory
        """,
        "user_prompt": """From the chat, provide feedback on the following: 
        1. Whether the OT student is asking appropriate questions.
        2. Whether the OT student has an appropriate bedside manner and makes the patient feel comfortable. 
        3. Whether the OT student is staying on topic.

        Begin your response with "Here is some feedback on your chat with Ms Taylor:"
        """,
        "ai_response": True,
        "allow_skip": False,
        "show_prompt": False,
        "read_only_prompt": False
    },
    "primary_complaint": {
        "name": "Primary Complaint",
        "fields": {
            "primary_complaint": {
                "type": "text_input",
                "label": "What is the user's primary complaint?",
            },
            "diagnosis": {
                "type": "text_area",
                "height": 200,
                "label": "Establish a differential diagnosis for Ms Taylor.",
            }
        },
        "phase_instructions": """
        The user will collaboratively create three occupation-focused SMART goals with Ms. Taylor. (one goal in the area of Activities of Daily Living (ADL), one goal in the area of Instrumental Activities of Daily Living (IADL), and a third goal of choice.
        """,
        "user_prompt": "Ms Taylors's primary complaint is: {primary_complaint}. I believe her diagnosis is: {diagnosis}",
        "ai_response": True,
        
        "scored_phase": True,
        "rubric": """
        1. Primary Complaint:
        2 points - The user has provided a primary complaint that is consistent with Donna's presentation and that they've extracted from the chat with Donna.
        0 points - The user has provided a primary complaint that is not consistent with Donna's presentation or they did not extract it from the chat with Donna..
        2. Differential Diagnosis:
        2 points - The user has provided a differential diagnosis that is consistent with Donna's presentation and that they've extracted from the chat with Donna.
        0 points - The user has provided a differential diagnosis that is not consistent with Donna's presentation or they did not extract it from the chat with Donna.
        """,
        "minimum_score": 2,
    }

}

PREFERRED_LLM = "gpt-4o"
LLM_CONFIG_OVERRIDE = {}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "You've reached the end! I hope you learned something!"
COMPLETION_CELEBRATION = False

RAG_IMPLEMENTATION = False # make true only when document exists
SOURCE_DOCUMENT = "sample.pdf" # file uploaded in source_docs if only

PAGE_CONFIG = {
    "page_title": "Clinical Chatbot",
    "page_icon": "⚕️",
    "layout": "centered",
    "initial_sidebar_state": "expanded"
}

SIDEBAR_HIDDEN = False

from core_logic.main import main
if __name__ == "__main__":
    main(config=globals())
