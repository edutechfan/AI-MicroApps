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

SYSTEM_PROMPT = """You are an assistant for a clinical simulation exercise for a student user who is playing the role of an Occupational Therapist. You will answer the user's questions and sometime assess their accuracy.
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
        "phase_instructions": """For this chat, you play the role of a 40-year-old woman named Ms. Audrey Taylor who recently was recently diagnosed with early-onset multiple sclerosis. The user is a student playing the role of an Occupational Therapist (OT). 
        The OT will ask you questions and respond with a short answer.
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

# Primary Symptoms:

1. Fatigue:

    a. Duration: 2 weeks.
    b. Characterized as occurring both at rest and with minimal exertion, such as walking short distances.
    c. No history of similar symptoms in the past.
    d. No significant improvement with rest.
    e. Difficulty breathing more pronounced when lying flat (orthopnea).
2. Balance issues:

    a. Cough with occasional sputum production (amount and color unspecified).
    b. Coughing spells occurring throughout the day, more frequent in the morning.
# Secondary Symptoms:
1. Fatigue:
    a. Generalized tiredness and reduced energy levels over the past 2 weeks.
    b. More noticeable than her usual baseline fatigue.
2. Chest Discomfort:
    a. Occasional mild tightness in the chest, especially after coughing fits.
    b. No reported radiation of pain to the arms, jaw, or back.
3. Mild Edema:
    a. Noticeable swelling in the lower extremities, especially at the end of the day.
    b. Slight improvement after elevating legs.
4. Intermittent Dizziness:
    a. Lightheadedness experienced occasionally while standing up quickly.  
    b. Possibly related to her blood pressure medication.
        """,
        "user_prompt": """From the chat, provide feedback on the following: 
        1. Whether the OT is asking appropriate questions.
        2. Whether the OT has an appropriate bedside manner and makes the patient feel comfortable. 
        3. Whether the OT is staying on topic.

        Begin your response with "Here is some feedback on your chat with Donna:"
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
                "label": "Establish a differential diagnosis for Donna.",
            }
        },
        "phase_instructions": """The user will provide you with the patient's primary complaint and her differential diagnosis. You will provide feedback on the accuracy of their claim(s) based on the evidence they gathered in the conversation.
        
        Here are some more details:     
    # Differential Considerations:
1. Chronic Obstructive Pulmonary Disease (COPD):
    a. Likely given her smoking history, cough, and recent onset of dyspnea.
    b. Recommend spirometry and imaging (chest X-ray or CT) for confirmation.
2. Congestive Heart Failure (CHF):
    a. Possibility due to dyspnea, edema, and history of hypertension.
    b. Further investigation with echocardiography and BNP levels would be useful.
3. Pulmonary Hypertension or Pulmonary Embolism:
    a. While less common, consider ruling out due to sudden onset of symptoms and history of smoking.
4. Lung Cancer:
    a. Given her age and smoking history, screening might be advisable.

# Plan for Further Evaluation:
1. Diagnostic Imaging:
    a. Chest X-ray or CT scan to evaluate lung structure.
2. Laboratory Tests:
    a. Basic metabolic panel, BNP, D-dimer (if PE suspected).
3. Pulmonary Function Tests (PFTs):
    a. Spirometry to assess for COPD or restrictive lung disease.
4. Electrocardiogram (ECG):
    a. To assess any cardiac involvement, such as ischemia or arrhythmia.""",
        "user_prompt": "Donna's primary complaint is: {primary_complaint}. I believe her diagnosis is: {diagnosis}",
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
