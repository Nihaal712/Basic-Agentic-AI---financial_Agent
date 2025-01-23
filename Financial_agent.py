from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

# Web Search Agent
web_search_agent = Agent(
    name="web search agent",
    role="search the web for information",
    model=Groq(id="llama-3.1-70b-versatile", api_key="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"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tools_calls=True,
    markdown=True,
)

# Finance Agent
finance_agent = Agent(
    name="Finance AI Agent",
    model=Groq(id="llama-3.1-70b-versatile", api_key="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"),
    tools=[YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        stock_fundamentals=True,
        company_news=True
    )],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

# Multi-Agent with Groq Model
multi_ai_agent = Agent(
    team=[web_search_agent, finance_agent],
    model=Groq(id="llama-3.1-70b-versatile",api_key="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"),
    instructions=["Always include sources", "Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

# Query the Multi-Agent
multi_ai_agent.print_response("Give the most recent financial news on oracle and analyse trend and give predictions on buy or sell", stream=True)