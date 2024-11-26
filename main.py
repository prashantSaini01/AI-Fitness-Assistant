from fitness_assistant import create_interface
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    demo = create_interface()
    #demo.launch(share=True)
    demo.launch(server_name="0.0.0.0", server_port=port)