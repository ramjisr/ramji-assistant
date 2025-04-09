import streamlit as st
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader

st.set_page_config(page_title="Ram Ji Assistant", layout="centered")
st.title("Ram Ji Assistant")

query = st.text_input("Poochhiye kuch bhi Ram Ji Tripathi ke baare mein...")

if query:
    documents = SimpleDirectoryReader('data').load_data()
    index = GPTVectorStoreIndex.from_documents(documents)
    response = index.query(query)
    st.markdown("**उत्तर:**")
    st.write(response.response)