# DES Soln Django Project

DES Soln is a Django-based web platform designed to support waste management processes in India and Singapore. The website offers features like data analysis reports, informational articles, a chatbot assistant, forums, feedback forms, and more, aimed at educating users on sustainable waste practices.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [License](#license)

## Overview

**DES Soln** is a web application built to educate and assist both businesses and individuals with waste management practices in India and Singapore. Using Django as the backend framework, the platform includes a range of features such as a chatbot (DES Agent), PowerBI data analysis reports, educational articles, a community forum, and user feedback options.

## Features

1. **Data Analysis with PowerBI**: Access detailed reports on historical waste data for India and Singapore, available in PDF format for easy viewing and download.
2. **DES Agent (Chatbot)**: An AI-driven assistant to answer user questions and provide information on various waste management topics.
3. **Informative Articles**: A section dedicated to educating users on waste management best practices, challenges, and regulatory frameworks.
4. **Community Forum**: A discussion board where users can ask questions, share knowledge, and discuss waste management topics.
5. **Feedback Form**: Allows users to submit feedback on the platform’s services, helping to improve user experience.
6. **Contact Us Page**: Provides a way for users to reach out for further support or inquiries.

## Project Structure

Here’s an overview of the main directories in the project:

- **DES DA**: Contains PowerBI PDF reports and resources related to data analysis.
- **DESSoln**: Core functionality and configurations for the DES Soln platform.
- **article**: Manages articles that provide educational content on waste management.
- **desagent**: Contains the code for the DES Agent (chatbot), which answers user queries.
- **feedback**: Handles the feedback form functionality.
- **forumpost**: Manages forum posts, enabling user discussions.
- **home**: Contains templates and views for the homepage and general navigation.
- **static**: Houses static files such as CSS, JavaScript, and images used throughout the website.

Other files:
- **README.md**: Documentation for the project.
- **manage.py**: Django’s management script for various administrative tasks.

## Installation and Setup

### Prerequisites

- Python 3.x
- Django
- Postgresql

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/des-soln.git
   cd des-soln
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

4. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```

5. **Start the server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the website**:
   Open your browser and navigate to `http://127.0.0.1:8000` to view the application.

## Usage

- **Homepage**: Get an overview of DES Soln’s mission and navigate to various sections of the website.
- **Data Analysis (DES DA)**: View PowerBI-generated reports in PDF format, detailing waste management data for India and Singapore.
- **DES Agent (Chatbot)**: Use the chatbot to ask questions and get immediate answers on waste management topics.
- **Articles**: Explore articles on topics like sustainable practices, recycling, and environmental regulations.
- **Forum**: Participate in discussions, ask questions, and share insights within the waste management community.
- **Feedback**: Provide feedback on your experience and suggest improvements for the platform.
- **Contact Us**: Reach out for more information or to get in touch with the DES Soln team.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.




