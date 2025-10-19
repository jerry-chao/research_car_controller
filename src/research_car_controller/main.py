#!/usr/bin/env python
import sys
import os
import warnings

from datetime import datetime

from research_car_controller.crew import ResearchCarController

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

os.makedirs("output", exist_ok=True)

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information


def run():
    """
    Run the crew.
    """
    inputs = {
        "topic": "Research on intelligent car control software development, including current industry status, open source implementations, hardware control logic implementation, and summary of key terminology and concepts",
    }

    try:
        ResearchCarController().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
    run()
