import streamlit as st
import string
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

lemmatizer = WordNetLemmatizer()
stopwords_set = set(stopwords.words('english'))

# Preprocessing function
def preprocess_email(email_to_classify):
    email_text = email_to_classify.lower()
    email_text = email_text.translate(str.maketrans('', '', string.punctuation))
    email_text = [lemmatizer.lemmatize(word) for word in email_text.split() if word not in stopwords_set]
    return " ".join(email_text)  # Ensure it returns a string

# Streamlit app interface
st.title("Email Spam Detector Using NLP")

email_to_classify = st.text_area("Enter Email Content")

if st.button('Predict'):
    if not email_to_classify.strip():
        st.error("Please enter email content to classify!")
    else:
        # Preprocess the email
        processed_email = preprocess_email(email_to_classify)

        # Vectorize the preprocessed email
        x_email = vectorizer.transform([processed_email])  # Pass as a list
        prediction = loaded_model.predict(x_email)

        # Display 
        if prediction == 1:
            st.write("**This email is classified as Spam.**")
        else:
            st.write("**This email is classified as Not Spam.**")
