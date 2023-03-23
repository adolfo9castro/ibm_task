"""Module made translate"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def english_to_french(english_text: any):
    """Function translate English to French"""
    if english_text:
        translation = language_translator.translate(
            english_text,
            model_id='en-fr'
        ).get_result()
        return translation['translations'][0]['translation']
    return 'Bad request!', 500


def french_to_english(frensh_text: any):
    """Function translate French to English"""
    if frensh_text:
        translation = language_translator.translate(
            frensh_text,
            model_id='fr-en'
        ).get_result()
        return translation['translations'][0]['translation']
    return 'Bad request!', 500


def spanish_to_english(spanish_text):
    """Function translate Spanish to English"""
    if spanish_text:
        translation = language_translator.translate(
            spanish_text,
            model_id='es-en'
        ).get_result()
        return translation
    return 'Bad request!', 500
