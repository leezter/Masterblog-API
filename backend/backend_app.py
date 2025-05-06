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


@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    """
    Delete a blog post by its ID.

    This endpoint handles DELETE requests to remove a blog post from the POSTS list.
    Args:
        post_id (int): The ID of the post to delete.
    Returns:
        A JSON response with a success message if the post is deleted, or an error message if the post is not found.
    """
    # Find the post by ID
    post = None
    for p in POSTS:
        if p['id'] == post_id:
            post = p
            break

    if not post:
        return jsonify({"error": f"Post with id {post_id} not found."}), 404

    # Remove the post from the list
    POSTS.remove(post)

    return jsonify({"message": f"Post with id {post_id} has been deleted successfully."}), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
