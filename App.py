import streamlit as st
from groq import Groq

st.set_page_config("pragyanAI Content Generator", layout="wide")
st.title("pragyan_AI - Content Generator")
st.image("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/71322cb8-c781-4c3a-b2b8-58ac33324fe6/dfof921-61b056f7-43fe-4436-9132-103ccb628712.jpg/v1/fill/w_1192,h_670,q_70,strp/tom_and_jerry_chase__by_xrthayp44_dfof921-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTA4MCIsInBhdGgiOiJcL2ZcLzcxMzIyY2I4LWM3ODEtNGMzYS1iMmI4LTU4YWMzMzMyNGZlNlwvZGZvZjkyMS02MWIwNTZmNy00M2ZlLTQ0MzYtOTEzMi0xMDNjY2I2Mjg3MTIuanBnIiwid2lkdGgiOiI8PTE5MjAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.ZhEU9B_KpYqaqJM26kMxAcQI4lc98VHtcL1rN5QV7os")
# Get GROQ API Key
client = Groq(api_key=st.secrets["GROQ_API_KEY"])
# Get Product Name and Audience for That Product
product = st.text_input("Product")
audience = st.text_input("Audience")
# Button to Generate Content
if st.button("Generate Content"):
    prompt = f"Write marketing content for {product} targeting {audience}."
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    st.session_state.text = response.choices[0].message.content
    text =response.choices[0].message.content
    st.write(text)
# After Content Create - Download The File
if "text" in st.session_state:
    content = st.text_area("Generated Content", st.session_state.text, height=300)
    st.download_button(
            label="⬇️ Download as TXT",
            data=content,
            file_name="marketing_copy.txt",
            mime="text/plain"
        )
else:
    st.info("Generate content first")
