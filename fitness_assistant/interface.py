import gradio as gr
from .assistant import FitnessAssistant

def create_interface():
    """Create the Gradio interface"""
    assistant = FitnessAssistant()
    
    with gr.Blocks(theme=gr.themes.Soft()) as demo:
        gr.Markdown(
            """
            # 🏋️‍♂️ AI Fitness Assistant
            Your comprehensive fitness companion!
            """
        )
        
        with gr.Tabs():
            # Fitness Plan Generator Tab
            with gr.Tab("Customized Fitness Plan"):
                with gr.Row():
                    with gr.Column(scale=1):
                        goal = gr.Dropdown(
                            choices=['weight_loss', 'muscle_gain', 'strength', 'endurance'],
                            label="Fitness Goal",
                            value='weight_loss'
                        )
                        fitness_level = gr.Dropdown(
                            choices=['beginner', 'intermediate', 'advanced'],
                            label="Fitness Level",
                            value='beginner'
                        )
                        duration = gr.Slider(
                            minimum=1,
                            maximum=12,
                            value=4,
                            step=1,
                            label="Program Duration (weeks)"
                        )
                        calories = gr.Number(
                            label="Daily Calorie Target (optional)",
                            value=None
                        )
                        generate_btn = gr.Button("Generate Plan", variant="primary")
                
                    with gr.Column(scale=2):
                        plan_output = gr.Markdown(
                            label="Your Personalized Fitness Plan"
                        )

            # Home Workout Tab
            with gr.Tab("Home Workout"):
                with gr.Row():
                    with gr.Column(scale=1):
                        hw_fitness_level = gr.Dropdown(
                            choices=['beginner', 'intermediate', 'advanced'],
                            label="Fitness Level",
                            value='beginner'
                        )
                        hw_duration = gr.Slider(
                            minimum=1,
                            maximum=12,
                            value=4,
                            step=1,
                            label="Program Duration (weeks)"
                        )
                        target_area = gr.Dropdown(
                            choices=['Full Body', 'Upper Body', 'Lower Body', 'Core'],
                            label="Target Area",
                            value='Full Body'
                        )
                        hw_generate_btn = gr.Button("Generate Home Workout", variant="primary")
                    
                    with gr.Column(scale=2):
                        hw_output = gr.Markdown(
                            label="Your Home Workout Plan"
                        )

            # Jawline Exercises Tab
            with gr.Tab("Jawline Exercises"):
                with gr.Row():
                    with gr.Column(scale=1):
                        jaw_duration = gr.Slider(
                            minimum=1,
                            maximum=12,
                            value=4,
                            step=1,
                            label="Program Duration (weeks)"
                        )
                        jaw_generate_btn = gr.Button("Generate Jawline Routine", variant="primary")
                    
                    with gr.Column(scale=2):
                        jaw_output = gr.Markdown(
                            label="Your Jawline Exercise Routine"
                        )

            # Calisthenics Tab
            with gr.Tab("Calisthenics"):
                with gr.Row():
                    with gr.Column(scale=1):
                        cal_fitness_level = gr.Dropdown(
                            choices=['beginner', 'intermediate', 'advanced'],
                            label="Fitness Level",
                            value='beginner'
                        )
                        cal_duration = gr.Slider(
                            minimum=1,
                            maximum=12,
                            value=4,
                            step=1,
                            label="Program Duration (weeks)"
                        )
                        focus_skills = gr.Dropdown(
                            choices=['Basic fundamentals', 'Pull-ups', 'Push-ups', 'Handstand', 'Planche', 'L-sit'],
                            label="Focus Skills",
                            value='Basic fundamentals'
                        )
                        cal_generate_btn = gr.Button("Generate Calisthenics Plan", variant="primary")
                    
                    with gr.Column(scale=2):
                        cal_output = gr.Markdown(
                            label="Your Calisthenics Training Plan"
                        )

            # BMI Calculator Tab
            # with gr.Tab("BMI Calculator"):
            #     with gr.Row():
            #         with gr.Column(scale=1):
            #             weight = gr.Number(
            #                 label="Weight (kg)",
            #                 value=70.0
            #             )
            #             height = gr.Number(
            #                 label="Height (cm)",
            #                 value=170.0
            #             )
            #             bmi_calculate_btn = gr.Button("Calculate BMI", variant="primary")
                    
            #         with gr.Column(scale=2):
            #             bmi_output = gr.Markdown(
            #                 label="BMI Results"
            #             )
            
            # Progress Tracking Tab
            with gr.Tab("Track Progress"):
                with gr.Row():
                    with gr.Column(scale=1):
                        track_weight = gr.Number(
                            label="Current Weight (kg)",
                            value=0.0
                        )
                        body_fat = gr.Number(
                            label="Body Fat Percentage",
                            value=0.0
                        )
                        muscle_mass = gr.Number(
                            label="Muscle Mass (kg)",
                            value=0.0
                        )
                        notes = gr.Textbox(
                            label="Additional Notes",
                            lines=3
                        )
                        analyze_btn = gr.Button("Analyze Progress", variant="primary")
                
                    with gr.Column(scale=2):
                        progress_output = gr.Markdown(
                            label="Progress Analysis"
                        )
        
        # Set up button click events
        generate_btn.click(
            fn=assistant.generate_fitness_plan,
            inputs=[goal, fitness_level, duration, calories],
            outputs=plan_output
        )
        
        hw_generate_btn.click(
            fn=assistant.generate_home_workout,
            inputs=[hw_fitness_level, hw_duration, target_area],
            outputs=hw_output
        )
        
        jaw_generate_btn.click(
            fn=assistant.generate_jawline_exercises,
            inputs=[jaw_duration],
            outputs=jaw_output
        )
        
        cal_generate_btn.click(
            fn=assistant.generate_calisthenics_plan,
            inputs=[cal_fitness_level, cal_duration, focus_skills],
            outputs=cal_output
        )
        
        # bmi_calculate_btn.click(
        #     fn=assistant.calculate_bmi,
        #     inputs=[weight, height],
        #     outputs=bmi_output
        # )
        
        analyze_btn.click(
            fn=assistant.analyze_progress,
            inputs=[track_weight, body_fat, muscle_mass, notes],
            outputs=progress_output
        )

    return demo