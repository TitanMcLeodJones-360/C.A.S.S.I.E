import speech_recognition as sr
import logging

class CommandInput:
    def __init__(self):
        self.voice_mode = self.check_microphone()

    def check_microphone(self):
        """
        Checks if a microphone is available. Returns True if detected.
        """
        try:
            with sr.Microphone() as source:
                logging.info("Microphone detected.")
                return True
        except OSError:
            logging.warning("No microphone detected. Switching to text input mode.")
            return False

    def get_voice_command(self):
        """
        Uses voice recognition to get a command from the user.
        """
        recognizer = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Listening for your command...")
                recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            logging.info(f"Voice command received: {command}")
            return command.lower()
        except sr.UnknownValueError:
            logging.error("Voice recognition could not understand the audio.")
            return "error: could not understand audio"
        except sr.RequestError as e:
            logging.error(f"Could not request results from speech recognition service; {e}")
            return "error: speech recognition service error"

    def get_text_command(self):
        """
        Prompts the user to input a command via text.
        """
        command = input("Please type your command: ").strip()
        logging.info(f"Text command received: {command}")
        return command.lower()

    def get_command(self):
        """
        Retrieves a command based on the available input mode.
        """
        if self.voice_mode:
            return self.get_voice_command()
        else:
            return self.get_text_command()
