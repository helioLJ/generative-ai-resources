from flask import Flask, Response, request
from openai import OpenAI
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://127.0.0.1:5500"])
openai_client = OpenAI()

@app.route('/stream_chat_completion', methods=['POST'])
def stream_chat_completion():
    user_input = request.json.get('user_input')

    completion = openai_client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[{'role': 'user', 'content': user_input}],
        stream=True
    )

    def generate():
        accumulated_response = ""

        for chunk in completion:
            chunk_content = chunk.choices[0].delta.content
            if len(chunk_content):
                accumulated_response += str(chunk_content)
                print(accumulated_response)
                yield accumulated_response

    return Response(generate(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)
