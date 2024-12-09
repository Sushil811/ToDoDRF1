1. Models: Models define the database schema for our app. They are Python classes that map directly to database tables.
2. Tag Model: Represents labels that can be assigned to tasks for categorization.
3. Fields:
4. name: A unique string field with a maximum length of 100 characters.
  timestamp: Automatically records when the task is created. Read-only and cannot be updated later.
  title: Short description of the task (max length: 100). Mandatory.
  description: Detailed description of the task (max length: 1000). Mandatory.
  due_date: An optional date field for specifying when the task should be completed.
  tags: A many-to-many relationship with the Tag model, allowing multiple tags to be assigned to a single task.
  status: The current state of the task. Choices include:
  OPEN (default value), WORKING, PENDING REVIEW, COMPLETED, OVERDUE, CANCELLED

5. Django Admin Configuration: Django Admin allows administrators to manage the application through a web interface.
6. ToDoItemAdmin
List view: Displays task attributes like title, timestamp, due date, and status in a tabular format.
Filters: Allows filtering tasks by:
status (e.g., OPEN, COMPLETED)
due_date (e.g., tasks due on a specific date)
tags (e.g., tasks with a specific tag).
Fieldsets: Groups form fields logically when creating or editing tasks:
Basic Information: Title, description, due date, and status.
Tags: Assign tags to the task.
Timestamp: View-only field for the creation timestamp.
Purpose: Provides a user-friendly interface to manage tasks efficiently.

7. REST APIs
These APIs allow programmatic interaction with the application using HTTP requests. Built using Django Rest Framework (DRF).

Serializers
Serializers handle validation and transformation of data between the Python objects and JSON format.

TagSerializer:
Handles serialization of the Tag model. Ensures tags are passed in JSON format.

ToDoItemSerializer:

Serializes the ToDoItem model.
Handles the tags field as a nested structure.
Custom methods:
create: Creates a new task and its associated tags if they don't already exist.
update: Updates the task and its tags, ensuring the tag list is replaced rather than appended.
Views
Views process API requests and return responses.

8. ToDoItemCreateView:

Allows creating a new task.
Example: POST /create/ with task details in the request body.
ToDoItemDetailView:

Retrieves details of a specific task by its ID.
Example: GET /<id>/.
ToDoItemListView:

Returns a list of all tasks.
Example: GET /.
ToDoItemUpdateView:

Updates details of a specific task.
Example: PUT /update/<id>/.
ToDoItemDeleteView:

Deletes a specific task by ID.
Example: DELETE /delete/<id>/.

Authentication: All views require Basic Authentication, ensuring only authenticated users can interact with the API.

9. URLs: The urls.py file maps HTTP endpoints to their corresponding views.
