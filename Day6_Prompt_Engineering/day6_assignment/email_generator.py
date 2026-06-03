"""
Day 6 Assignment: Cold Email Generator
Author: Cohort Teaching Team
Date: 2026

This tool generates a personalized outbound B2B email based on prospect
information using Role Prompting, Few-Shot data, and Chain of Thought (CoT).
"""

import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

# Load environment configurations
load_dotenv()

# Verify API configuration
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("Error: OPENAI_API_KEY environment variable is not set.")
    print("Please set up your .env file as instructed in the README.")
    sys.exit(1)

# Initialize OpenAI Client
client = OpenAI(api_key=api_key)

SYSTEM_ROLE = """
You are a top-performing Sales Development Representative (SDR). Your outbound emails are personalized, short, and under 150 words.
You avoid generic buzzwords like 'synergy', 'disruptive', or 'game-changing'.

You must analyze the prospect's pain point and map it directly to a Stripe value proposition first.

Your output format MUST follow this structure:
REASONING:
- [bullet point analyzing the prospect's pain point]
- [bullet point mapping pain point to value proposition]
- [bullet point on the hook strategy]

EMAIL:
Subject: [Short, clear subject line]
Hi [Name],

[Hook connecting to their role or company]
[Value proposition directly solving their pain point]
[Call to Action proposing a brief discussion]

Best,
[Your Name]
"""

FEW_SHOT_DATA = """
PROSPECT DETAILS:
Name: Jane Smith
Role: VP of Engineering
Company: FinTechCorp
Pain Point: API response times are slowing down checkout conversions.

Output:
REASONING:
- Prospect is a tech leader concerned with checkout conversion speeds.
- Stripe offers a payment gateway API with 99.99% uptime and <100ms response times.
- Hook should reference checkout latency.

EMAIL:
Subject: Reducing checkout latency at FinTechCorp
Hi Jane,

I notice FinTechCorp has been scaling customer transactions, but checkout page latency can easily cost up to 1% of conversion revenue.

Stripe's payment APIs are built to handle high volume under 100ms, helping engineering teams speed up payments without adding infrastructure.

Do you have 5 minutes this Wednesday for a quick discussion on payment performance benchmarks?

Best,
Alex
---
"""

def generate_email(name: str, role: str, company: str, pain_point: str) -> str:
    """
    Sends the prompt to OpenAI and gets the reasoning + email output.
    """
    user_prompt = f"""
    {FEW_SHOT_DATA}
    
    PROSPECT DETAILS:
    Name: {name}
    Role: {role}
    Company: {company}
    Pain Point: {pain_point}
    
    Output:
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": SYSTEM_ROLE},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.3  # Temperature set to 0.3 to ensure logic and brevity
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Runtime Error calling API: {str(e)}"

def main():
    print("=" * 60)
    print("🚀 PROMPT-ENGINEERED COLD OUTBOUND EMAIL GENERATOR")
    print("=" * 60)
    
    name = input("Prospect Name: ").strip()
    role = input("Prospect Role: ").strip()
    company = input("Prospect Company: ").strip()
    pain_point = input("Prospect Pain Point: ").strip()
    
    # Fallbacks if user leaves inputs empty
    if not name:
        name = "David Miller"
        role = "VP of Operations"
        company = "LogisticsHub"
        pain_point = "High package tracking error rate causing customer complaints."
        print(f"\nUsing default prospect details:\nName: {name}\nRole: {role}\nCompany: {company}\nPain Point: {pain_point}")
        
    print("\nDrafting reasoning and email...")
    email_output = generate_email(name, role, company, pain_point)
    
    print("\n" + "-" * 50)
    print(email_output)
    print("-" * 50 + "\n")

if __name__ == "__main__":
    main()
