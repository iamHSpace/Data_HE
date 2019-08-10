import os
import pandas as pd 
import cv2
# curr = os.getcwd()
# train_csv = pd.read_csv('/home/hspace/Downloads/HE_Data/data/train.csv')
# train_csv.set_index('image_id',inplace=True)


'''
for i in range(18540):
	img = cv2.imread('/home/hspace/Downloads/HE_Data/data/train/{}.jpg'.format(i),1)
	if os.path.exists('/home/hspace/Downloads/HE_Data/data/final data/{}'.format(train_csv['category'][i])) != True:
		os.mkdir('/home/hspace/Downloads/HE_Data/data/final data/{}'.format(train_csv['category'][i]))
	cv2.imwrite("/home/hspace/Downloads/HE_Data/data/final data/{}/{}.jpg".format(train_csv['category'][i],i),img)
	

print(train_csv['category'][2])
# '''
for i in range(1,103):
	j=0
	for filename in os.listdir('/home/hspace/Downloads/HE_Data/data/final data/{}/'.format(i)):
		dst = str(j)+".jpg"
		src = '/home/hspace/Downloads/HE_Data/data/final data/{}/'.format(i)+filename
		dst = '/home/hspace/Downloads/HE_Data/data/final data/{}/'.format(i)+dst
		os.rename(src,dst)
		j=j+1




for i in range(1,5):
	print(i)