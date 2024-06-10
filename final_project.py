import cv2
import numpy as np

def cartoonify_image(image, sharpness_factor=1.2, bilateral_filter_d=7, bilateral_filter_sigma_color=150, bilateral_filter_sigma_space=150, details_enhancement_factor=1.2):
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gray = cv2.bilateralFilter(gray, d=bilateral_filter_d, sigmaColor=bilateral_filter_sigma_color, sigmaSpace=bilateral_filter_sigma_space)

    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, 9, 2)

    color = cv2.bilateralFilter(image, d=bilateral_filter_d, sigmaColor=bilateral_filter_sigma_color, sigmaSpace=bilateral_filter_sigma_space)
    lab = cv2.cvtColor(color, cv2.COLOR_BGR2LAB)

    cartoon = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

    cartoon = cv2.bitwise_and(cartoon, cartoon, mask=edges)

    kernel_sharpening = np.array([[-1, -1, -1],
                                  [-1, sharpness_factor + 8, -1],
                                  [-1, -1, -1]])
    cartoon = cv2.filter2D(cartoon, -1, kernel_sharpening)

    cartoon = cv2.convertScaleAbs(cartoon, alpha=details_enhancement_factor, beta=20)

    blurred = cv2.GaussianBlur(cartoon, (0, 0), 1)
    cartoon = cv2.addWeighted(cartoon, 1.2, blurred, -0.2, 0)

    return cartoon

def main():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        cartoon_with_details = cartoonify_image(frame, sharpness_factor=1.2, bilateral_filter_d=7, bilateral_filter_sigma_color=150, bilateral_filter_sigma_space=150, details_enhancement_factor=1.2)

        cv2.imshow("Original", frame)
        cv2.imshow("Cartoon (Details Enhanced)", cartoon_with_details)

        # Break the loop when 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
