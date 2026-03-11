import openai

openai.api_key="YOUR_OPENAI_KEY"

def generate_article(keyword,language):

    prompt=f"""
Write a professional blog report about '{keyword}'.

Language: {language}

Requirements

- Title must attract readers
- Article about 2000 characters
- Original content
- No copyright infringement
- Add SEO explanation
"""

    response=openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    article=response["choices"][0]["message"]["content"]

    hashtags=f"\n\n#{keyword} #{language}"

    return article+hashtags