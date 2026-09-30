# Demo_Neural-Semantic-Matching-Protocol
# uv init
# uv venv
# .venv\Scripts\activate
# uv add -r requirements.txt

# Streamlit run app.py

# Run Test MCP
mcp dev mcp_server.py or python mcp_server.py
and 
open http://localhost:6274/

pip uninstall mcp -y

pip install "mcp[cli]>=1.20,<2.0"

# python guardrails_eval.py