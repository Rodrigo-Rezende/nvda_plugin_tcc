# Add-on development example using NVDA speech with error handling and navigating to error line

import nvdaControllerClient # Import the NVDA controller client for speech functionality

class GlobalPlugin:

    def __init__(self):
        self.error_line = None  # Variable to store the line number where the error occurred

    def script_readCode(self, gesture):
        try:
            # Get code input from the user
            code_to_read = self.getInput("Enter the code to be read:", "Code Input")

            # Check if the user provided code
            if code_to_read:
                # Execute the code
                exec(code_to_read)

                # Initialize NVDA controller client
                controller = nvdaControllerClient.Controller()

                # Split the code into lines
                lines = code_to_read.split('\n')

                # Read each line along with the line number
                for line_num, line in enumerate(lines, start=1):
                    # Use NVDA's speech to read the line number and code
                    controller.speakText(f"Line {line_num}: {line}")

        except Exception as e:
            # Handle exceptions by storing the error message and line number
            self.error_line = line_num
            controller.speakText(f"Error: {str(e)}")

    def script_goToErrorLine(self, gesture):
        if self.error_line is not None:
            # Navigate to the line where the error occurred
            self.goToLine(self.error_line)

    def goToLine(self, line_number):
        #Implement going to the line of code with the error
        pass

    __gestures = {
        "kb:NVDA+C": "readCode",
        "kb:NVDA+G": "goToErrorLine"
    }
