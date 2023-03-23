"""Classes and functions used in my project"""
import random
from IPython.display import IFrame

# general suggestions for user struggling with mental health
suggestion = ["Take a deap breath.",
              "Remember to drink water and stay hydrated",
              "Take a 10 minute walk to get your body moving.",
              "Show gratitude to someone in your life.",
              "Unwind with your favorite hobby or video.",
              "Take a 30 minute break from social media.",
              "Step outside and get some fresh air."
              "Journal your thoughts in a notebook",
              "Eat a delicious or nutritious meal and savor it."]

# general affirmations for mental health
affirmation = ["You got this!",
               "Everything will be okay.",
               "Everything happens for a reason",
               "Don't live in the past. Forgive and learn from your mistakes.",
               "You are loved.",
               "Trust that there is something better in store for you.",
               "This is not the end, this is only the beginning."]

def describe_depression():
    """ Prints a description of depression with depression resources.

            Returns
            ----------
            depression_description : string
                description of depression and its resources
    """
    depression_description = ("Depression (also called major depressive disorder or clinical depression) is a common but serious mood disorder. It causes severe symptoms that affect how you feel, think, and handle daily activities, such as sleeping, eating, or working.\n" + 
    "Here are some links that could be helpful: \n" +
    "SAMHSA National hotline: (800) 662-4357 \n" +
    "Suicide Prevention Hotline: 988")
    
    print(depression_description)

def describe_anxiety():
    """ Prints a description of anxiety with anxiety resources.

            Returns
            ----------
            anxiety_description : string
                description of depression and its resources
    """
    
    anxiety_description = ("There are several types of anxiety disorders, including generalized anxiety disorder, panic disorder, social anxiety disorder, and various phobia-related disorders.\n" + 
    "Here are some links that could be helpful: \n" + 
    "(NAMI) Helpline: 1-800-950-NAMI (6264) \n" + 
    "CallHOPE Hotline: (833) 317-HOPE (4673)")
    
    print(anxiety_description)
    
def describe_ed():
    """ Prints a description of an eating disorder with eating disorder resources.

            Returns
            ----------
            ed_description : string
                description of depression and its resources
    """
    
    ed_description = ("Eating disorders are actually serious and often fatal illnesses that are associated with severe disturbances in people’s eating behaviors and related thoughts and emotions.\n" + 
    "Here are some links that could be helpful: \n" + 
    "National Eating Disorders Association (NEDA): 1-(800)-931-2237 \n" + 
    "Eating Disorder Helpline: 1-(888)-375-7767")
    
    print(ed_description)
    
def describe_ptsd():
        """ Prints a description of post traumatic stress order with resources.

            Returns
            ----------
            ptsd_description : string
                description of ptsd and its resources
    """
        ptsd_description = ("Post-traumatic stress disorder (PTSD) is a disorder that develops in some people who have experienced a shocking, scary, or dangerous event.\n" +
    "Here are some links that could be helpful: \n" + 
    "Veteran Combat Call Center: 1 (877) 927-8387 \n" + 
    "Suicide Prevention Hotline: 988 and Press 1") 
        
        print(ptsd_description)
    
class User:
    """ The constructor (__init__) takes inputs name, age, and previous mental health conditions
    """
    def __init__(self, name, age, prev_conditions):
        self.name = name
        self.age = age
        self.prev_conditions = prev_conditions

# dictionary of users        
users = {}

def add_user(name, age, prev_conditions):
        users[name] = User(name, age, prev_conditions)
        """ adds User's name to list users.

            Parameters
            ----------
            name : string
                User's name.
        """    

def help_user():
    """ Greets user and asks what they can assist with.

            Parameters
            ----------
            user_input : string
                User's response to the question asked.

            Returns
            ----------
            random.choice(suggestion) : string
                Returns random string from suggestion list.

            random.choice(affirmation) : string
                Returns random string from affirmation list.
                
            describe_depression : string
                Returns description of depression and resources
            
            describe_anxiety : string
                Returns description of anxiety and resources
            
            describe_ed : string
                Returns description of eating disorder and resources
            
            describe_ptsd : string
                Returns description of PTSD and resources
                
            panick_attack : display(IFrame)
                Opens an embeded youtube video on breathing.
                        
     """
    name = input("What is your name? \n")
    age = input("What is your age? \n")
    prev_conditions = input("Do you have any previous mental health conditions? (Yes or No). \n")
    
    # If User is already in users, welcomes User back. If not, greets user
    if name in users:
        print("Welcome back " + name + "!")
   
    else:
        users[name] = User(name, age, prev_conditions)
        print("Hello new user " + name + "!")
    
    # Loop while talking with user and get user's response
    chat = True
    while chat:

        print("How can I help you today? (Respond with suggestion, affirmation, or your previous mental health condition).\n")
        
        # convert response to lower case
        user_input = input().lower()
        
        # If user would like a random mental health suggestion
        if "suggestion" in user_input:
            print("Sure thing. Here is a reminder to take care of your mental health: ")
            print(random.choice(suggestion))
        
        # If user wants positive affirmations
        elif "affirmation" in user_input:
            print("Here's a positive affirmation: ")
            print(random.choice(affirmation))
    
        # If user expriences depression, prints depression description and resources
        elif "depression" in user_input:
            describe_depression()
        
        # If user expriences anxiety, prints anxiety description and resources
        elif "anxiety" in user_input:
            describe_anxiety()
            
        # If user has eating disorder, prints description and resources
        elif "eating disorder" in user_input:
            describe_ed()
            
        # If user expriences PTSD, prints PTSD description and resources
        elif "ptsd" in user_input:
            describe_ptsd()
            
        # If user has panic attack, plays a breathing video in another window    
        elif "panic attack" in user_input:
            url = 'https://www.youtube.com/embed/bF_1ZiFta-E'
            display(IFrame(url, width = 560, height = 315))
       
        # If not able to be answered by chatbot, print they cannot help
        else:
            print("I'm sorry, I am unable to help you with that.")
            continue
        
        # Asks if there is anything else they can help with
        print("Is there anything else I can help you with? (Yes or No)")
        user_input = input().lower()
        
        # If yes, ask user what they need help with
        if user_input == "yes":
            print("Sure. What else can I do for you?")
            continue
        
        # If not, close chat
        elif user_input == "no":
            print("Okay, have a great day!")
            break
