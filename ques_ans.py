import streamlit as st
from transformers import pipeline  #pip install transformers

model=pipeline(task='question-answering', model='deepset/roberta-base-squad2')

st.title("Question Anwering Model")
st.sidebar.markdown('''This Extractive question answering model is based on the roberta base model (sqaud2).
                    Enter some context and ask a relevant question.
					It will extract the answer from the context.''')

def main():
	context=st.text_area("Enter Context here:")
	query=st.text_input("Enter Query here: ")
	if context and query:
		answer = model(question=query, context=context)
		st.text(answer["answer"])

main()
#streamlit run "D:\KMV\NLP\Ques answering project\ques_ans.py"
