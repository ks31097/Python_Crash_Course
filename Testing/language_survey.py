from survey import AnonymousServey

"""Defining a question by creating an AnonymousServey instance."""
question = "What language did you first learn to speak?"
my_servey = AnonymousServey(question)

"""Displaying the question and saving the answers"""
my_servey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_servey.store_response(response)

"""Output of survey results."""
print("\nThank you to everyone who participated in the survey!")
my_servey.show_results()