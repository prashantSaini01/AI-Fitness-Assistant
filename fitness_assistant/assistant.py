# from .api_client import GroqAPIClient
# from .config import Config

# class FitnessAssistant:
#     def __init__(self):
#         """Initialize Fitness Assistant"""
#         self.api_client = GroqAPIClient()
#         self.plan_templates = Config.PLAN_TEMPLATES

#     def generate_fitness_plan(self, goal, fitness_level, duration, calories=None):
#         """Generate a personalized fitness plan"""
#         template = self.plan_templates.get(goal, self.plan_templates['weight_loss'])
        
#         messages = [
#             {
#                 "role": "system",
#                 "content": """You are an expert fitness coach creating personalized workout plans. 
#                 Format your response in Markdown with proper headings (#, ##), lists (1., 2., -), 
#                 and emphasis (**bold**, *italic*) where appropriate."""
#             },
#             {
#                 "role": "user",
#                 "content": f"""
#                 Create a {duration}-week fitness plan with:
#                 Goal: {goal}
#                 Fitness Level: {fitness_level}
#                 Daily Calories: {calories if calories else 'Maintenance'}
                
#                 Structure your response with these sections using proper Markdown formatting:
#                 # Personalized Fitness Plan
#                 ## Program Overview
#                 ## Weekly Schedule
#                 ## Exercise Details
#                 ## Nutrition Guidelines
#                 ## Progress Tracking
#                 ## Safety Tips
                
#                 Base the plan on: {template}
#                 """
#             }
#         ]
        
#         return self.api_client.call_api(messages)

#     def analyze_progress(self, weight, body_fat, muscle_mass, notes):
#         """Analyze fitness progress and provide recommendations"""
#         messages = [
#             {
#                 "role": "system",
#                 "content": """You are an expert fitness coach analyzing progress data.
#                 Format your response in Markdown with proper headings (#, ##), lists (1., 2., -), 
#                 and emphasis (**bold**, *italic*) where appropriate."""
#             },
#             {
#                 "role": "user",
#                 "content": f"""
#                 Analyze these fitness metrics and provide feedback using proper Markdown formatting:
                
#                 # Progress Analysis Report
                
#                 ## Current Metrics
#                 - Weight: {weight} kg
#                 - Body Fat: {body_fat}%
#                 - Muscle Mass: {muscle_mass} kg
#                 - Notes: {notes}

#                 Include these sections in your analysis:
#                 ## Metrics Analysis
#                 ## Recommendations
#                 ## Next Steps
#                 """
#             }
#         ]
        
#         return self.api_client.call_api(messages)


from .api_client import GroqAPIClient
from .config import Config
from .calculators import FitnessCalculators

class FitnessAssistant:
    def __init__(self):
        """Initialize Fitness Assistant"""
        self.api_client = GroqAPIClient()
        self.plan_templates = Config.PLAN_TEMPLATES
        self.calculators = FitnessCalculators()

    def generate_fitness_plan(self, goal, fitness_level, duration, calories=None):
        """Generate a personalized fitness plan"""
        template = self.plan_templates.get(goal, self.plan_templates['weight_loss'])
        
        messages = [
            {
                "role": "system",
                "content": """You are an expert fitness coach creating personalized workout plans. 
                Format your response in Markdown with proper headings (#, ##), lists (1., 2., -), 
                and emphasis (**bold**, *italic*) where appropriate."""
            },
            {
                "role": "user",
                "content": f"""
                Create a {duration}-week fitness plan with:
                Goal: {goal}
                Fitness Level: {fitness_level}
                Daily Calories: {calories if calories else 'Maintenance'}
                
                Structure your response with these sections using proper Markdown formatting:
                # Personalized Fitness Plan
                ## Program Overview
                ## Weekly Schedule
                ## Exercise Details
                ## Nutrition Guidelines
                ## Progress Tracking
                ## Safety Tips
                
                Base the plan on: {template}
                """
            }
        ]
        
        return self.api_client.call_api(messages)

    def generate_home_workout(self, fitness_level, duration, target_area=None):
        """Generate a home workout plan"""
        messages = [
            {
                "role": "system",
                "content": """You are an expert home workout coach creating equipment-free workout plans. 
                Focus on bodyweight exercises and minimal space requirements."""
            },
            {
                "role": "user",
                "content": f"""
                Create a {duration}-week home workout plan with:
                Fitness Level: {fitness_level}
                Target Area: {target_area if target_area else 'Full Body'}
                
                Include:
                # Home Workout Plan
                ## Overview
                ## Weekly Schedule (with rest days)
                ## Exercise Details (with form tips)
                ## Space Requirements
                ## Alternative Exercises
                ## Progress Tracking
                """
            }
        ]
        
        return self.api_client.call_api(messages)

    def generate_jawline_exercises(self, duration):
        """Generate jawline exercise routine"""
        messages = [
            {
                "role": "system",
                "content": """You are an expert in facial exercises and muscle toning."""
            },
            {
                "role": "user",
                "content": f"""
                Create a {duration}-week jawline exercise routine that includes:
                # Jawline Exercise Program
                ## Daily Routine
                ## Exercise Descriptions
                ## Proper Form Guide
                ## Progress Pictures Guide
                ## Tips and Precautions
                ## Expected Timeline
                """
            }
        ]
        
        return self.api_client.call_api(messages)

    def generate_calisthenics_plan(self, fitness_level, duration, focus_skills=None):
        """Generate a calisthenics training plan"""
        messages = [
            {
                "role": "system",
                "content": """You are an expert calisthenics coach creating progressive bodyweight mastery programs."""
            },
            {
                "role": "user",
                "content": f"""
                Create a {duration}-week calisthenics plan with:
                Fitness Level: {fitness_level}
                Focus Skills: {focus_skills if focus_skills else 'Basic fundamentals'}
                
                Include:
                # Calisthenics Training Plan
                ## Skill Progression Roadmap
                ## Weekly Schedule
                ## Exercise Progressions
                ## Mobility Work
                ## Form Guidelines
                ## Progress Benchmarks
                ## Safety Considerations
                """
            }
        ]
        
        return self.api_client.call_api(messages)

    def calculate_bmi(self, weight, height):
        """Calculate BMI"""
        return self.calculators.calculate_bmi(weight, height)

    def analyze_progress(self, weight, body_fat, muscle_mass, notes):
        """Analyze fitness progress and provide recommendations"""
        messages = [
            {
                "role": "system",
                "content": """You are an expert fitness coach analyzing progress data."""
            },
            {
                "role": "user",
                "content": f"""
                Analyze these fitness metrics and provide feedback:
                
                # Progress Analysis Report
                
                ## Current Metrics
                - Weight: {weight} kg
                - Body Fat: {body_fat}%
                - Muscle Mass: {muscle_mass} kg
                - Notes: {notes}

                Include these sections in your analysis:
                ## Metrics Analysis
                ## Recommendations
                ## Next Steps
                """
            }
        ]
        
        return self.api_client.call_api(messages)
