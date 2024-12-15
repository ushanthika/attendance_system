This simple student attendance management system was created using HTML/CSS/JS for the front end and Flask for the back end. 
The system has client-server communication, JWT token authentication, and login capabilities.

PROJECT STRUCTURE
attendance-system/
├── server/                # Server-side code
│   ├── app.py            # Flask server application
│   └── users.txt         # User credentials (username:password)
├── client/                # Client-side code
│   ├── login.html        # Login page
│   ├── home.html         # Home page
│   ├── styles.css        # CSS file
│   └── script.js         # JavaScript for client-server interaction
└── docs/                  # Documentation folder
└── README.md              # Project instructions

Before running this project, ensure you have the following installed:
=> Python (Version 3.7 or higher)
=> pip (Python package manager)
=> Git (Optional for cloning the repository)

Setup Instructions
Follow these steps to set up and run the project:

1. Clone the Repository
If you are using Git, clone the repository:
git clone https://github.com/your-repository/attendance-system.git
cd attendance-system

2. Install Dependencies
Navigate to the server folder and install the required Python libraries:
cd server
pip install Flask PyJWT

3. Create User Credentials
Create a file named users.txt inside the server folder.
Add sample credentials in the format username:password:
admin:password123
teacher:pass456
student:test789

4.Run the Server
python app.py
The server will run on http://127.0.0.1:5000.

5. Open the Client
Open a web browser.
Go to the login page:
http://127.0.0.1:5000/client/login.html

Testing the Project
Login Credentials
Use the following credentials for testing:

Username        Password
admin            admin123
teacher          password
student          12345
