# YOLOvs-Image-Classification

## Project Overview

This project uses the YOLOv5 object detection model and PyTorch to detect objects in an image. The model identifies objects, draws bounding boxes around them, displays confidence scores, and saves the final output image.

The project demonstrates the practical use of open-source computer vision technology for image analysis and object detection.

---

## Features

- Detects objects in an image using YOLOv5
- Draws bounding boxes around detected objects
- Displays confidence scores
- Prints detected object names
- Prints the total number of detected objects
- Saves the output image automatically

---

## Technologies Used

- Python
- PyTorch
- YOLOv5
- OpenCV
- NumPy
- Matplotlib

---

## Project Modifications

The following modifications were made to the original code:

1. Changed the confidence threshold to **0.30**
2. Printed the total number of detected objects
3. Printed detected object names and confidence scores
4. Added comments to explain important code sections

---

## Input Image

The project uses a custom image provided by the user.

File:

```text
input_image.jpg
```

The image contains multiple objects that can be detected by the YOLOv5 model.

---

## How to Run

### Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOLOvs-Image-Classification.git
```

### Navigate to the Project Folder

```bash
cd YOLOvs-Image-Classification
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Program

```bash
python main.py
```

---

## Example Output

```text
Total detected objects: 5

person: 0.91
chair: 0.88
laptop: 0.84
bottle: 0.79
backpack: 0.75
```

*Replace the above output with your actual detection results.*

---

## Output Result

The detected image is saved as:

```text
output_result.png
```

The output image contains:

- Bounding boxes
- Object labels
- Confidence scores

---

## Project Structure

```text
YOLOvs-Image-Classification/
│
├── main.py
├── input_image.jpg
├── output_result.png
├── README.md
├── requirements.txt
├── LICENSE
└── report.docx
```

---

## Why README.md and requirements.txt Are Important

### README.md

README.md provides information about the project, including its purpose, features, setup instructions, and usage. It helps other users understand and use the project easily.

### requirements.txt

requirements.txt contains all required Python libraries. It allows users to install the necessary dependencies quickly and run the project without configuration issues.

---

## License

This project is licensed under the MIT License.

See the LICENSE file for details.

---

## Author

**Fahad Mainuddin**

Open Source Software Course

Sejong University
