import AI_voice_output
import speech_conversion
import datetime
import webbrowser

def action(data):
    user_data = data.lower()

    if "what is your name" in user_data or "Who are you" in user_data:
        AI_voice_output.AI_voice_output("My name is U-Phoria, I'm your Virtual assistant!")
        return "My name is U-Phoria, I'm your Virtual assistant!"

    elif "hello" in user_data or "hey" in user_data or "hi" in user_data:
        AI_voice_output.AI_voice_output("Hello sir, how can I help you?")
        return "Hello sir, how can I help you?"

    elif "good morning" in user_data:
        AI_voice_output.AI_voice_output("Good morning sir!")
        return "Good morning sir!"

    elif "good night" in user_data:
        AI_voice_output.AI_voice_output("Good night sir! Sleep well!")
        return "Good night sir! Sleep well!"

    elif "time now" in user_data:
        current_time = datetime.datetime.now()
        Time = (str)(current_time) + " Hour :", (str)(current_time.minute) + " Minutes"
        AI_voice_output.AI_voice_output(Time)
        return Time

    elif "shut down" in user_data:
        AI_voice_output.AI_voice_output("Okay sir")
        return "Okay sir"

    elif "play music" in user_data:
        webbrowser.open("https://open.spotify.com")
        AI_voice_output.AI_voice_output("Spotify is ready!")
        return "Spotify is ready!"

    elif "youtube" in user_data:
        webbrowser.open("https://www.youtube.com")
        AI_voice_output.AI_voice_output("Youtube is ready!")
        return "Youtube is ready!"

    elif "open google" in user_data:
        webbrowser.open("https://www.google.com")
        AI_voice_output.AI_voice_output("Google is ready!")
        return "Google is ready!"

    else:
        AI_voice_output.AI_voice_output("Sir, I am not able to understand")
        return "Sir, I am not able to understand"