import os
from flask import Flask, render_template, request, jsonify
from groq import Groq
from prompts import JD_ANALYSIS_PROMPT, RESUME_TAILORING_PROMPT
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_jd(jd):
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",  
            messages=[
                {"role": "system", "content": JD_ANALYSIS_PROMPT},
                {"role": "user", "content": jd}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error in analyze_jd: {e}")
        raise

def get_tailored_resume(jd_analysis, resume):
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",  
            messages=[
                {"role": "system", "content": "You are an expert resume tailor."},
                {"role": "user", "content": f"Based on this top three responsibilities {jd_analysis}"},
                {"role": "user", "content": RESUME_TAILORING_PROMPT.format(resume=resume)}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error in get_tailored_resume: {e}")
        raise

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tailor_resume', methods=['POST'])
def tailor_resume():
    jd = request.form['jd']
    resume = request.form['resume']
    
    try:
        jd_analysis = analyze_jd(jd)
        tailored_resume = get_tailored_resume(jd_analysis, resume)
        return jsonify({'tailored_resume': tailored_resume})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
