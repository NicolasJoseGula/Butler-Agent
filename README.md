# Butler Agent

A conversational AI agent built with the **THINK → ACT → OBSERVE** loop, capable of using real-world tools to answer questions and manage state across a multi-turn conversation.

---

## Overview

Butler Agent demonstrates the core architecture of a modern LLM agent:

- **THINK** — The model reasons about what to do next based on the conversation context
- **ACT** — The agent executes a tool (function call) to interact with the real world
- **OBSERVE** — The result is added back to the context so the model can reason further

The agent can chain multiple tool calls in a single response, handle errors gracefully, and maintain memory across an entire conversation session.

---

## Features

- Multi-turn conversation with persistent context
- Real-time weather data via [WeatherAPI](https://www.weatherapi.com/)
- Wardrobe state management (get items, wash clothing)
- Tool chaining — the agent decides which tools to call and in what order
- Graceful error handling for unknown tools and missing wardrobe items
- Clean separation of concerns: client, agent loop, tools, prompts

---

## Architecture

```
Butler-Agent/
├── butler/
│   ├── client.py       # OpenAI client initialization
│   ├── agent.py        # Core THINK-ACT-OBSERVE loop
│   ├── prompts.py      # System prompt
│   └── tools/
│       ├── weather.py  # check_weather(city) — calls WeatherAPI
│       └── wardrobe.py # get_wardrobe_items(), wash_clothing(item_name)
├── tests/
│   └── test_butler.py
├── main.py             # Entry point — continuous conversation loop
├── .env.example
└── requirements.txt
```

The agent loop in `agent.py` iterates up to `MAX_ITERATIONS = 5` times per user message. Each iteration:
1. Calls the OpenAI Responses API with the current context and available tools
2. If the model returns a `function_call`, executes the tool and appends the result to context
3. If the model returns a `message`, exits the loop and returns the final response

---

## Tools

| Tool | Parameters | Description |
|---|---|---|
| `check_weather` | `city: str` | Returns current weather conditions for a given city |
| `get_wardrobe_items` | — | Lists all wardrobe items and their status (clean/dirty) |
| `wash_clothing` | `item_name: str` | Washes a clothing item, updating its status to clean |

---

## Quickstart

### 1. Clone the repository

```bash
git clone https://github.com/NicolasJoseGula/Butler-Agent.git
cd Butler-Agent
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

```bash
cp .env.example .env
```

Edit `.env` with your credentials:

```env
OPENAI_API_KEY=your_openai_api_key_here
WEATHER_API_KEY=your_weather_api_key_here
```

- Get your OpenAI key at [platform.openai.com](https://platform.openai.com/)
- Get your WeatherAPI key at [weatherapi.com](https://www.weatherapi.com/) (free tier available)

### 5. Run the agent

```bash
python main.py
```

Type `q`, `quit`, or `exit` to end the session.

---

## Example Conversation

```
[USER]: What should I wear today in London?

[ENTERING AGENT LOOP]
[THINK]: Model decided to return these items: ['ResponseFunctionToolCall']
[ACT]: Calling "check_weather" with arguments {'city': 'London'}
[OBSERVE]: Result London: Overcast, 11.0°C (feels like 9.5°C), humidity 82%
[THINK]: Model decided to return these items: ['ResponseFunctionToolCall']
[ACT]: Calling "get_wardrobe_items" with arguments {}
[OBSERVE]: Result Item blue sweater is dirty; Item brown jacket is dirty
[THINK]: Model decided to return these items: ['ResponseFunctionToolCall', 'ResponseFunctionToolCall']
[ACT]: Calling "wash_clothing" with arguments {'item_name': 'blue sweater'}
[OBSERVE]: Result blue sweater is washed
[ACT]: Calling "wash_clothing" with arguments {'item_name': 'brown jacket'}
[OBSERVE]: Result brown jacket is washed
[THINK]: Model decided to return these items: ['ResponseOutputMessage']
[EXITING AGENT LOOP]
[ASSISTANT]: It's overcast and 11°C in London today. I've washed your blue sweater and brown jacket — both are ready to wear. I'd recommend layering the blue sweater under the brown jacket to stay warm. Don't forget an umbrella!
```

---

## Running Tests

```bash
pytest tests/
```

---

## Key Concepts

**Agent Loop** — An iterative reasoning cycle where the model thinks, acts through tools, observes results, and repeats until it reaches a final answer.

**Tool Calling** — A structured way for the LLM to request function execution. The model returns a function name and arguments; our code executes it and returns the result.

**Context Management** — The full conversation history (user messages, tool calls, tool results, assistant responses) is passed to the model on every iteration, giving the agent memory.

**ReAct Framework** — This project implements the Reasoning + Acting pattern, where the model interleaves reasoning steps with tool calls to solve multi-step tasks.

---

## Tech Stack

- [OpenAI Python SDK](https://github.com/openai/openai-python) — Responses API with tool calling
- [WeatherAPI](https://www.weatherapi.com/) — Real-time weather data
- [python-dotenv](https://github.com/theskumar/python-dotenv) — Environment variable management
- [pytest](https://pytest.org/) — Testing
