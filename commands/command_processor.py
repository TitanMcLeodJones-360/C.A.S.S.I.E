import openai
import logging

class CommandProcessor:
    def __init__(self, dashboard):
        """
        Initialize the CommandProcessor with a reference to the Dashboard.
        :param dashboard: An instance of the Dashboard to trigger actions.
        """
        self.dashboard = dashboard
        self.commands = {
            "open browser": self.dashboard.launch_browser,
            "run diagnostics": self.dashboard.run_diagnostics,
            "show storage": self.dashboard.show_storage_management,
            "show notifications": self.dashboard.show_notifications,
            "exit application": self.exit_application
        }
        # Load the OpenAI API Key from settings
        self.api_key = self.dashboard.browser_settings.get_settings().get("openai_api_key", "")

    def interpret_with_openai(self, command):
        """
        Use OpenAI's GPT model to interpret the user command.
        :param command: The input command string.
        :return: The interpreted command.
        """
        if not self.api_key:
            logging.error("OpenAI API Key is not set.")
            return None
        
        openai.api_key = self.api_key
        
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",  # Use a GPT model
                prompt=f"Interpret this command: {command}",
                max_tokens=50
            )
            interpreted_command = response.choices[0].text.strip().lower()
            logging.info(f"OpenAI interpreted command: {interpreted_command}")
            return interpreted_command
        except openai.error.OpenAIError as e:
            logging.error(f"OpenAI API error: {e}")
            return None

    def process_command(self, command):
        """
        Process a user command and execute the corresponding action.
        :param command: The input command string.
        """
        command = command.lower().strip()
        action = self.commands.get(command)

        if not action:
            # Try interpreting the command with OpenAI
            interpreted_command = self.interpret_with_openai(command)
            if interpreted_command:
                action = self.commands.get(interpreted_command)
        
        if action:
            logging.info(f"Executing command: {command}")
            action()
        else:
            logging.warning(f"Unknown command: {command}")
            self.dashboard.notifications.add_notification(f"Unknown command: {command}", "warning")
            self.dashboard.show_message("Unknown Command", f"The command '{command}' is not recognized.")

    def exit_application(self):
        """
        Safely exits the application.
        """
        logging.info("Exiting application...")
        self.dashboard.root.destroy()
