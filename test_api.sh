#!/bin/bash

curl -X POST http://localhost:8000/students/ -H "Content-Type: application/json" -d '{"name": "John", "email": "john@example.com"}'
curl -X POST http://localhost:8000/courses/ -H "Content-Type: application/json" -d '{"title": "Physics", "description": "Physics 101"}'
curl -X POST http://localhost:8000/enroll/ -H "Content-Type: application/json" -d '{"student_id": 1, "course_id": 1}'
curl http://localhost:8000/students/1
curl http://localhost:8000/courses/1
