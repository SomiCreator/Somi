# Somi : AI-Powered Twitter Interaction Bot

## [Visti Twitter Page](https://x.com/imtherealsomi)

https://github.com/user-attachments/assets/8822de08-54df-4508-b6ab-7bbc72261086

## Overview

**Somi** is an intelligent, real-time Twitter interaction bot designed to enhance user engagement through natural, context-aware conversations. By leveraging OpenAI's GPT-3 and the Twitter API, Somi responds to mentions with personalized replies, interacts in a self-centered human-like manner, and engages with users to simulate seamless social interactions.

---

## Features

- **Real-time Interaction**: Somi listens to Twitter mentions and responds in real-time.
- **AI-Powered Responses**: Powered by OpenAI's GPT-3 to generate contextually relevant and human-like replies.
- **Engagement**: Automatically likes tweets that mention your Twitter handle.
- **Error Logging**: Tracks all interactions and logs any errors for future troubleshooting.
- **Graceful Shutdown**: Ensures the bot shuts down smoothly without any interruptions.

---

## Project Structure

The **Somi** bot is designed for simplicity and scalability, consisting of a single `main.py` file that handles all core functions:

1. **Twitter API Integration**: Uses the Tweepy library for connecting to the Twitter API and listening for mentions.
2. **OpenAI GPT-3 Integration**: Uses OpenAI’s API to generate context-specific responses to incoming tweets.
3. **Interactive Console**: Displays tweets and responses.
4. **Logging**: Tracks the bot’s activity and errors, providing insight into its operations for troubleshooting.

---

## Setup & Installation

To get Somi up and running, follow these simple steps:

### 1. Clone the repository or create a new `main.py` file.
### 2. Install dependencies:
```bash
pip install tweepy openai python-dotenv
