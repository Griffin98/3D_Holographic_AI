import speech_recognition as sr


def recognize_speech_from_mic(recognizer, microphone):
    # set up the response object
    response = {
        "error": None,
        "transcription": None
    }

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)


    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response


def recognize():
    NUM_OF_FAIL_PROMPT_LIMIT = 3

    # create recognizer and mic instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    for i in NUM_OF_FAIL_PROMPT_LIMIT:
        guess = recognize_speech_from_mic(recognizer,microphone)

        if guess["transcription"] and guess["error"] == None:
            break
        if guess["error"]:
            print(guess["error"])
            break
        else:
            i+=1

        print(format(guess["transcription"]))


if __name__ == "__main":
    recognize()