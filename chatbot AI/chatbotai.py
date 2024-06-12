def chatbot():
    print("Hello! I'm a simple chatbot. How can I help you today?")
    
    while True:
        user_input = input("You: ").lower()
        
        if 'hello' in user_input:
            print("Chatbot: Hello! How are you?")
        
        elif 'how are you' in user_input:
            print("Chatbot: I'm just a bunch of code, but I'm functioning as expected. How about you?")
        
        elif 'fine' in user_input or 'good' in user_input:
            print("Chatbot: That's great to hear! How can I assist you today?")
        
        elif 'help' in user_input:
            print("Chatbot: Sure, I'm here to help! What do you need assistance with?")
        
        elif 'name' in user_input:
            print("Chatbot: I don't have a name yet, but you can call me Chatbot.")
        
        elif 'bye' in user_input or 'exit' in user_input or 'quit' in user_input:
            print("Chatbot: Goodbye! Have a nice day!")
        elif 'Who created You' in user_input:
            print("i am a chatbot created by Nikhil")
            break
        
        else:
            print("Chatbot: I'm sorry, I don't understand that. Can you please retype ?")

chatbot()
