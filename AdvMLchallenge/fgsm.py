import torch
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import matplotlib.pyplot as plt

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load a pre-trained ResNet model
model = models.resnet50(pretrained=True)
model = model.to(device)
model.eval()

preprocess = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])


def fgsm_attack(image, epsilon, data_grad):
    '''
    Fast Gradient Sign Method Attack Function

    Args:
        image (torch.Tensor): Original image
        epsilon (float): Perturbation amount
        data_grad (torch.Tensor): gradient of image
    
    Returns:
        torch.Tensor: Peturbed image
    '''

    # TODO

    # Get the sign of the gradient

    # Perturb the image in the direction of the gradient

    # Clip the perturbed image to ensure it stays within valid pixel range

    return None

# Load an example image
image_path = "panda.jpg"

image = Image.open(image_path)
image_tensor = preprocess(image).unsqueeze(0)  # Add batch dimension

image_tensor = image_tensor.to(device).requires_grad_(True)

# Forward pass to get the prediction
output = model(image_tensor)
_, initial_prediction = torch.max(output, 1)

criterion = nn.CrossEntropyLoss()
loss = criterion(output, initial_prediction)

with torch.no_grad():
    loss.backward()
data_grad = image_tensor.grad.data

epsilon = 0.03

perturbed_image = fgsm_attack(image_tensor, epsilon, data_grad)

output_perturbed = model(perturbed_image)
_, perturbed_prediction = torch.max(output_perturbed, 1)

print("Initial prediction:", initial_prediction.item())
print("Perturbed prediction:", perturbed_prediction.item())

original_image_np = image_tensor.squeeze(0).cpu().detach().numpy().transpose((1, 2, 0))
perturbed_image_np = perturbed_image.squeeze(0).cpu().detach().numpy().transpose((1, 2, 0))

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original Image (Prediction: {})".format(initial_prediction.item()))
plt.imshow(original_image_np)
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Perturbed Image (Prediction: {})".format(perturbed_prediction.item()))
plt.imshow(perturbed_image_np)
plt.axis("off")

plt.show()
