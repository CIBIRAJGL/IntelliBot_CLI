# 🧠 IntelliBot_CLI: LangChain-Powered AI Utility Assistant

A powerful command-line AI assistant powered by LangChain + OpenAI, featuring useful tools like math operations, unit conversion, date calculations, password strength checker, jokes, quotes, and more.

## 🚀 Features

- 🧮 Basic math operations (add, subtract, multiply, divide)
- 📏 Unit converter (imperial ↔ SI)
- 🕓 Current date & time
- 📅 Days between two dates
- 🔐 Password strength checker
- 😂 Joke generator
- 💡 Quote of the day

## 📂 Project Structure

```
.
├── IntelliBot_CLI.py    # Main executable script
├── .env                 # Your OpenAI API key (not committed)
├── .env.example         # Template for environment setup
├── requirements.txt     # Required Python packages
├── README.md            # Project overview
```

## 🛠 Setup Instructions

1. Clone the repository:
   ```bash
   # Clone YOUR repository (replace with your actual GitHub URL)
   git clone https://github.com/CIBIRAJGL/IntelliBot_CLI.git
   cd IntelliBot_CLI
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a .env file:
   ```bash
   touch .env
   ```

4. Add your OpenAI API key to .env:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```

5. Run the assistant:
   ```bash
   python main.py
   ```

## 🧪 Example Usage

```bash
You: what's 5 multiplied by 12?
Assistant: 5 * 12 = 60

You: convert 10 inches to cm
Assistant: 10 inch is 25.4 cm

You: days between 2024-01-01 and 2025-01-01
Assistant: There are 366 days between 2024-01-01 and 2025-01-01.
```

## 🔐 Environment Variables

| Key             | Description            |
|-----------------|------------------------|
| OPENAI_API_KEY  | Your OpenAI API key    |

Create a .env file or use Streamlit Secrets (if adapting for web).

## 📜 License

This project is licensed under the MIT License.

---

Made with ❤️ using LangChain + OpenAI
