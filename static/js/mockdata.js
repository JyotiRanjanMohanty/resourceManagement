// Mock data for the chatbot interface
const MOCK_TEAM_MEMBERS = [
    {
        "id": 1,
        "name": "Alex Johnson",
        "role": "Senior Developer",
        "skills": ["Python", "React", "AWS"],
        "experience": 7,
        "availability": 30
    },
    {
        "id": 2,
        "name": "Sam Williams",
        "role": "Frontend Developer",
        "skills": ["JavaScript", "Vue", "CSS"],
        "experience": 4,
        "availability": 70
    },
    {
        "id": 3,
        "name": "Taylor Brown",
        "role": "Backend Developer",
        "skills": ["Java", "Spring", "PostgreSQL"],
        "experience": 5,
        "availability": 50
    },
    {
        "id": 4,
        "name": "Jordan Smith",
        "role": "DevOps Engineer",
        "skills": ["Docker", "Kubernetes", "CI/CD"],
        "experience": 6,
        "availability": 20
    },
    {
        "id": 5,
        "name": "Casey Miller",
        "role": "QA Engineer",
        "skills": ["Selenium", "Test Automation", "JIRA"],
        "experience": 3,
        "availability": 90
    },
    {
        "id": 6,
        "name": "Riley Davis",
        "role": "Full Stack Developer",
        "skills": ["Python", "React", "MongoDB"],
        "experience": 4,
        "availability": 60
    },
    {
        "id": 7,
        "name": "Morgan Wilson",
        "role": "UI/UX Designer",
        "skills": ["Figma", "Sketch", "UI Design"],
        "experience": 5,
        "availability": 80
    },
    {
        "id": 8,
        "name": "Jamie Parker",
        "role": "Security Specialist",
        "skills": ["Python", "Security", "API Integration"],
        "experience": 6,
        "availability": 45
    }
];

const MOCK_ISSUES = [
    {
        "id": 101,
        "title": "API Integration with Payment Gateway",
        "description": "Integrate the application with Stripe payment gateway for handling subscriptions and one-time payments.",
        "status": "Open",
        "skills": ["Python", "API Integration", "Security"],
        "complexity": 4
    },
    {
        "id": 102,
        "title": "Dashboard UI Redesign",
        "description": "Redesign the admin dashboard UI to improve usability and incorporate the new brand guidelines.",
        "status": "In Progress",
        "skills": ["React", "CSS", "UI Design"],
        "complexity": 3
    },
    {
        "id": 103,
        "title": "Database Performance Optimization",
        "description": "Optimize database queries and indexing to improve overall system performance for reporting features.",
        "status": "Open",
        "skills": ["PostgreSQL", "SQL", "Performance Tuning"],
        "complexity": 5
    },
    {
        "id": 104,
        "title": "Authentication Service Refactoring",
        "description": "Refactor the authentication service to support multi-factor authentication and improve security.",
        "status": "In Progress",
        "skills": ["Java", "Security", "Microservices"],
        "complexity": 4
    },
    {
        "id": 105,
        "title": "Mobile Responsive Layout",
        "description": "Update the customer portal layout to be fully responsive on mobile devices.",
        "status": "Open", 
        "skills": ["CSS", "HTML", "UI Design"],
        "complexity": 2
    },
    {
        "id": 106,
        "title": "CI/CD Pipeline Setup",
        "description": "Set up a continuous integration and deployment pipeline for the backend services.",
        "status": "Open",
        "skills": ["Docker", "CI/CD", "Shell Scripting"],
        "complexity": 3
    }
];

const SUGGESTED_QUERIES = [
    "Give me top 3 resources for issue #101",
    "Show over-utilized resources",
    "Find references for issue #102",
    "Generate a skill coverage report",
    "Update status for issue #103",
    "Show team velocity report"
];
