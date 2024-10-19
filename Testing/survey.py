class AnonymousServey():
    """Collection anonymous servey responses."""
    def __init__(self, question):
        """Saves the question and prepares to save the answers."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Displays a question."""
        print(self.question)

    def store_response(self, new_response):
        """Saves one response to a survey."""
        self.responses.append(new_response)

    def show_results(self):
        """Display all received responses."""
        print("Survey results: ")
        for response in self.responses:
            print(f"- {response}")