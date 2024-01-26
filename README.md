# HTTP Server Task

## Implementation Details
All the instructions provided have been meticulously implemented in the code, designed according to the given specifications.

## Project Structure
1. **app.py**: Main implementation of the HTTP server.
2. **Dockerfile**: Docker configuration for bundling the project.
3. **data/**: Directory containing data files.
4. **requirements.txt**: File containing project dependencies.

## Instructions for Running the Project
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
    Access the server at [http://localhost:8080/data](http://localhost:8080/data).
   [http://127.0.0.1:8080/data?n=1&m=30]

## Docker Compatibility
The Dockerfile has been configured to be compatible with both ARM architecture and x86.

```bash
docker buildx build -t shivanshsharma1507605/http-server --platform linux/amd64,linux/arm64 --push .
docker buildx build -t <YOUR_DOCKER_ID>/http-server .
Replace <YOUR_DOCKER_ID> with your actual Docker ID when executing the command.
