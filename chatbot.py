def get_response(user_input):

  text = user_input.lower().strip()
  if text in ("hi", "hello", "hey"):
    return "Hi!"
  elif text in ("how are you", "how's it going"):
    return "I'm fine, what's about you?"
  elif text in ("what's your name", "who are you"):
    return "I'm a Python chatbot."
  elif text in ("help", "help me"):
    return "Sure! I can help you with basic questions."
  elif text in ("bye", "goodbye"):
    return "Goodbye!"
  else:
    return "I don't understand that."

def main():
  print("Welcome to the Python Chatbot! Type 'bye' to exit.")
  while True:
    user_input = input("You: ")
    response = get_response(user_input)
    print("Chatbot:", response)
    if user_input.lower().strip() == "bye":
      break 

if __name__ == "__main__":
  main()