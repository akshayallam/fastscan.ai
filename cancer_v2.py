from fastai.imports import *
from fastai.transforms import *
from fastai.conv_learner import *
from fastai.model import *
from fastai.dataset import *
from fastai.sgdr import *
from fastai.plots import *
import requests

def run_ai(image_url):
	PATH = "data/cancer/"
	sz = 224
	arch = resnet50
	data = ImageClassifierData.from_paths(PATH, tfms = tfms_from_model(arch, sz))
	learn = ConvLearner.pretrained(arch,data,precompute=True)
	learn.fit(0.0075, 150)
	img_data = requests.get(image_url).content	
	with open('image_name.jpg', 'wb') as handler:
		handler.write(img_data)
		trn_tfms, val_tfms = tfms_from_model(arch,sz)
		im = val_tfms(open_image('image_name.jpg'))
		learn.precompute = False
		preds = abs(learn.predict_array(im[None]))
		if min(preds[0]) == 0:
			return np.argmax(preds)
		elif max(preds[0])/min(preds[0]) < 50:
			return 0
		else:
			return np.argmax(preds)
		
