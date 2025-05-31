from rapidocr_onnxruntime import RapidOCR

engine = RapidOCR()

img_path = './sample/img3.png'
result, elapse = engine(img_path)
print(result)
print(elapse)
