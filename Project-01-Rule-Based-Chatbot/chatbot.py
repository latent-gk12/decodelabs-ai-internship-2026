from responses import responses


def get_response(user_input):
    user_input = user_input.lower().strip()

    if user_input == "exit":
        return None

    for key in responses:
        if key in user_input:
            return responses[key]

    return "Sorry, I don't understand that. Please try another question."