import streamlit as st
import hashlib

# -------------------------------
# Functions
# -------------------------------
def generate_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

def generate_file_hash(file_bytes):
    return hashlib.sha256(file_bytes).hexdigest()

def highlight_diff(h1, h2):
    result = ""
    for c1, c2 in zip(h1, h2):
        if c1 == c2:
            result += c2
        else:
            result += f"<span style='color:red; font-weight:bold'>{c2}</span>"
    return result

# -------------------------------
# Title
# -------------------------------
st.title("🔐 Secure Hash Demonstration (SHA-256)")

# -------------------------------
# Dropdown Menu (4 options)
# -------------------------------
option = st.sidebar.selectbox(
    "Choose Functionality",
    [
        "Generate Hash (Text)",
        "Generate Hash (File)",
        "Avalanche Effect (Text)",
        "Avalanche Effect (File)"
    ]
)

# ===============================
# 1. TEXT HASH
# ===============================
if option == "Generate Hash (Text)":
    st.header("Generate SHA-256 Hash (Text)")

    text = st.text_input("Enter text")

    if st.button("Generate Hash"):
        if text:
            hash_value = generate_hash(text)
            st.success("Hash Generated!")
            st.code(hash_value)
        else:
            st.warning("Enter some text")

# ===============================
# 2. FILE HASH
# ===============================
elif option == "Generate Hash (File)":
    st.header("Generate SHA-256 Hash (File)")

    file = st.file_uploader("Upload a file")

    if file:
        file_bytes = file.read()
        file_hash = generate_file_hash(file_bytes)

        st.success("File Hash Generated!")
        st.code(file_hash)

# ===============================
# 3. AVALANCHE (TEXT)
# ===============================
elif option == "Avalanche Effect (Text)":
    st.header("Avalanche Effect for Text")

    text1 = st.text_input("Enter original text")
    text2 = st.text_input("Enter modified text")

    if st.button("Compare"):
        if text1 and text2:
            hash1 = generate_hash(text1)
            hash2 = generate_hash(text2)

            st.write("Original Hash:")
            st.code(hash1)

            st.write("Modified Hash:")
            st.code(hash2)

            if hash1 != hash2:
                st.error("⚡ Avalanche Effect Observed")
            else:
                st.info("Try different inputs")

        else:
            st.warning("Enter both inputs")

# ===============================
# 4. AVALANCHE (FILE)
# ===============================
elif option == "Avalanche Effect (File)":
    st.header("Avalanche Effect for Files")

    file1 = st.file_uploader("Upload File 1", key="f1")
    file2 = st.file_uploader("Upload File 2", key="f2")

    if file1 and file2:
        hash1 = generate_file_hash(file1.read())
        hash2 = generate_file_hash(file2.read())

        st.write("File 1 Hash:")
        st.code(hash1)

        st.write("File 2 Hash (Differences Highlighted):")
        st.markdown(highlight_diff(hash1, hash2), unsafe_allow_html=True)

        # Analysis
        diff = sum(c1 != c2 for c1, c2 in zip(hash1, hash2))
        similarity = round((1 - diff/len(hash1)) * 100, 2)

        st.write("### Analysis")
        st.write(f"Different Characters: {diff}")
        st.write(f"Similarity: {similarity}%")

        if hash1 != hash2:
            st.error("⚡ Avalanche Effect Observed")
        else:
            st.success("Files are identical")
