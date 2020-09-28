import numpy as np
from skimage import io
import matplotlib.pyplot as plt
from skimage import data
import matplotlib.patches as patches

def get_mask(image):
	''' Creates mask with three defect regions '''
	mask = np.zeros(image.shape[:-1]) # 0 for non damaged pixels

	maks[101:106, 0:240] = 1

	mask[152:154, 0:60] = 1
	mask[153:155, 60:100] = 1
	mask[154:156, 100:120] = 1
	mask[155:156, 120:140] = 1

	mask[212:217, 0:150] = 1
	mask[217:222, 150:256] = 1
	return mask

def show_image(image, title='Image', cmap_type='gray'):
	plt.imshow(image, cmap=cmap_type)
	plt.title(title)
	plt.axis('off')
	plt.show()


def show_image_contour(image, contours):
	plt.figure()
	for n, contour in enumerate(contours):
		plt.plot(contour[:, 1], contour[:, 0], linewidth=3)
	plt.imshow(image, interpolation='nearest', cmap='gray_r')
	plt.title('Contours')
	plt.axis('off')

def show_image_with_corners(image, coords, title="Corners detected"):
	plt.imshow(image, interpolation='nearest', cmap='gray')
	plt.title(title)
	plt.plot(coords[:, 1], coords[:, 0], '+r', markersize=15)
	plt.axis('off')

def crop_face(result, detected, title="Face detected"):
	for d in detected:
		print(d)
		rostro= result[d['r']:d['r']+d['width'], d['c']:d['c']+d['height']]
	
		plt.figure(figsize=(8, 6))
		plt.imshow(rostro)	
		plt.title(title)
		plt.axis('off')
		plt.show()


def show_detected_face(result, detected, title="Face image"):
	plt.figure()
	plt.imshow(result)
	img_desc = plt.gca()
	plt.set_cmap('gray')
	plt.title(title)
	plt.axis('off')

	for patch in detected:
		
		img_desc.add_patch(
			patches.Rectangle(
				(patch['c'], patch['r']),
				patch['width'],
				patch['height'],
				fill=False,
				color='r',
				linewidth=2)
		)
	plt.show()
	crop_face(result, detected)

image_orig = data.astronaut()[0:200, 0:200]

# Create mask with three defect regions: left, middle, right respectively
astronaut_mask = np.zeros(image_orig.shape[:-1])
astronaut_mask[20:60, 0:20] = 1
astronaut_mask[160:180, 70:155] = 1
astronaut_mask[30:60, 170:195] = 1

# Defect image over the same region in each color channel
damaged_astronaut = image_orig.copy()
for layer in range(damaged_astronaut.shape[-1]):
	damaged_astronaut[np.where(astronaut_mask)] = 0

image_with_logo = io.imread('Images/chapter3/4.2.06_w_logo_2_2.png')
dog_image = io.imread('Images/chapter3/shiba.jpg')
landscape_image = io.imread('Images/chapter3/noise-noisy-nature.jpg')
face_image = io.imread('Images/chapter3/chinese.jpg')
image_dices = io.imread('Images/chapter3/dices.png')
grapefruit = io.imread('Images/chapter4/toronjas.jpg')
building_image = io.imread('Images/chapter4/corners_building_top.jpg')
night_image = io.imread('Images/chapter4/face_det3.jpg')
friends_image = io.imread('Images/chapter4/face_det_friends22.jpg')
profile_image = io.imread('Images/chapter4/face_det9.jpg')