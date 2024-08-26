import random
import cv2
from matplotlib import pyplot as plt
import albumentations as A

def visualize_comparison(original_image, transformed_image):
    plt.figure(figsize=(16, 8))
    
    # Display original image
    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.axis('off')
    plt.imshow(original_image)
    
    # Display transformed image
    plt.subplot(1, 2, 2)
    plt.title('Transformed Image')
    plt.axis('off')
    plt.imshow(transformed_image)
    
    plt.tight_layout()
    plt.show()

# Read and convert image
image = cv2.imread(r'D:\datasets\grape\origin\pic\frame_0001.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Define transformation
transform = A.Compose([
    A.RandomGridShuffle(grid=(3, 3), p=1)
])


# Set random seed
random.seed(7)

# Apply transformation
augmented_image = transform(image=image)['image']

# Visualize comparison
visualize_comparison(image, augmented_image)

# BOX_COLOR = (255, 0, 0) # Red
# TEXT_COLOR = (255, 255, 255) # White


# def visualize_bbox(img, bbox, class_name, color=BOX_COLOR, thickness=2):
#     """Visualizes a single bounding box on the image"""
#     x_min, y_min, w, h = bbox
#     x_min, x_max, y_min, y_max = int(x_min), int(x_min + w), int(y_min), int(y_min + h)

#     cv2.rectangle(img, (x_min, y_min), (x_max, y_max), color=color, thickness=thickness)

#     ((text_width, text_height), _) = cv2.getTextSize(class_name, cv2.FONT_HERSHEY_SIMPLEX, 0.35, 1)
#     cv2.rectangle(img, (x_min, y_min - int(1.3 * text_height)), (x_min + text_width, y_min), BOX_COLOR, -1)
#     cv2.putText(
#         img,
#         text=class_name,
#         org=(x_min, y_min - int(0.3 * text_height)),
#         fontFace=cv2.FONT_HERSHEY_SIMPLEX,
#         fontScale=0.35,
#         color=TEXT_COLOR,
#         lineType=cv2.LINE_AA,
#     )
#     return img


# def visualize(image, bboxes, category_ids, category_id_to_name):
#     img = image.copy()
#     for bbox, category_id in zip(bboxes, category_ids):
#         class_name = category_id_to_name[category_id]
#         img = visualize_bbox(img, bbox, class_name)
#     plt.figure(figsize=(12, 12))
#     plt.axis('off')
#     plt.imshow(img)
#     plt.show()

# image = cv2.imread(r'D:\datasets\grape\origin\pic\frame_0001.jpg')
# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# bboxes = [[5.66, 138.95, 147.09, 164.88], [366.7, 80.84, 132.8, 181.84]]
# category_ids = [17, 18]

# # We will use the mapping from category_id to the class name
# # to visualize the class label for the bounding box on the image
# category_id_to_name = {17: 'cat', 18: 'dog'}

# visualize(image, bboxes, category_ids, category_id_to_name)

# transform = A.Compose(
#     [A.HorizontalFlip(p=0.5)],
#     bbox_params=A.BboxParams(format='coco', label_fields=['category_ids']),
# )


# random.seed(7)
# transformed = transform(image=image, bboxes=bboxes, category_ids=category_ids)
# visualize(
#     transformed['image'],
#     transformed['bboxes'],
#     transformed['category_ids'],
#     category_id_to_name,
# )
