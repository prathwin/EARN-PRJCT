import re
import random

class RuleBot:
    negative_responses = ("no", "nope", "nah", "not a chance", "sorry")
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye")
    # Random starter question
    random_questions = (
        "Why are you here?",
        "Are there any humans like you?",
        "Does Earth have a leader?",
        "What can I help you with?"
    )

    def __init__(self):
        self.alienbabble = {
            'describe_planet_intent': r'.*\s*your planet.*',
            'answer_why_intent': r'why\sare.*',
            'about_intellipat': r'.*\s*intellipat.*'
        }

    def greet(self):
        self.name = input("What is your name?\n")
        will_help = input(f"Hi {self.name}, I am Rule-Bot. Will you help me learn about your planet?\n")
        if will_help in self.negative_responses:
            print("Ok, have a nice day!")
            return
        self.chat()

    def make_exit(self, reply):
        for command in self.exit_commands:
            if reply == command:
                print("Okay, have a nice Earth day!")
                return True
        return False

    def chat(self):
        reply = input(random.choice(self.random_questions)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))

    def match_reply(self, reply):
        for key, value in self.alienbabble.items():
            intent = key
            regex_pattern = value
            found_match = re.match(regex_pattern, reply)
            if found_match and intent == 'describe_planet_intent':
                return self.describe_planet_intent()
            elif found_match and intent == 'answer_why_intent':
                return self.answer_why_intent()
            elif found_match and intent == 'about_intellipat':
                return self.about_intellipat()
        return self.no_match_intent()

    def describe_planet_intent(self):
        responses = (
            "My planet is a utopia of diverse organisms and species.\n",
            "I am from Mundaje, the capital of the Wayerd galaxy.\n"
        )
        return random.choice(responses)

    def answer_why_intent(self):
        responses = (
            "I come in peace.\n",
            "I am here to collect some human data.\n",
            "I heard that coffee is good here.\n"
        )
        return random.choice(responses)

    def about_intellipat(self):
        responses = (
            "It is the world's largest tech platform, where you can learn more about Earth.\n",
            "Come here to study and learn more!\n"
        )
        return random.choice(responses)

    def no_match_intent(self):
        responses = (
            "Please tell me more.\n",
            "Tell me more!\n",
            "Why do you say that?\n",
            "Can you elaborate?\n",
            "Interesting. Can you tell me more?\n",
            "I see. How do you think?\n",
            "Why?\n",
            "How is that possible?\n"
        )
        return random.choice(responses)

# Instantiate and start the bot
Alienbot = RuleBot()
Alienbot.greet()
