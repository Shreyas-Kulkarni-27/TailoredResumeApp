JD_ANALYSIS_PROMPT = """
You are an expert resume writer with over 20 years of experience working with job seekers trying to land a role in tech. Highlight 3 most important job responsibilities in below job description:

{jd}
"""

RESUME_TAILORING_PROMPT = """
Great. Based on these 3 most important responsibilities from job description, please tailor my resume for this position in the job description. Do not make information up, here's my resume:

{resume}
"""