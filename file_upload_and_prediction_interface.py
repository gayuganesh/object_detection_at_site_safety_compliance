import gradio as gr

def upload_file(files):
    global file_paths
    file_paths = [file.name for file in files]
    return file_paths
def Predict():
    predicted = model.predict(file_paths, confidence=40, overlap=30).json()
    objects = []
    Score = 0
    for i in predicted.get('predictions'):
      objects.append(i.get('class'))
    for j in objects:
      if j in ("Helmet","Vest","Gloves"):
        Score+=1
      else:
        continue
    return Score

with gr.Blocks() as demo:
    file_output = gr.File()
    upload_button = gr.UploadButton("Click to Upload a File", file_types=["image", "video"], file_count="multiple")
    upload_button.upload(upload_file, upload_button, file_output)
    print(file_paths)

demo.launch()
