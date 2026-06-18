from groq import Groq
import os
from dotenv import load_dotenv
import time

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_agent(system_prompt, user_query):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_query}
        ]
    )
    return response.choices[0].message.content
def parse_research(research_text):
    papers = []
    for i in range(1, 4):
        try:
            title = research_text.split(f"PAPER{i}_TITLE:")[1].split("\n")[0].strip()
            authors = research_text.split(f"PAPER{i}_AUTHORS:")[1].split("\n")[0].strip()
            source = research_text.split(f"PAPER{i}_SOURCE:")[1].split("\n")[0].strip()
            url = research_text.split(f"PAPER{i}_URL:")[1].split("\n")[0].strip()
            summary = research_text.split(f"PAPER{i}_SUMMARY:")[1].split("\n")[0].strip()
            papers.append({
                "title": title,
                "authors": authors,
                "source": source,
                "url": url,
                "summary": summary
            })
        except:
            pass
    return papers

def run_doctoraai(user_query):

    print("Agent A thinking...")
    diagnosis = ask_agent(
        """You are a medical diagnosis specialist. 
        Analyze the given symptoms carefully.watch the symptomps as well as the duration of them
        List possible conditions from most to least likely.
        Always remind the user to consult a real doctor.
        Keep response clear and simple.""",
        user_query
    )
    time.sleep(5)  # wait 5 seconds

    print("Agent B thinking...")
    treatment = ask_agent(
        """You are a treatment and medication expert.
        Suggest general treatment approaches for given symptoms.
        Never recommend specific drug dosages.
        Always remind the user to consult a real doctor.""",
        user_query
    )
    time.sleep(5)  # wait 5 seconds

    print("Agent C thinking...")
    research = ask_agent(
        """You are a medical research assistant.
        Find 2-3 relevant research papers for the given symptoms.
        
        Return ONLY in this exact format, nothing else:
        
        PAPER1_TITLE: [title here]
        PAPER1_AUTHORS: [author here]
        PAPER1_SOURCE: [journal name]
        PAPER1_URL: https://pubmed.ncbi.nlm.nih.gov/?term=[relevant+search+terms]
        PAPER1_SUMMARY: [one line summary]
        
        PAPER2_TITLE: [title here]
        PAPER2_AUTHORS: [author here] 
        PAPER2_SOURCE: [journal name]
        PAPER2_URL: https://pubmed.ncbi.nlm.nih.gov/?term=[relevant+search+terms]
        PAPER2_SUMMARY: [one line summary]
        
        PAPER3_TITLE: [title here]
        PAPER3_AUTHORS: [author here]
        PAPER3_SOURCE: [journal name]
        PAPER3_URL: https://pubmed.ncbi.nlm.nih.gov/?term=[relevant+search+terms]
        PAPER3_SUMMARY: [one line summary]
        
        Use real PubMed search URLs with relevant medical terms.""",
        user_query
    )
    print("Validator synthesizing...")
    final = ask_agent(
        f"""You are a medical validation agent.
        Three specialist AI agents analyzed this query: "{user_query}"

        Agent A (Diagnosis) said:
        {diagnosis}

        Agent B (Treatment) said:
        {treatment}

        Agent C (Research) said:
        {research}

        Your job:
        1. Synthesize into a SHORT, structured response (max 200 words)
        2. Use this exact format:

        **Likely Condition:** [2-3 conditions max]
        
        **Key Observations:** [3-4 bullet points only]
        
        **Recommended Actions:** [3-4 bullet points only]
        
        ⚠️ **Disclaimer:** Always consult a licensed medical professional.
        
        Be concise. No long paragraphs.""",
        ""
    )

    return diagnosis, treatment, research, final

if __name__ == "__main__":
    result = run_doctoraai("I have a headache and fever since 2 days")
    print("\n===FINAL RESPONSE===\n")
    print(result[3])