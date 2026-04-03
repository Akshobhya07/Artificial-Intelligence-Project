from flask import Flask, request, jsonify, render_template
from rules_engine import RulesEngine
from test_generator import TestGenerator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/generate', methods=['POST'])
def generate_test_case():
    data = request.json
    text_input = data.get('text', '')
    
    if not text_input.strip():
        return jsonify({"error": "Input text cannot be empty"}), 400

    try:
        engine = RulesEngine()
        scenarios = engine.evaluate_text(text_input)
        
        generator = TestGenerator()
        markdown = generator.generate_human_readable(scenarios)
        python_stubs = generator.generate_python_stubs(scenarios)
            
        return jsonify({
            "success": True,
            "markdown": markdown,
            "python": python_stubs
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
