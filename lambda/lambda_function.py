# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import os
import random
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_s3.adapter import S3Adapter
s3_adapter = S3Adapter(bucket_name=os.environ["S3_PERSISTENCE_BUCKET"])

from ask_sdk_model import Response
from ask_sdk_core.skill_builder import CustomSkillBuilder


#crowd applause <audio src="soundbank://soundlibrary/human/amzn_sfx_crowd_applause_01"/>
#Elephant Sound <audio src="soundbank://soundlibrary/animals/amzn_sfx_elephant_05"/>
#chew sound <audio src="soundbank://soundlibrary/toys_games/board_games/board_games_01"/>

questions=[
    'what are your ears for? your options are, listening or eating'
     ]
answers=[
   'listening'
    ]
finishedbite=[
    'you are soooo sweet!!! Let me ask you a question.',
    'wow!!! very good. Let me ask you a question.',
    'Awesome!!! Let me ask you a question.'
    ]

intro=''' I am your meal friend Alexa. we will have meal together. I will have my bite and you have your bite. After finished your bite, you
        should tell me finished friend. or if you are still having your bite, you should say me wait friend so that i will wait for you.
        after each bytes i will be having games and surprises for you. So untill you finish your meal you will be having lots of surprises. Everyday you will be having
        different games and surprises. So come lets have meal and have fun.'''

ques=[
    'What are we going to have now?',
    "What's there on your plate?",
    'What your mom prepared for you?'
]
musiq=[
    '<audio src="soundbank://soundlibrary/musical/amzn_sfx_drum_comedy_01"/>',
    '<audio src="soundbank://soundlibrary/musical/amzn_sfx_drum_and_cymbal_01"/>'
    ]
foodsen=[
    'Wow!!! i love it let’s have it together, I am having my bite.',
    'wow!!! Sounds Yummy. lets have it together,I am having my bite.',
    'wow!!! is it? come lets have it together, I am having my bite.'
    ]
greetingsen=[
    'hi!!! I am your meal friend and you know i am your best friend',
    'Hellooo!! I am your meal friend and i am happy to have meal with you.',
    'Welcome to meal friend. I was waiting for you to have meal and have fun.',
    'Hey I am your meal friend and you are my meal friend.',
    'Hey Meal friend lets have fun together'
    ]
greetingsen1=[
    'hi!!! I am your meal friend.  and you know i am your best friend.',
    'Hellooo!! I am your meal friend and i am happy to have meal with you.',
    'Welcome to meal friend.I was waiting for you to have meal and have fun.',
    'Hey I am your meal friend and you are my meal friend.',
    'Hey Meal friend lets have fun together.'
    ]
happysen=[
    'wow!!! so tasty!!!!, lets have next byte.',
    'very good, come lets have next byte together.',
    'very delicious right? can not wait to have next byte? shall we?.',
    'You are so sweet!!! lets have next byte.'
    ]
trysen=[
    "ok. have it. chew food properly. and i am waiting for your reply",
    "our elephant friend is waiting for us. have it fast. waiting for your reply",
    "i was hungry so had is fast. you have it slowly. waiting for your reply",
    "food is very important for us. so dont waste, have it. waiting for your reply"
    ]
nextbite=[
    'very good!!! lets have next bite.',
    'superb!!! come lets have next bite',
    'Awesome!!! lets have next bite'
        ]
gamesen=[
    'you are sooo sweet!!! come,lets paly a game now.',
    'very good!!! come, lets play a game',
    'wow!!!! superb!!! come, lets play a game now'
    ]
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
finished=0
class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
       # var1 = "Hi!!! I am your meal friend Alexa. Come, lets have meal together."
        attr = handler_input.attributes_manager.persistent_attributes
        attributes_are_present = "name" in attr
        #name=attr['name']
        if  attributes_are_present:
            name=attr['name']
            speech_text="welcome back "+name+"!!!!"+ " Are you ready to have meal and play games with me? You can say me play "  
            return handler_input.response_builder.speak(speech_text).ask(speech_text).response
        else:

            ques1= 'Let me know about you, so that i will remember when you come back. '
            ques2= 'My name is Alexa. What is your name?' 
           # welcome_msg = random.choice(greetingsen1)
            welcome_msg="Welcome to meal friend."
            ques_msg = random.choice(ques1)
            musiq_msg = random.choice(musiq)
       # speech_text = ('<emphasis level="strong">'+var1+'</emphasis> '
          #             '<amazon:emotion name="excited" intensity="low">'+var2+'</amazon:emotion>')
       # speech_text = ('<speak><say-as interpret-as="interjection">'+var1+'</say-as>''<audio src="soundbank://soundlibrary/magic/amzn_sfx_fairy_melodic_chimes_01"/>'
        #              '<amazon:emotion name="excited" intensity="high">'+var2+'</amazon:emotion>''<say-as interpret-as="interjection">'+var3+'</say-as></speak>')
       # speech_text = ('<speak><say-as interpret-as="interjection">'+var1+'</say-as>''<audio src="soundbank://soundlibrary/musical/amzn_sfx_drum_and_cymbal_01"/>'
        #             '<say-as interpret-as="interjection">'+var2+'</say-as>''<say-as interpret-as="interjection">'+var3+'</say-as></speak>')
        #speech_text = ('<speak>'+var1+'<audio src="soundbank://soundlibrary/musical/amzn_sfx_drum_and_cymbal_01"/>'+var2+'</speak>')
            speech_text = ( welcome_msg+musiq_msg+ques1+'<break time="2s"/>'+ques2)
       # speech_text = ( "<speak> This is Alexa's regular speech, followed by the sound effect named Bear Groan Roar (1)."
  #'<audio src="soundbank://soundlibrary/animals/amzn_sfx_bear_groan_roar_01"/></speak>')
            return handler_input.response_builder.speak(speech_text).ask(speech_text).response

'''class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
       # var1 = "Hi!!! I am your meal friend Alexa. Come, lets have meal together."
        welcome_msg = random.choice(greetingsen)
        ques_msg = random.choice(ques)
        musiq_msg = random.choice(musiq)
       # speech_text = ('<emphasis level="strong">'+var1+'</emphasis> '
          #             '<amazon:emotion name="excited" intensity="low">'+var2+'</amazon:emotion>')
       # speech_text = ('<speak><say-as interpret-as="interjection">'+var1+'</say-as>''<audio src="soundbank://soundlibrary/magic/amzn_sfx_fairy_melodic_chimes_01"/>'
        #              '<amazon:emotion name="excited" intensity="high">'+var2+'</amazon:emotion>''<say-as interpret-as="interjection">'+var3+'</say-as></speak>')
       # speech_text = ('<speak><say-as interpret-as="interjection">'+var1+'</say-as>''<audio src="soundbank://soundlibrary/musical/amzn_sfx_drum_and_cymbal_01"/>'
        #             '<say-as interpret-as="interjection">'+var2+'</say-as>''<say-as interpret-as="interjection">'+var3+'</say-as></speak>')
        #speech_text = ('<speak>'+var1+'<audio src="soundbank://soundlibrary/musical/amzn_sfx_drum_and_cymbal_01"/>'+var2+'</speak>')
        speech_text = ( welcome_msg+musiq_msg+ques_msg)
       # speech_text = ( "<speak> This is Alexa's regular speech, followed by the sound effect named Bear Groan Roar (1)."
  #'<audio src="soundbank://soundlibrary/animals/amzn_sfx_bear_groan_roar_01"/></speak>')
        return handler_input.response_builder.speak(speech_text).ask(speech_text).response
     
 
class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("LaunchRequest")(handler_input)
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Welcome, you can say Hello or Help. Which would you like to try?"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
                  attr = handler_input.attributes_manager.persistent_attributes
        name = attr['name']
        if name:
            speak_output = 'Welcome back '+name
            handler_input.response_builder.speak(speak_output)
            return handler_input.response_builder.response
        else:
       
        )'''
class HasBirthdayLaunchRequestHandler(AbstractRequestHandler):
    """Handler for launch after they have set their birthday"""

    def can_handle(self, handler_input):
        # extract persistent attributes and check if they are all present
        attr = handler_input.attributes_manager.persistent_attributes
        attributes_are_present = "name" in attr 

        return attributes_are_present and ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        attr = handler_input.attributes_manager.persistent_attributes
        name = attr['name']
        

        # TODO:: Use the settings API to get current date and then compute how many days until user's bday
        # TODO:: Say happy birthday on the user's birthday

        speak_output = 'Welcome back '+ name
        handler_input.response_builder.speak(speak_output)

        return handler_input.response_builder.response

class NameIntentHandler(AbstractRequestHandler):
    """Handler for Name Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("NameIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        name = slots["name"].value
        attributes_manager = handler_input.attributes_manager
        kid_attributes = {
            "name": name,
            "index": 0,
            "count": 0,
            "points": 0
        }
        attributes_manager.persistent_attributes = kid_attributes
        attributes_manager.save_persistent_attributes()
        #var1=random.choice(musiq)
        var2= "Sweet name "+name
        var3=" How old are you? "
        speak_output = ( var2+'<break time="2s"/>'+ var3)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
class FinishedIntentHandler(AbstractRequestHandler):
    """Handler for Happy Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("FinishedIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        #speak_output = "You are a good girl!!! lets have next byte."
        num=random(0,len(questions)-1)
        attributes_manager = handler_input.attributes_manager
        kid_attributes = {
            "index":num,
            "count":0,
            "points":0
            
        }
        
        attributes_manager.persistent_attributes = kid_attributes
        attributes_manager.save_persistent_attributes()
        #var1=random.choice(musiq)
        var2= questions[kid_attributes["index"]]
        speak_output= random.choice(finishedbite)+'<break time="1s"/>'+var2
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
class QuizIntentHandler(AbstractRequestHandler):
    """Handler for Name Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("QuizIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        #var1=random.choice(musiq)
       # attr = handler_input.attributes_manager.session_attributes
        
        slots = handler_input.request_envelope.request.intent.slots
        ans = slots["list_of_answers"].value
        attr = handler_input.attributes_manager.persistent_attributes
        n=attr["index"]
        ans1=answers[n]
        #if ans==anwers[attr["quesindex"]]:
        attr_ans= "index" in attr
        if ans==ans1:
            n=attr["index"]
            speak_output ="Very good!!!! right answer"
            return (
                        handler_input.response_builder
                            .speak(speak_output)
                            .ask(speak_output)
                            .response
                    ) 
        else:
            speak_output = "Sorry!!! The correct answer is "+ans1
            return (
                        handler_input.response_builder
                            .speak(speak_output)
                            .ask(speak_output)
                            .response
                    ) 
    
class AgeIntentHandler(AbstractRequestHandler):
    """Handler for Which Food Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AgeIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        #var1=random.choice(musiq)
        #var1= "Are you ready to have meal and play games with me? "
        var2= "Thank You. I will remember you. "
        var3=" Do you want to know more about me?  "
        speak_output = ( var2+'<break time="2s"/>'+var3)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
class PlayIntentHandler(AbstractRequestHandler):
    """Handler for Which Food Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("PlayIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        #var1=random.choice(musiq)
        var1= random.choice(ques)
        speak_output = var1
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
class YesIntentHandler(AbstractRequestHandler):
    """Handler for Which Food Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("YesIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        var1= " Are you ready to have meal and play games with me? "
        speak_output = intro+'<break time="2s"/>'+var1
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
'''class GenderIntentHandler(AbstractRequestHandler):
    """Handler for Which Food Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("GenderIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        var1=random.choice(musiq)
        var2= "Thank You. I will remember you. "
        var3=" Do you want to know more about me?  "
        speak_output = ( var2+'<break time="3s"/>'+ var3)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )'''
class WhichFoodIntentHandler(AbstractRequestHandler):
    """Handler for Which Food Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("WhichFoodIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        var1=random.choice(foodsen)
        var2= "did you finish your bite? you can say me finished, or wait."
        speak_output = ('<speak>'+var1+'<audio src="soundbank://soundlibrary/toys_games/board_games/board_games_01"/><break time="3s"/>'+var2+'</speak>')
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class HappyIntentHandler(AbstractRequestHandler):
    """Handler for Happy Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HappyIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
      #  speak_output=random.choice(happysen)("<speak>"'<audio src="soundbank://soundlibrary/foley/amzn_sfx_swoosh_cartoon_fast_01"/></speak>')
        quiz=random.choice(questions)
        var1=random.choice(finishedbite)
        speech_text= var1+'<break time="1s"/>'+quiz
        #speak_output = ("<speak> wow!!! so tasty, lets have next byte."
        #'<audio src="soundbank://soundlibrary/foley/amzn_sfx_swoosh_cartoon_fast_01"/></speak>')
        return handler_input.response_builder.speak(speech_text).ask(speech_text).response
''' return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )'''
class TryAgainIntentHandler(AbstractRequestHandler):
    """Handler for Happy Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("TryAgainIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        speak_output=random.choice(trysen)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class HelloWorldIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HelloWorldIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Hello World"

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


#sb = SkillBuilder()
sb = CustomSkillBuilder(persistence_adapter=s3_adapter)


sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HasBirthdayLaunchRequestHandler())
sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(WhichFoodIntentHandler())
sb.add_request_handler(NameIntentHandler())
sb.add_request_handler(AgeIntentHandler())
sb.add_request_handler(PlayIntentHandler())
sb.add_request_handler(QuizIntentHandler())
sb.add_request_handler(YesIntentHandler())
sb.add_request_handler(HappyIntentHandler())
sb.add_request_handler(TryAgainIntentHandler())
sb.add_request_handler(FinishedIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()