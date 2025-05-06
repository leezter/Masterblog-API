from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

POSTS = [
    {"id": 1, "title": "First post", "content": "This is the first post."},
    {"id": 2, "title": "Second post", "content": "This is the second post."},
]


@app.route('/api/posts', methods=['GET'])
def get_posts():
    """
    Retrieve all blog posts.

    This endpoint handles GET requests to fetch all the blog posts stored in the POSTS list.
    Returns:
        A JSON response containing a list of all blog posts.
    """
    return jsonify(POSTS)


@app.route('/api/posts', methods=['POST'])
def add_post():
    """
    Add a new blog post.

    This endpoint handles POST requests to add a new blog post to the POSTS list.
    The request body must contain a JSON object with 'title' and 'content' fields.
    Returns:
        A JSON response containing the newly created blog post with a unique ID.
    """
    data = request.get_json()

    # Validate input
    if not data:
        return jsonify({"error": "Request body must be a valid JSON object."}), 400

    missing_fields = []
    if 'title' not in data or not data['title'].strip():
        missing_fields.append('title')
    if 'content' not in data or not data['content'].strip():
        missing_fields.append('content')

    if missing_fields:
        return jsonify({"error": f"Missing or empty fields: {', '.join(missing_fields)}"}), 400

    # Generate a new unique ID
    new_id = max(post['id'] for post in POSTS) + 1 if POSTS else 1

    # Create the new post
    new_post = {
        "id": new_id,
        "title": data['title'],
        "content": data['content']
    }
    POSTS.append(new_post)

    return jsonify(new_post), 201


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
