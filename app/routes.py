from flask import Blueprint, request, jsonify, render_template
from .services import generate_linkedin_post
import os
print("Current working directory:", os.getcwd())
bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@bp.route('/generate_post', methods=['POST'])
def generate_post():
    if request.is_json:
        data = request.get_json()
        topic = data.get('topic')
    else:
        topic = request.form.get('topic')

    if not topic:
        return jsonify({'error': 'Missing "topic" parameter.'}), 400

    post = generate_linkedin_post(topic)

    if request.is_json:
        return jsonify({'linkedin_post': post})
    else:
        return render_template('index.html', topic=topic, linkedin_post=post)

