from flask import Flask, request, render_template
from utils import create_agent_vapi, create_agent_retell

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create-agent', methods=['POST'])
def create_agent():
    data = request.json
    provider = data.get("provider")

    if provider == "vapi":
        result = create_agent_vapi(data)
        return result, 200, {'Content-Type': 'text/plain'}
    elif provider == "retell":
        result = create_agent_retell(data)
        return result, 200, {'Content-Type': 'text/plain'}

    return "Unsupported provider", 400

if __name__ == "__main__":
    app.run(debug=True)