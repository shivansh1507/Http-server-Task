# HTTP Server Task

## Implementation Details
All the instructions provided have been meticulously implemented in the code, designed according to the given specifications.

## Tech Stack
- Python
- Docker

## Project Structure
1. **app.py**: Main implementation of the HTTP server.
2. **Dockerfile**: Docker configuration for bundling the project.
3. **data/**: Directory containing data files.
4. **requirements.txt**: File containing project dependencies.

## Instructions for Running the Project
### Prerequisites
- [Docker](https://www.docker.com/) installed on your machine.

### Steps
1. **Clone the repository:**
    ```bash
    git clone https://github.com/shivansh1507/Http-server-Task.git
    cd http-server-project
    ```

2. **Build and run the Docker container:**
    ```bash
    docker build -t http-server .
    docker run -p 8080:8080 --memory=1500m --cpus=2 http-server
    ```
    The server is now accessible at [http://localhost:8080/data](http://localhost:8080/data).
   on my local server [http://127.0.0.1:8080/data?n=1&m=30] it was showing
   ![Screenshot](https://raw.githubusercontent.com/shivansh1507/Http-server-Task/main/http1.png) 

## Docker Compatibility
The Dockerfile has been configured to be compatible with both ARM architecture and x86.

```bash
# Build for multiple platforms
docker buildx build -t shivanshsharma1507605/http-server --platform linux/amd64,linux/arm64 --push .
# Build for a specific platform
docker buildx build -t <YOUR_DOCKER_ID>/http-server .
```
Google Doc link for instructions[https://docs.google.com/document/d/1-eo2pqcTCXXaJsWtRZ584CoXzup-M_fu8y3UIJjcnrc/edit?usp=sharing].
