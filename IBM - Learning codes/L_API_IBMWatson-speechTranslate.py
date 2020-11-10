from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3

authenticator = IAMAuthenticator('i6rvGnsL06Ihx4kuzyjMrM2OozIk9hmF4X7KPV2lhz_I')
s2t = SpeechToTextV1(
    authenticator=authenticator
)

s2t.set_service_url('https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/65cccc98-904f-4a3a-a7f6-4983cd9a0526')

filename = "hellothisispython.mp3"

with open(filename, mode = "rb") as wav:
    response = s2t.recognize(audio = wav, content_type = 'audio/mp3')
    # See results with response.result

    recognized_text = response.result['results'][0]["alternatives"][0]["transcript"]
    print(recognized_text)

authenticator = IAMAuthenticator('lmFd080qJqzExMb0cZKTxpRhTAQrcwKEIw8IFXVCba6f')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/83dd1249-c0c5-4859-a1ef-cb1e067d13ef')

# print(language_translator.list_identifiable_languages().get_result())

translation_response = language_translator.translate(text = recognized_text, model_id = 'en-es')
translation = translation_response.get_result()
print(translation)
