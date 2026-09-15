# MiniLinearJira
Mini Linear/Jira Exercise project
# Mini SaaS — Project Management System

## 📌 Overview

Build a production-style project management backend similar to a simplified version of Linear or Jira.

The goal of this project is to practice real-world backend development with Django REST Framework, PostgreSQL, authentication, permissions, API design, testing, and performance optimization.

The project should be designed as if it were going to be used by real users.

---

## 🛠 Tech Stack

### Required

* Python 3.12+
* Django
* Django REST Framework
* PostgreSQL
* JWT Authentication

### Recommended

* Docker
* Docker Compose
* Redis
* Celery
* pytest
* drf-spectacular / Swagger
* GitHub Actions

### Optional

* React
* TypeScript

---

# 🎯 Core Requirements

## 1. Authentication

Implement user authentication.

### Required functionality

* User registration
* Login
* Logout / token invalidation
* JWT authentication
* Get current user
* Update profile
* Change password

### Example endpoints

```text
POST   /api/auth/register/
POST   /api/auth/login/
POST   /api/auth/logout/
GET    /api/auth/me/
PATCH  /api/auth/me/
POST   /api/auth/change-password/
```

---

# 2. Projects

Authenticated users can create and manage projects.

### Project fields

```text
id
name
description
created_by
created_at
updated_at
```

### Requirements

A user can:

* Create a project
* Update a project
* Delete a project
* View a project
* List their projects

Only users who have access to a project should be able to see it.

---

# 3. Project Members

Projects should support multiple users.

Each member has a role:

```text
owner
admin
member
```

### Permissions

#### Owner

Can:

* Update project
* Delete project
* Add members
* Remove members
* Change member roles
* Create/update/delete tasks

#### Admin

Can:

* Update project
* Add members
* Remove members
* Create/update/delete tasks

#### Member

Can:

* View project
* View tasks
* Create tasks
* Update tasks
* Update tasks assigned to them

Members should not be able to manage project permissions.

---

# 4. Tasks

Each project can contain multiple tasks.

### Task fields

```text
id
project
title
description
status
priority
assignee
created_by
due_date
created_at
updated_at
```

### Status

```text
todo
in_progress
done
```

### Priority

```text
low
medium
high
critical
```

---

# 5. Task API

Implement the following functionality:

### Create

```text
POST /api/projects/{project_id}/tasks/
```

### List

```text
GET /api/projects/{project_id}/tasks/
```

### Retrieve

```text
GET /api/tasks/{task_id}/
```

### Update

```text
PATCH /api/tasks/{task_id}/
```

### Delete

```text
DELETE /api/tasks/{task_id}/
```

---

# 6. Filtering

The task API must support filtering.

Example:

```text
GET /api/projects/1/tasks/?status=in_progress
```

Multiple filters should be supported:

```text
GET /api/projects/1/tasks/?status=todo&priority=high
```

Supported filters:

* status
* priority
* assignee
* created_by
* due_date

---

# 7. Search

Implement task search by title.

Example:

```text
GET /api/projects/1/tasks/?search=authentication
```

The search should be case-insensitive.

---

# 8. Sorting

The API should support sorting.

Example:

```text
GET /api/projects/1/tasks/?ordering=created_at
```

Descending:

```text
GET /api/projects/1/tasks/?ordering=-created_at
```

Possible ordering fields:

```text
created_at
updated_at
due_date
priority
```

---

# 9. Pagination

All list endpoints must use pagination.

Example:

```text
GET /api/projects/1/tasks/?page=2&page_size=20
```

Do not return unlimited querysets.

---

# 🧠 Architecture Requirements

Do not put all business logic inside views.

The project should have a clean structure.

Example:

```text
project/
│
├── apps/
│   ├── users/
│   ├── projects/
│   ├── tasks/
│   └── common/
│
├── config/
│   ├── settings/
│   ├── urls.py
│   └── wsgi.py
│
├── tests/
│
├── manage.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

You are free to choose a different structure if you can explain why.

---

# 🔐 Permissions

Implement proper object-level permissions.

Examples:

* A user cannot access a project they are not a member of.
* A member cannot delete a project.
* A member cannot change another member's role.
* A user cannot assign a task to someone who is not a member of the project.
* A user cannot modify tasks from another project.

Do not rely only on frontend restrictions.

All authorization must be enforced on the backend.

---

# ⚡ Performance

The API should be designed to avoid unnecessary database queries.

Pay attention to:

* `select_related`
* `prefetch_related`
* database indexes
* queryset optimization
* pagination

You should be able to explain how you prevented N+1 queries.

---

# 🗄 Database

Use PostgreSQL.

Think about appropriate indexes.

For example:

```text
Task.status
Task.priority
Task.assignee
Task.project
Task.created_at
```

Do not blindly add indexes everywhere.

Be able to explain why each index exists.

---

# 🔄 Concurrency

Consider the following situation:

Two users open the same task.

User A changes:

```text
status = in_progress
```

User B changes:

```text
priority = critical
```

Your API should behave predictably when concurrent updates happen.

Think about:

* transactions
* `select_for_update`
* optimistic locking
* race conditions

You don't necessarily need to implement every technique, but you should understand the problem and document your approach.

---

# 🧪 Testing

Write automated tests.

At minimum, test:

### Authentication

* Registration
* Login
* Unauthorized requests
* Password change

### Projects

* Create project
* Update project
* Delete project
* Project visibility

### Permissions

* Owner permissions
* Admin permissions
* Member permissions
* Unauthorized access

### Tasks

* Create task
* Update task
* Delete task
* Filtering
* Search
* Pagination

### Edge cases

Test invalid input and unexpected situations.

Example:

```text
User A tries to access Project B.
```

The API must reject the request.

---

# 🚀 Bonus Features

Once the core functionality is complete, implement additional features.

## Redis

Use Redis for caching or other appropriate functionality.

---

## Celery

Use Celery for asynchronous jobs.

Example:

```text
When a user is assigned a task,
send an email notification asynchronously.
```

---

## Email Notifications

Send notifications when:

* A user is added to a project
* A user is assigned a task
* A task is updated

---

# 📜 Audit Log

Implement an audit log.

Example:

```text
User: John
Action: TASK_UPDATED
Task: Fix authentication bug
Timestamp: 2026-09-13 12:30:00
```

Track important actions such as:

* Project created
* Member added
* Member removed
* Role changed
* Task created
* Task updated
* Task deleted

---

# 🗑 Soft Delete

Implement soft deletion for tasks.

Instead of permanently deleting:

```text
DELETE FROM tasks;
```

store information such as:

```text
deleted_at
```

Deleted tasks should not appear in normal API responses.

---

# 📚 API Documentation

Document the API using OpenAPI / Swagger.

The documentation should describe:

* Authentication
* Endpoints
* Request parameters
* Request bodies
* Response formats
* Error responses
* Authentication requirements

---

# 🐳 Docker

The application should be runnable using:

```bash
docker compose up
```

The Docker environment should contain at least:

```text
Django
PostgreSQL
```

Bonus:

```text
Redis
Celery
Celery Beat
```

---

# 🔄 CI/CD

Create a GitHub Actions workflow.

The workflow should:

1. Install dependencies
2. Run linting
3. Run tests
4. Build the Docker image

The pipeline should fail if tests fail.

---

# 🌐 Frontend — Optional

Build a simple React frontend.

The frontend should allow users to:

* Login
* View projects
* Create projects
* View tasks
* Create tasks
* Edit tasks
* Filter tasks
* Assign tasks
* Change task status

You don't need to build a beautiful UI.

Focus on communication between React and the DRF API.

---

# 📋 Definition of Done

The project is considered complete when:

* [ ] Authentication works
* [ ] JWT authentication is implemented
* [ ] Projects can be created and managed
* [ ] Project members and roles work
* [ ] Tasks can be created and managed
* [ ] Permissions are enforced
* [ ] Filtering works
* [ ] Search works
* [ ] Sorting works
* [ ] Pagination works
* [ ] PostgreSQL is used
* [ ] N+1 queries are avoided
* [ ] Database indexes are considered
* [ ] Automated tests are implemented
* [ ] API documentation exists
* [ ] Docker setup works
* [ ] README explains the architecture

### Bonus

* [ ] Redis
* [ ] Celery
* [ ] Email notifications
* [ ] Audit log
* [ ] Soft delete
* [ ] GitHub Actions
* [ ] React frontend

---

# 🎓 Development Rules

Before writing code:

1. Design the database schema.
2. Design the API endpoints.
3. Define authentication and authorization rules.
4. Think about database indexes.
5. Decide where business logic should live.
6. Document important architectural decisions.

Do not start by writing serializers and views immediately.

The goal is not simply to make the CRUD work.

The goal is to build the project as a **real production-style backend**.

---

# 💼 Portfolio Goal

The finished project should demonstrate that you understand:

* Django
* Django REST Framework
* PostgreSQL
* REST API design
* Authentication
* Authorization
* Object-level permissions
* Database optimization
* Transactions
* Testing
* Docker
* Async processing
* Caching
* API documentation
* CI/CD
* Backend architecture

The final repository should be clean enough to show to a potential employer during a technical interview.
