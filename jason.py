import json
from datetime import datetime
import random


class PersonalAssistant:
    def __init__(self, owner_name):
        self.name = "Anansh"
        self.owner = owner_name
        self.conversation_history = []
        # Load knowledge base from JSON file
        try:
            with open('knowledge_base.json', 'r') as f:
                self.knowledge_base = json.load(f)
        except FileNotFoundError:
            self.knowledge_base = {
                "general_responses": [
                    "I'm afraid I don't have enough information to answer that properly.",
                    "Could you please provide more context?",
                    "That's an interesting question. Let me try to help."
                ],
                "greetings": [
                    f"Hello {owner_name}! How can I help you today?",
                    f"Great to see you, {owner_name}!",
                    f"Hi {owner_name}! What's on your mind?"
                ]
            }

    def authenticate_user(self, provided_name):
        """Basic authentication to ensure only the owner can use the assistant"""
        return provided_name.lower() == self.owner.lower()

    def process_input(self, user_input, user_name):
        """Process user input and generate appropriate response"""
        if not self.authenticate_user(user_name):
            return "Access denied. This assistant is personalized for another user."

        # Log the interaction
        self.conversation_history.append({
            "timestamp": str(datetime.now()),
            "user_input": user_input,
            "user": user_name
        })

        # Simple keyword-based response system
        user_input_lower = user_input.lower()

        # Handle greetings
        if any(word in user_input_lower for word in ["hello", "hi", "hey"]):
            return random.choice(self.knowledge_base["greetings"])

        # Handle general queries
        # This is where you'd integrate more sophisticated response generation
        return self.generate_response(user_input)

    def generate_response(self, query):
        """
        Generate a response to user query
        This is a placeholder for more sophisticated response generation
        """
        # In a real implementation, this would include:
        # - Natural Language Processing
        # - Context understanding
        # - Response generation models
        return random.choice(self.knowledge_base["general_responses"])

    def learn_from_interaction(self, user_input, correct_response):
        """Add new knowledge to the assistant's knowledge base"""
        # This is where you'd implement learning capabilities
        pass

    def save_knowledge_base(self):
        """Save the current knowledge base to a file"""
        with open('knowledge_base.json', 'w') as f:
            json.dump(self.knowledge_base, f, indent=2)


# Example usage
def main():
    # Initialize the assistant
    owner_name = "Anansh "  # Replace with your name
    jason = PersonalAssistant(owner_name)

    print(f"Jason AI Assistant initialized for {"Anansh Jain"}")
    print("Type 'exit' to end the conversation")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            jason.save_knowledge_base()
            break

        response = jason.process_input(user_input, owner_name)
        print(f"Jason: {response}")


if __name__ == "__main__":
    main()