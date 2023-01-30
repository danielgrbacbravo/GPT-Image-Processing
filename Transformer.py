
from transformers import VisionEncoderDecoderModel, ViTFeatureExtractor, AutoTokenizer
import torch
from PIL import Image

import openai
from os import getenv

import apiconfigparser

model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
feature_extractor = ViTFeatureExtractor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)



max_length = 16
num_beams = 4
gen_kwargs = {"max_length": max_length, "num_beams": num_beams}
def predict_step(image_paths):
  images = []
  for image_path in image_paths:
    i_image = Image.open(image_path)
    if i_image.mode != "RGB":
      i_image = i_image.convert(mode="RGB")

    images.append(i_image)

  pixel_values = feature_extractor(images=images, return_tensors="pt").pixel_values
  pixel_values = pixel_values.to(device)

  output_ids = model.generate(pixel_values, **gen_kwargs)

  preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
  preds = [pred.strip() for pred in preds]
  return preds

imagedescriptor = predict_step(['1595526028946.jpeg'])[0]
print(imagedescriptor)
#function that uses the openai api to generate a poem using the imagedecriptor as the prompt
def generate_poem(imagedescriptor):
    openai.api_key = apiconfigparser.get_openai_api_key()
    response = openai.Completion.create(
      engine="davinci",
      prompt= " image caption ["+ imagedescriptor + '] n/ write a more detailed description based on the caption: ',
      max_tokens=100,
      temperature=0.9,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0.6,
      stop=["\n"]
    )
    return response.choices[0].text


print(generate_poem(imagedescriptor))
