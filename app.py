import streamlit as st
import base64

# 표시할 PDF 파일 경로 (예: 같은 폴더에 있는 'sample.pdf')
pdf_path = "agree.pdf"

# PDF 파일 읽기 및 base64 인코딩
with open(pdf_path, "rb") as f:
    base64_pdf = base64.b64encode(f.read()).decode('utf-8')

# Streamlit 앱 구성
st.title("내장 PDF 뷰어")

# iframe을 사용해 PDF 출력
pdf_display = f"""
    <iframe 
        src="data:application/pdf;base64,{base64_pdf}" 
        width="700" 
        height="1000" 
        type="application/pdf">
    </iframe>
"""
st.markdown(pdf_display, unsafe_allow_html=True)