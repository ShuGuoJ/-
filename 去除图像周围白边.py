from matplotlib import pyplot as plt
from PIL import Image
# 读取照片
img = Image.open('liuyifei.jpg')

# 设置画布大小，与图像大小一致
w, h = img.size
# 画布大小是先宽后高
plt.figure(figsize=(w/100.0, h/100.0), facecolor='y')
plt.imshow(img, aspect='equal')
# 去除白边
# 调整区域边距
plt.subplots_adjust(top=1, bottom=0, left=0, right=1, wspace=0, hspace=0)
plt.margins(0,0)
plt.axis('off')
plt.savefig('0.jpg')
