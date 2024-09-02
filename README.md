# Personal Website
This is my personal website for my portfolio etc. This website will be a W.I.P, as I haven't had much time to work on it.(it does look like crap, i know and it will be fixed once i have time) I will be working on this more once I have the time.
![image](https://github.com/user-attachments/assets/c71b4e02-713c-4c05-a269-bd6d440892ad)

## Self-Hosting Instructions

### Prerequisites

1. **Python**: Ensure you have Python 3.6 or higher installed. You can download it from [python.org](https://www.python.org/downloads/).
2. **Git**: Ensure you have Git installed. You can download it from [git-scm.com](https://git-scm.com/downloads).

### Steps to Self-Host

1. **Clone the Repository**

   Open your terminal or command prompt and run the following command to clone the repository:

   ```sh
   git clone https://github.com/N1k0s1/personalwebsite.git
   cd personalwebsite
   ```

2. **Create a Virtual Environment**

   Create a virtual environment to manage dependencies. Run the following commands:

   - On Windows:
     ```sh
     python -m venv venv
     .\venv\Scripts\activate
     ```

   - On macOS/Linux:
     ```sh
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install Dependencies, Set Environment Variables, and Run the Application**

   Install the required dependencies using `pip`, set the necessary environment variables, and start the Flask application:

   ```sh
   pip install -r requirements.txt
   ```

   Start the Flask application by running:

   ```sh
   flask run
   ```

   You should see output indicating that the server is running, typically at `http://127.0.0.1:5000/`.

4. **Access the Website**

   Open your web browser and navigate to `http://127.0.0.1:5000/` to see the website in action.
