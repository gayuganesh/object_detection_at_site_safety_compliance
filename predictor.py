predicted = model.predict("/content/50498892-young-factory-worker-controlling-the-work.png", confidence=40, overlap=30).json()
print(predicted)
