Algorithm Explanation:

Grayscale Conversion:
Input image undergoes a conversion process to grayscale, typically achieved through weighted averaging of the color channels. This simplifies subsequent processing by reducing the image to a single intensity channel.

Bilateral Filtering:
Grayscale image is subjected to bilateral filtering, a non-linear filtering technique. This involves a convolution operation with a Gaussian filter in both spatial and intensity domains. The goal is to smooth the image while preserving edges by considering both spatial proximity and intensity differences.

Edge Detection:
Adaptive thresholding is applied to the filtered grayscale image to identify edges. This process involves setting a pixel as an edge if its intensity is significantly different from its neighbors, creating a binary mask highlighting regions of pronounced intensity changes.

LAB Color Space Conversion:
The original color image is transformed into the LAB color space. LAB separates the luminance (L) component, representing lightness, from the chromaticity components (a and b), which encode color information. This separation facilitates independent processing of luminance and color.

Color Adjustment (Optional):
The chromaticity components (a and b) in the LAB color space can be selectively adjusted based on a predetermined color scheme. This adjustment introduces shifts in the color distribution, allowing for the customization of warm or cool tones in the final cartoonified image.

Cartoon Image Combination:
The LAB image is converted back to the BGR color space, and the cartoon image is obtained by combining the color information with the edge-detected mask.

Sharpening:
A sharpening kernel is applied to enhance the edges and make the cartoon image more visually appealing.

Contrast Adjustment:
The contrast of the cartoon image is increased to make it more vibrant.

Details Enhancement:
An unsharp mask is applied to enhance fine details in the cartoon image, providing a more intricate appearance.







How To Run The Code:

Install Required Libraries:
Make sure you have Python(3.12.0) installed on your system.

Install the necessary library by running:
Copy code
pip install opencv_python

Run the Code:
Copy the provided Python code into a file (e.g., cartoonify.py).
Open a terminal or command prompt and navigate to the directory containing the file.

Run the script using:
Copy code
python cartoonify.py

Interacting with the Application:
The application will open a window displaying the original camera feed alongside the cartoonified version.
Press 'q' to exit the application.

Adjust Parameters (Optional):
You can experiment with adjusting parameters in the code, such as color scheme, sharpness, and details enhancement, to observe their effects on the cartoonified image.



