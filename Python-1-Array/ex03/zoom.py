from load_image import ft_load
from PIL import Image

def zooming(path: str) -> None:
    img_array = ft_load(path)
    h, w = img_array.shape[:2]
    channels = 1
    if len(img_array.shape) > 2:
        channels = img_array.shape[2]
    
    # Define the region to zoom in (center 400x400 pixels)
    start_h = (h - 400) // 2 if h > 400 else 0
    start_w = (w - 400) // 2 if w > 400 else 0
    
    height = min(400, h)
    width = min(400, w)
    
    # Extract the region
    if channels > 1:
        # Keep only the first channel for the zoomed version
        zoomed_array = img_array[start_h:start_h+height, start_w:start_w+width, 0:1]
    else:
        # If grayscale, just slice the array
        zoomed_array = img_array[start_h:start_h+height, start_w:start_w+width]
        zoomed_array = zoomed_array[..., np.newaxis]  # Add channel dimension for consistency
    
    zoomed_image = Image.fromarray(zoomed_array.squeeze(), mode='L')
    zoomed_image.save("hhh.jpeg")
    print("Saved zoomed image as 'hhh.jpeg'")
    


    



if __name__ == "__main__":
    zooming("animal.jpeg")