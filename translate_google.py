import six
from google.cloud import translate_v2 as translate


def translate_text(text):
    """Translates text into the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language='en', source_language='ko')
    # print(sorted(dir(translate_client)))
    # print(translate_client.getResponce(text, target_language='en', source_language='ko'))
    # print(u"Text: {}".format(result["input"]))
    # print(u"Translation: {}".format(result["translatedText"]))
    return result["translatedText"]

if __name__ == "__main__":
    print(translate_text("오후 해가 저물어"))
