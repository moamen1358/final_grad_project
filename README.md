
- [`main.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Finvisa%2FDesktop%2Fmy_grad_streamlit%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22246d973a-88ae-4dd4-b5ed-1fde6b242444%22%5D "/home/invisa/Desktop/my_grad_streamlit/main.py"): The main Streamlit app file that handles navigation.
- [`home.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Finvisa%2FDesktop%2Fmy_grad_streamlit%2Fhome.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22246d973a-88ae-4dd4-b5ed-1fde6b242444%22%5D "/home/invisa/Desktop/my_grad_streamlit/home.py"): The Home page.
- [`real_time_prediction.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Finvisa%2FDesktop%2Fmy_grad_streamlit%2Freal_time_prediction.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22246d973a-88ae-4dd4-b5ed-1fde6b242444%22%5D "/home/invisa/Desktop/my_grad_streamlit/real_time_prediction.py"): The Real-Time Prediction page.
- [`registration_form.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Finvisa%2FDesktop%2Fmy_grad_streamlit%2Fregistration_form.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22246d973a-88ae-4dd4-b5ed-1fde6b242444%22%5D "/home/invisa/Desktop/my_grad_streamlit/registration_form.py"): The Registration Form page.
- [`report.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Finvisa%2FDesktop%2Fmy_grad_streamlit%2Freport.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22246d973a-88ae-4dd4-b5ed-1fde6b242444%22%5D "/home/invisa/Desktop/my_grad_streamlit/report.py"): The Report page.

## Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Create a virtual environment** (optional but recommended):

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:

    ```sh
    pip install -r requirements.txt
    ```
## Running the App With Docker

1. **Build the docker**

    ```sh
    docker build -t face_recognition_app .
    ```

2. **Run the Docker**:

    ```sh
    docker run -p 8501:8501 face_recognition_app
    ```



## Running the App

1. **Navigate to the project directory**:

    ```sh
    cd my_project
    ```

2. **Run the Streamlit app**:

    ```sh
    streamlit run src/main.py
    ```

This will start the Streamlit server and open your app in a web browser.

## Usage

### Home Page

The Home page provides a welcome message and basic information about the app.

### Real-Time Prediction

The Real-Time Prediction page allows you to perform real-time face recognition using an RTSP stream. You can adjust the recognition threshold using a slider.

### Registration Form

The Registration Form page allows you to register new faces. You can either upload multiple images or use your camera to capture images for registration.

### Report

The Report page displays the registered faces.

## Dependencies

- streamlit
- opencv-python-headless
- numpy
- pandas
- chromadb
- insightface
- onnxruntime

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [OpenCV](https://opencv.org/)
- [InsightFace](https://github.com/deepinsight/insightface)
- [ChromaDB](https://github.com/chroma-core/chroma)