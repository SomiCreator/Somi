import time
import os
import sys
import random

if __name__ == "__main__" and __package__ is None:
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    __package__ = "somi"

from somi.auth import authenticate_to_twitter
from somi.ai_brain import generate_tweet, generate_response
from somi.logger import setup_logger

logger = setup_logger("Somi")

def print_letter_by_letter(text, delay_range=(0.01, 0.05)):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(random.uniform(*delay_range))
    print()  # New line at the end

def display_startup_effect():
    print("\n" * 2)
    startup_messages = [
        "Initializing Somi...\n",
        "Loading AI modules...\n",
        "Connecting to Twitter API...\n",
        "Calibrating response algorithms...\n",
        "Warming up tweet generator...\n",
        "🔑 Authenticating to Twitter API...\n",
        "✅ Authenticated to Twitter API\n",
        "🚀 Somi is now online and ready to interact! 🌐"
    ]
    
    for message in startup_messages:
        print_letter_by_letter(message)
        time.sleep(0.5)
    
    print_letter_by_letter("\nStartup complete!")
    time.sleep(1)
    print("\n" * 2)

def simulate_interaction():
    tweet = generate_tweet()
    print_letter_by_letter(f"User tweet: {tweet}")
    logger.info(f"log saved: {tweet}")

    response = generate_response(tweet)
    print_letter_by_letter(f"AI response: {response}")
    logger.info(f"log saved: {response}")

    print_letter_by_letter("\n" + "-"*50 + "\n")

def main():
    display_startup_effect()

    # Authenticate to Twitter API
    
    time.sleep(1)
    print()  # Add an extra newline for spacing

    while True:
        try:
            simulate_interaction()
            time.sleep(2)  # Wait for 2 seconds between interactions
        except KeyboardInterrupt:
            print_letter_by_letter("\nShutting down Somi. Goodbye!")
            break
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            print_letter_by_letter("An error occurred. Please check the logs.")
            time.sleep(5)

if __name__ == "__main__":
    main()
