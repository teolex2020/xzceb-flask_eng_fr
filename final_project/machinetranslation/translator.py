import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('apikey')
language_translator = LanguageTranslatorV3(
    version='2018-05-01}',
    authenticator=authenticator
)

__all__=['englishToFrench']

#Translate english
def englishToFrench(englishText):
    
    language_translator.set_service_url('url')

    frenchText = language_translator.translate(
        text='Hello, how are you today?',
        model_id='en-fr').get_result()

    return frenchText

#Translate french
def frenchToEnglish(frenchText):
    
    language_translator.set_service_url('url')

    englishText = language_translator.translate(
        text='Hello, how are you today?',
        model_id='fr-en').get_result()

    return englishText