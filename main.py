import cv2
import torch

# Load YOLOv5 model
yolov5 = torch.hub.load(
    'ultralytics/yolov5',
    'yolov5s',
    pretrained=True,
    trust_repo=True
)

# Modification 1
# Change confidence threshold
yolov5.conf = 0.30

# Load image
image_path = "input_image.jpg"
image = cv2.imread(image_path)

# Run detection
results = yolov5(image)

# Convert detections
objects = results.xyxyn[0].detach().cpu().numpy()

# Modification 2
# Print total detected objects
print("Total detected objects:", len(objects))

# Class names
classes = yolov5.names

# Copy image
output_image = image.copy()

h, w, _ = output_image.shape

# Convert coordinates
objects[:, 0:4] = objects[:, 0:4] * [w, h, w, h]

for obj in objects:

    x1, y1, x2, y2, conf, class_id = obj

    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)

    label = classes[int(class_id)]

    print(f"{label}: {conf:.2f}")

    cv2.rectangle(
        output_image,
        (x1, y1),
        (x2, y2),
        (0, 255, 0),
        2
    )

    cv2.putText(
        output_image,
        f"{label} {conf:.2f}",
        (x1, y1 - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (0,255,0),
        2
    )

# Save output
cv2.imwrite("output_result.png", output_image)

print("Output image saved.")