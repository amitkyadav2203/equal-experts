# Flask App to fetch github user gists - Assignemnt Amit Kumar Yadav

This Flask application accepts a GitHub username and returns the public gists of that user on GitHub. The app is containerized using Docker for ease of deployment.


## Prerequisites

Ensure the following are installed on your system:

`Git`: To clone the repository.

`Docker`: To build and run the Docker image.

`Python 3`: For testing the API using the provided test.py script.



## Steps to Use


## 1. Clone the Repository and Change Branch
```
Clone the repository
git clone https://github.com/EqualExperts-Assignments/equal-experts-resourceful-mature-impeccable-energy-a77cf20f8d12.git EqualExperts-Assignments

# Navigate to the project directory
cd EqualExperts-Assignments

# Change to the desired branch
git checkout amit-kumar-yadav
```


## 2. Build the Docker Image

Use the docker build command to create the Docker image from the provided Dockerfile.

```
docker build -t github-gist-app:latest .
```

`-t`: Tags the image with a name (github-gist-app) and tag (latest).

`.` : Specifies the current directory as the build context.


## 3. Build the Docker Network

Use the docker network to create a common network for containers.

```
docker network create EqualExperts
```


## 4. Run the Docker Container
Start the Flask app in a Docker container with the following command:
```
docker run -d -p 5000:5000 --network EqualExperts --name github-gist-container github-gist-app:latest
```

`-d`: Runs the container in detached mode.

`-p 5000:5000`: Maps port 5000 on your machine to port 5000 inside the container.

`--name`: Assigns a name to the container (github-gist-container).




## 5. Check if the Application is Running

Verify that the application is running by visiting the following URL in your browser:
```
http://127.0.0.1:5000
```

You should see a response instructing how to use the API. For example:

```
{
    "message": "Please provide a GitHub username in the path, e.g., /octocat, to retrieve public Gists for that user."
}
```





## 6. Test the API with a Python Script in same Docker image
Use the provided test.py script to test the API. The script sends a request to the Flask app container and prints the response.

Sample test.py Script:
```
docker run --rm --network EqualExperts github-gist-app:latest python3 test.py 
```

Please make sure to update tests as appropriate.


## 7. Test the API with a github username

Sample username `octocat`:
```
http://127.0.0.1:5000/octocat
```

Response
```
[
  {
    "description": "Hello world!",
    "id": "6cad326836d38bd3a7ae",
    "url": "https://gist.github.com/octocat/6cad326836d38bd3a7ae"
  },
  {
    "description": "",
    "id": "0831f3fbd83ac4d46451",
    "url": "https://gist.github.com/octocat/0831f3fbd83ac4d46451"
  },
  {
    "description": "",
    "id": "2a6851cde24cdaf4b85b",
    "url": "https://gist.github.com/octocat/2a6851cde24cdaf4b85b"
  },
  {
    "description": "Some common .gitignore configurations",
    "id": "9257657",
    "url": "https://gist.github.com/octocat/9257657"
  },
  {
    "description": null,
    "id": "1305321",
    "url": "https://gist.github.com/octocat/1305321"
  },
  {
    "description": null,
    "id": "1169854",
    "url": "https://gist.github.com/octocat/1169854"
  },
  {
    "description": null,
    "id": "1169852",
    "url": "https://gist.github.com/octocat/1169852"
  },
  {
    "description": null,
    "id": "1162032",
    "url": "https://gist.github.com/octocat/1162032"
  }
]
```


#### Note: Check pretty print in browser if not presented in json. 

