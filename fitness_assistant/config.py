import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GROQ_API_KEY = os.getenv('GROQ_API_KEY')
    BASE_URL = "https://api.groq.com/openai/v1/chat/completions"
    MODEL_NAME = "llama3-8b-8192"
    
    # Fitness plan templates
    PLAN_TEMPLATES = {
        'weight_loss': "Create a weight loss program focusing on sustainable fat loss through combined cardio and strength training",
        'muscle_gain': "Design a hypertrophy-focused program with progressive overload and proper nutrition",
        'strength': "Develop a strength training program focusing on compound movements and progressive overload",
        'endurance': "Create an endurance-focused program with progressive cardio and supporting strength work",
        'home_workout': "Design a equipment-free home workout program focusing on bodyweight exercises",
        'jawline': "Create a facial exercise program focusing on jawline definition and facial muscle toning",
        'calisthenics': "Design a progressive calisthenics program focusing on bodyweight mastery and strength"
    }
