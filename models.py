# Not using database models for this demo as we're using hardcoded responses
# This file is a placeholder for future extension with real database integration

class MockUser:
    """Mock user model for demo purposes."""
    def __init__(self, id, name, role, skills, experience, availability):
        self.id = id
        self.name = name
        self.role = role
        self.skills = skills  # List of skills
        self.experience = experience  # Years of experience
        self.availability = availability  # Percentage available (0-100)
        
class MockIssue:
    """Mock GitLab issue model for demo purposes."""
    def __init__(self, id, title, description, status, required_skills, complexity):
        self.id = id
        self.title = title
        self.description = description
        self.status = status  # Open, In Progress, Closed
        self.required_skills = required_skills  # List of required skills
        self.complexity = complexity  # 1-5 scale
