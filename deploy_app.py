!nohup streamlit run app.py --server.port 80 &
public_url = ngrok.connect(80, "http")
print("Public URL:", public_url)
