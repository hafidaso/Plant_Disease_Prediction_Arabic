# Plant Disease Prediction Using TensorFlow and Streamlit - Arabic

This project provides a web-based interface for predicting plant diseases using a pre-trained TensorFlow model. The application is built with Streamlit and predicts the disease in plants based on an image input. The model identifies various diseases for different plants such as apples, cherries, corn, and more.

## Features

- **Image Upload**: Upload an image of a plant's leaf for disease detection.
- **Disease Prediction**: The TensorFlow model predicts the plant disease and provides a confidence score.
- **Disease Descriptions**: The application includes descriptions of the diseases and suggested treatments for each identified disease.

## Demo

To see the application in action, follow the instructions below to run it locally.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/plant-disease-prediction.git
   cd plant-disease-prediction

### Running the Application

To run the Streamlit application, use the following command:
    ```bash
    streamlit run main.py


## Plant Diseases Covered

The model can identify and describe the following diseases:

- **Apple**: Apple Scab, Black Rot, Cedar Apple Rust, Healthy
- **Blueberry**: Healthy
- **Cherry**: Powdery Mildew, Healthy
- **Corn**: Cercospora Leaf Spot, Common Rust, Northern Leaf Blight, Healthy
- **Grape**: Black Rot, Esca (Black Measles), Leaf Blight, Healthy
- **Orange**: Huanglongbing (Citrus Greening)
- **Peach**: Bacterial Spot, Healthy
- **Pepper**: Bacterial Spot, Healthy
- **Potato**: Early Blight, Late Blight, Healthy
- **Strawberry**: Leaf Scorch, Healthy
- **Tomato**: Bacterial Spot, Early Blight


## Model Information

The model is a **convolutional neural network (CNN)** trained using **TensorFlow** and **Keras**. It processes images resized to **128x128 pixels** and outputs a predicted disease along with the confidence level.

## Future Improvements

- **Expand disease coverage**: Add support for more plants and diseases.
- **Optimize model**: Improve the accuracy and efficiency of the TensorFlow model.
- **UI Enhancements**: Enhance the user interface for a better experience.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, feel free to contact the project maintainer:

**Name**: Hafida Belayd  
**Email**: hafidabelaidagnaoui@gmail.com