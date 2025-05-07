# Masterblog API

Masterblog API is a simple blogging platform that provides a backend API for managing blog posts and a frontend for interacting with the API.

## Features

- Create, read, update, and delete blog posts.
- Search for blog posts by title or content.
- Sort blog posts by title or content in ascending or descending order.

## Project Structure

```
Masterblog-API/
    backend/
        backend_app.py  # Flask backend application
    frontend/
        frontend_app.py  # Frontend application
        static/          # Static files (JavaScript, CSS)
        templates/       # HTML templates
```

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd Masterblog-API
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the backend server:
   ```bash
   python backend/backend_app.py
   ```

5. Run the frontend server:
   ```bash
   python frontend/frontend_app.py
   ```

## API Endpoints

### `/api/posts` (GET)
- Retrieve all blog posts.
- Optional query parameters:
  - `sort`: Field to sort by (`title` or `content`).
  - `direction`: Sort order (`asc` or `desc`).

### `/api/posts` (POST)
- Add a new blog post.
- Request body:
  ```json
  {
      "title": "Post Title",
      "content": "Post Content"
  }
  ```

### `/api/posts/<post_id>` (DELETE)
- Delete a blog post by ID.

### `/api/posts/<post_id>` (PUT)
- Update a blog post by ID.
- Request body:
  ```json
  {
      "title": "Updated Title",
      "content": "Updated Content"
  }
  ```

### `/api/posts/search` (GET)
- Search for blog posts by title or content.
- Query parameters:
  - `title`: Search term for the title.
  - `content`: Search term for the content.

## License

This project is licensed under the MIT License.