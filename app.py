from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").lower()

    if user_message == "":
        return jsonify({"reply": "Please enter a question."})

    elif "Programming Languages" in user_message:
        reply = "Programming languages are used to create software, websites, mobile applications, games, and AI systems."


    elif "java" in user_message:
        reply = "Java is widely used for Android Development, Enterprise Software, Banking Systems, and Backend Development."

    elif "resume building" in user_message:
        reply = "A good resume should be one page, ATS-friendly, and include your education, projects, skills, internships, and certifications."

    elif "placements" in user_message:
        reply = "Prepare DSA, OOP, DBMS, Operating Systems, Aptitude, Communication Skills, and practice interview questions."
    elif "interview preparation" in user_message :
        reply = "Interview preparation is an essential step toward securing a job. It begins with thoroughly researching the company, its mission, values, products, and the job role. Candidates should review their resume and be prepared to explain their skills, projects, internships, and achievements with confidence. Practicing common interview questions, improving communication skills, and preparing answers using the STAR (Situation, Task, Action, Result) method can help deliver structured responses. Technical candidates should revise core concepts, coding problems, and project details relevant to the position. Dressing professionally, arriving on time, maintaining positive body language, and asking thoughtful questions at the end of the interview leave a strong impression. Finally, staying calm, confident, and honest throughout the interview significantly increases the chances of success."
        
    elif "machine learning" in user_message or "ai" in user_message:
        reply = "Start with Python, Mathematics, NumPy, Pandas, Matplotlib, Scikit-learn, TensorFlow, and build real-world projects."

    elif "web development" in user_message:
        reply = "Learn HTML, CSS, JavaScript, Bootstrap, React, Node.js, Express.js, MongoDB, and Git."

    elif "data science" in user_message:
        reply = "Data Science involves Python, Statistics, Pandas, NumPy, Machine Learning, SQL, and Data Visualization."

    elif "higher studies" in user_message:
        reply = "You can pursue M.Tech, MS abroad, MBA, or specialized AI certifications."
    elif "career options" in user_message :
        reply = "Career options are the various professional paths individuals can choose based on their interests, skills, education, and goals. Selecting the right career requires understanding personal strengths, exploring different industries, and staying informed about job market trends. Popular career options include software development, data science, artificial intelligence, cybersecurity, web development, healthcare, finance, digital marketing, education, entrepreneurship, and government services. Students should develop relevant technical and soft skills, gain practical experience through internships or projects, and continuously learn to adapt to changing industry demands. Choosing a career that aligns with both passion and long-term growth opportunities leads to greater job satisfaction and professional success."


    else:
        reply = "Sorry, I don't have information about that topic yet."

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)