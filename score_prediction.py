# infer on a local image
objects = []
Score = 0
for i in predicted.get('predictions'):
  objects.append(i.get('class'))
for j in objects:
  if j in ("Helmet","Vest","Gloves"):
    Score+=1
  else:
    continue
print(Score)
# visualize your prediction
# model.predict("your_image.jpg", confidence=40, overlap=30).save("prediction.jpg")

# infer on an image hosted elsewhere
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())
