from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
# openai.api_key = os.getenv('OPENAI_API_KEY')

decision_bp = Blueprint('decision', __name__)

@decision_bp.route('/api/decide', methods=['POST'])
@cross_origin(origins='*')
def decide():
    data = request.get_json()
    
    mood = data.get('mood')
    budget = data.get('budget')
    time = data.get('time')
    activity = data.get('activity')

    prompt = f"""
    Based on the following details, please create a detailed 3-hour itinerary that fits the user's preferences:
    - Mood: {mood}
    - Budget: {budget}
    - Time of day: {time}
    - Preferred activity type: {activity}

    Please break it down by time slots, give vivid but concise descriptions for each activity. Make it sound inspiring and fun.
    """



    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that suggests fun and practical activities."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
            max_tokens=60
        )

        suggestion = response.choices[0].message.content.strip()
        return jsonify({'suggestion': suggestion})

    except Exception as e:
        print('OpenAI API error:', e)
        return jsonify({"suggestion": "Sorry, I couldn't generate a suggestion right now."}), 500


    # try:
    #     response = openai.ChatCompletion.create(
    #         model="gpt-3.5-turbo",
    #         messages=[
    #             {"role": "system", "content": "You are a helpful assistant that suggests fun and practical activities."},
    #             {"role": "user", "content": prompt}
    #         ],
    #         temperature=0.8,
    #         max_tokens=60
    #     )

    #     suggestion = response.choices[0].message.content.strip()
    #     return jsonify({'suggestion': suggestion})
    
    # except Exception as e:
    #     print('OpenAI API error:', e)
    #     return jsonify({"suggestion": "Sorry, I couldn't generate a suggestion right now."}), 500
