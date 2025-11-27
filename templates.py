qa_template = """Use the following pieces of retrieved context to answer the question. 
If you don't know the answer, just say that you don't know, don't try to make up an answer.
Use three sentences maximum and keep the answer concise.
Question: {question} 
Context: {context} 
Answer:"""

quiz_msg_template = [
        (
            "system",
            "You are a helpful assistant specialized in generating educational quizzes."
            "Based *only* on the following context, create a set of 10 multiple-choice questions "
            "and their correct answers. Format the output clearly with MCQ format with 4 options.",
        ),
        ("human", "Context: {context}\n\nGenerate quiz questions about: {topic}"),
    ]

