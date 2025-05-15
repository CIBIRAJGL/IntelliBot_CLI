import re
from datetime import datetime
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import random

load_dotenv()

# 1. Basic Math Tool
@tool
def basic_math(operation: str, a: float, b: float) -> str:
    """Performs basic math operations: add, subtract, multiply, divide."""
    if operation == "add":
        return f"{a} + {b} = {a + b}"
    elif operation == "subtract":
        return f"{a} - {b} = {a - b}"
    elif operation == "multiply":
        return f"{a} * {b} = {a * b}"
    elif operation == "divide":
        if b == 0:
            return "Error: Cannot divide by zero."
        return f"{a} / {b} = {a / b}"
    else:
        return "Unsupported operation. Use add, subtract, multiply, or divide."

# 2. Unit Converter Tool
@tool
def unit_converter(unit_from: str, unit_to: str, value: float) -> str:
    """Converts between common SI and imperial units: inches<->cm, lbs<->kg, miles<->km, Fahrenheit<->Celsius."""
    conversions = {
        ("inch", "cm"): lambda x: x * 2.54,
        ("cm", "inch"): lambda x: x / 2.54,
        ("lb", "kg"): lambda x: x * 0.453592,
        ("kg", "lb"): lambda x: x / 0.453592,
        ("mile", "km"): lambda x: x * 1.60934,
        ("km", "mile"): lambda x: x / 1.60934,
        ("c", "f"): lambda x: (x * 9/5) + 32,
        ("f", "c"): lambda x: (x - 32) * 5/9,
    }

    key = (unit_from.lower(), unit_to.lower())
    if key in conversions:
        result = conversions[key](value)
        return f"{value} {unit_from} is {round(result, 2)} {unit_to}"
    else:
        return "Conversion not supported."

# 3. Current Datetime Tool
@tool
def current_datetime() -> str:
    """Returns the current date and time."""
    now = datetime.now()
    return now.strftime("Current date and time: %Y-%m-%d %H:%M:%S")

# 4. Days Between Dates Tool
@tool
def days_between(start_date: str, end_date: str) -> str:
    """Calculates the number of days between two dates. Format: YYYY-MM-DD"""
    try:
        d1 = datetime.strptime(start_date, "%Y-%m-%d")
        d2 = datetime.strptime(end_date, "%Y-%m-%d")
        delta = abs((d2 - d1).days)
        return f"There are {delta} days between {start_date} and {end_date}."
    except ValueError:
        return "Please use date format YYYY-MM-DD."

# 5. Password Strength Checker
@tool
def password_strength(password: str) -> str:
    """Evaluates the strength of a password and offers tips."""
    length = len(password)
    categories = sum(bool(re.search(p, password)) for p in [r"[A-Z]", r"[a-z]", r"[0-9]", r"[!@#$%^&*]"])
    
    if length >= 12 and categories == 4:
        return "✅ Strong password."
    elif length >= 8 and categories >= 3:
        return "🟡 Moderate password. Consider adding more symbols or uppercase letters."
    else:
        return "🔴 Weak password. Use 12+ characters, mix upper/lowercase, numbers & symbols."

# 6. Joke Generator
@tool
def joke_generator() -> str:
    """Tells a random joke."""
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why did the computer show up late to work? It had a hard drive.",
        "Why do Java developers wear glasses? Because they don't see sharp.",
    ]
    return random.choice(jokes)

# 7. Quote of the Day
@tool
def quote_of_the_day() -> str:
    """Returns a motivational quote."""
    quotes = [
        "Believe you can and you're halfway there. – Theodore Roosevelt",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
        "What you do today can improve all your tomorrows. – Ralph Marston",
    ]
    return random.choice(quotes)

# Main App
def main():
    model = ChatOpenAI(temperature=0)
    tools = [basic_math, unit_converter, current_datetime, days_between, password_strength, joke_generator, quote_of_the_day]
    agent_executor = create_react_agent(model, tools)

    print("🧠 AI Assistant is ready! Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "quit":
            print("👋 Goodbye!")
            break

        print("Assistant: ", end="")
        for chunk in agent_executor.stream({"messages": [HumanMessage(content=user_input)]}):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")
        print()

if __name__ == "__main__":
    main()
