import random
import json

# Mock data for demo purposes
TEAM_MEMBERS = [
    {"id": 1, "name": "Alex Johnson", "role": "Senior Developer", "skills": ["Python", "React", "AWS"], "experience": 7, "availability": 30},
    {"id": 2, "name": "Sam Williams", "role": "Frontend Developer", "skills": ["JavaScript", "Vue", "CSS"], "experience": 4, "availability": 70},
    {"id": 3, "name": "Taylor Brown", "role": "Backend Developer", "skills": ["Java", "Spring", "PostgreSQL"], "experience": 5, "availability": 50},
    {"id": 4, "name": "Jordan Smith", "role": "DevOps Engineer", "skills": ["Docker", "Kubernetes", "CI/CD"], "experience": 6, "availability": 20},
    {"id": 5, "name": "Casey Miller", "role": "QA Engineer", "skills": ["Selenium", "Test Automation", "JIRA"], "experience": 3, "availability": 90},
    {"id": 6, "name": "Riley Davis", "role": "Full Stack Developer", "skills": ["Python", "React", "MongoDB"], "experience": 4, "availability": 60},
    {"id": 7, "name": "Morgan Wilson", "role": "UI/UX Designer", "skills": ["Figma", "Sketch", "UI Design"], "experience": 5, "availability": 80},
    {"id": 8, "name": "Jamie Parker", "role": "Security Specialist", "skills": ["Python", "Security", "API Integration"], "experience": 6, "availability": 45},
]

ISSUES = [
    {"id": 101, "title": "API Integration with Payment Gateway", "skills": ["Python", "API Integration", "Security"], "complexity": 4},
    {"id": 102, "title": "Dashboard UI Redesign", "skills": ["React", "CSS", "UI Design"], "complexity": 3},
    {"id": 103, "title": "Database Performance Optimization", "skills": ["PostgreSQL", "SQL", "Performance Tuning"], "complexity": 5},
    {"id": 104, "title": "Authentication Service Refactoring", "skills": ["Java", "Security", "Microservices"], "complexity": 4},
    {"id": 105, "title": "Mobile Responsive Layout", "skills": ["CSS", "HTML", "UI Design"], "complexity": 2},
    {"id": 106, "title": "CI/CD Pipeline Setup", "skills": ["Docker", "CI/CD", "Shell Scripting"], "complexity": 3}
]

HISTORICAL_REFERENCES = [
    {"issue_id": 95, "title": "Payment Gateway Integration v1", "related_to": 101, "description": "Initial integration with Stripe completed in Sprint 24. See merge request !245 for implementation details."},
    {"issue_id": 87, "title": "Admin Dashboard Design", "related_to": 102, "description": "Previous dashboard design principles documented in Confluence under 'Design System > Dashboards'. Used component library v2."},
    {"issue_id": 76, "title": "Query Optimization for Reports", "related_to": 103, "description": "Database indexing strategy documented in issue #76. Improved query performance by 45%."},
    {"issue_id": 54, "title": "Auth Service Initial Implementation", "related_to": 104, "description": "Original authentication service created in Sprint 18. Architecture diagram available in project wiki."},
]

UTILIZATION_DATA = {
    "overutilized": [
        {"id": 1, "name": "Alex Johnson", "role": "Senior Developer", "utilization": 95, "issues": [101, 104]},
        {"id": 4, "name": "Jordan Smith", "role": "DevOps Engineer", "utilization": 90, "issues": [106]}
    ],
    "underutilized": [
        {"id": 5, "name": "Casey Miller", "role": "QA Engineer", "utilization": 25, "issues": []},
        {"id": 2, "name": "Sam Williams", "role": "Frontend Developer", "utilization": 40, "issues": [105]}
    ]
}

PROJECT_STATS = {
    "sprint_progress": {"completed": 68, "in_progress": 22, "todo": 10},
    "team_velocity": [21, 24, 22, 25, 23, 26, 28],
    "issue_distribution": {"bugs": 15, "features": 45, "tech_debt": 25, "docs": 15},
    "skill_coverage": {"Python": 85, "JavaScript": 70, "DevOps": 60, "Java": 50, "QA": 65}
}

def generate_response(intent, entities):
    """
    Generate a response based on the identified intent and entities.
    
    Args:
        intent (str): The identified intent
        entities (dict): The extracted entities
        
    Returns:
        dict: Response object with message and optional data
    """
    if intent == 'general':
        return generate_general_response(entities)
    elif intent == 'resource_allocation':
        return generate_resource_allocation_response(entities)
    elif intent == 'reference':
        return generate_reference_response(entities)
    elif intent == 'custom_report':
        return generate_report_response(entities)
    elif intent == 'issue_tracking':
        return generate_issue_tracking_response(entities)
    else:
        return {
            'type': 'text',
            'message': "I'm not sure I understand what you're asking. Could you rephrase or try asking about resource allocation, historical references, custom reports, or issue tracking?"
        }

def generate_general_response(entities):
    """Generate a general response for greetings and help requests."""
    if any(word in entities.get('greeting', '') for word in ['hello', 'hi', 'hey', 'greetings']):
        return {
            'type': 'text',
            'message': "Hello! I'm your Capacity Management Assistant. I can help with resource allocation, provide historical references, generate custom reports, and assist with issue tracking. How can I help you today?"
        }
    else:
        return {
            'type': 'text',
            'message': "I'm your Capacity Management Assistant. I can help with:\n\n" +
                      "1. Resource allocation (e.g., 'Give me top 3 resources for issue #101')\n" +
                      "2. Historical references (e.g., 'Find similar issues to #102')\n" +
                      "3. Custom reports (e.g., 'Show team utilization report')\n" +
                      "4. Issue tracking (e.g., 'Update status for issue #103')\n\n" +
                      "What would you like to know about?"
        }

def generate_resource_allocation_response(entities):
    """Generate resource allocation recommendations."""
    if 'utilization' in entities:
        utilization_type = entities['utilization']
        if utilization_type == 'under':
            data = UTILIZATION_DATA['underutilized']
            message = "Here are the under-utilized resources:"
            for resource in data:
                message += f"\n- {resource['name']} ({resource['role']}): {resource['utilization']}% utilized"
                if not resource['issues']:
                    message += " - No current assignments"
                else:
                    message += f" - Working on {len(resource['issues'])} issues"
            
            return {
                'type': 'utilization',
                'message': message,
                'data': {
                    'utilization_type': 'under',
                    'resources': data
                }
            }
        elif utilization_type == 'over':
            data = UTILIZATION_DATA['overutilized']
            message = "Here are the over-utilized resources:"
            for resource in data:
                message += f"\n- {resource['name']} ({resource['role']}): {resource['utilization']}% utilized"
                if resource['issues']:
                    message += f" - Working on {len(resource['issues'])} issues"
            
            return {
                'type': 'utilization',
                'message': message,
                'data': {
                    'utilization_type': 'over',
                    'resources': data
                }
            }
    
    if 'issue_id' in entities:
        issue_id = int(entities['issue_id'])
        count = entities.get('resource_count', 3)
        
        # Find the issue
        issue = None
        for i in ISSUES:
            if i['id'] == issue_id:
                issue = i
                break
        
        if not issue:
            return {
                'type': 'text',
                'message': f"I couldn't find issue #{issue_id}. Please verify the issue number and try again."
            }
        
        # Find team members with matching skills
        matching_members = []
        for member in TEAM_MEMBERS:
            skill_match_count = sum(1 for skill in issue['skills'] if skill in member['skills'])
            if skill_match_count > 0:
                # Calculate a score based on skill match, experience, and availability
                score = (skill_match_count / len(issue['skills'])) * 0.5 + \
                       (min(member['experience'], 10) / 10) * 0.3 + \
                       (member['availability'] / 100) * 0.2
                
                matching_members.append({
                    **member,
                    'score': round(score * 100),
                    'skill_match': skill_match_count,
                    'skill_match_percent': round((skill_match_count / len(issue['skills'])) * 100)
                })
        
        # Sort by score and take top N
        matching_members.sort(key=lambda x: x['score'], reverse=True)
        top_members = matching_members[:count]
        
        if not top_members:
            return {
                'type': 'text',
                'message': f"I couldn't find any team members with skills matching issue #{issue_id} ({issue['title']}). The required skills are: {', '.join(issue['skills'])}."
            }
        
        message = f"Top {len(top_members)} recommended resources for issue #{issue_id} ({issue['title']}):\n\n"
        for idx, member in enumerate(top_members):
            message += f"{idx+1}. {member['name']} ({member['role']})\n"
            message += f"   Skills: {', '.join(member['skills'])}\n"
            message += f"   Experience: {member['experience']} years\n"
            message += f"   Availability: {member['availability']}%\n"
            message += f"   Match score: {member['score']}%\n"
            message += f"   Skill match: {member['skill_match_percent']}% ({member['skill_match']}/{len(issue['skills'])} skills)\n\n"
        
        return {
            'type': 'resource_allocation',
            'message': message,
            'data': {
                'issue': issue,
                'recommended_resources': top_members
            }
        }
    
    # General resource allocation overview
    return {
        'type': 'text',
        'message': "For resource allocation, I can help you with:\n\n" +
                  "1. Finding the best resources for a specific issue (e.g., 'Give me top 3 resources for issue #101')\n" +
                  "2. Identifying under-utilized or over-utilized team members (e.g., 'Show over-utilized resources')\n\n" +
                  "Please specify what you'd like to know."
    }

def generate_reference_response(entities):
    """Generate historical references for similar issues."""
    if 'issue_id' in entities:
        issue_id = int(entities['issue_id'])
        
        # Find the issue
        issue = None
        for i in ISSUES:
            if i['id'] == issue_id:
                issue = i
                break
        
        if not issue:
            return {
                'type': 'text',
                'message': f"I couldn't find issue #{issue_id}. Please verify the issue number and try again."
            }
        
        # Find historical references
        references = []
        for ref in HISTORICAL_REFERENCES:
            if ref['related_to'] == issue_id:
                references.append(ref)
        
        if not references:
            # If no direct match, find references based on skills
            for ref in HISTORICAL_REFERENCES:
                related_issue = next((i for i in ISSUES if i['id'] == ref['related_to']), None)
                if related_issue:
                    skill_match = any(skill in issue['skills'] for skill in related_issue['skills'])
                    if skill_match:
                        references.append(ref)
        
        if not references:
            return {
                'type': 'text',
                'message': f"I couldn't find any historical references for issue #{issue_id} ({issue['title']}). This appears to be a new type of task for the team."
            }
        
        message = f"Historical references for issue #{issue_id} ({issue['title']}):\n\n"
        for ref in references:
            message += f"- Issue #{ref['issue_id']}: {ref['title']}\n"
            message += f"  {ref['description']}\n\n"
        
        return {
            'type': 'reference',
            'message': message,
            'data': {
                'issue': issue,
                'references': references
            }
        }
    
    return {
        'type': 'text',
        'message': "I can help you find historical references for similar issues. Please specify an issue number, for example: 'Find references for issue #101'."
    }

def generate_report_response(entities):
    """Generate custom reports with visualizations."""
    report_types = [
        'sprint progress', 'team velocity', 'issue distribution', 
        'skill coverage', 'resource utilization'
    ]
    
    # Check if a specific report type is requested
    requested_report = None
    for report_type in report_types:
        if report_type in ' '.join(entities.values()):
            requested_report = report_type
            break
    
    if requested_report == 'sprint progress':
        progress = PROJECT_STATS['sprint_progress']
        message = "Sprint Progress Report:\n\n"
        message += f"Completed: {progress['completed']}%\n"
        message += f"In Progress: {progress['in_progress']}%\n"
        message += f"To Do: {progress['todo']}%\n"
        
        return {
            'type': 'chart',
            'message': message,
            'data': {
                'chart_type': 'pie',
                'title': 'Sprint Progress',
                'labels': ['Completed', 'In Progress', 'To Do'],
                'datasets': [{
                    'data': [progress['completed'], progress['in_progress'], progress['todo']],
                    'backgroundColor': ['#28a745', '#ffc107', '#6c757d']
                }]
            }
        }
    
    elif requested_report == 'team velocity':
        velocity = PROJECT_STATS['team_velocity']
        message = "Team Velocity Report (Last 7 Sprints):\n\n"
        message += f"Current Velocity: {velocity[-1]} story points\n"
        message += f"Average Velocity: {sum(velocity) / len(velocity):.1f} story points\n"
        message += f"Trend: {'Increasing' if velocity[-1] > velocity[0] else 'Decreasing'}\n"
        
        return {
            'type': 'chart',
            'message': message,
            'data': {
                'chart_type': 'line',
                'title': 'Team Velocity (Last 7 Sprints)',
                'labels': [f'Sprint -{len(velocity) - i}' for i in range(len(velocity))],
                'datasets': [{
                    'label': 'Story Points',
                    'data': velocity,
                    'borderColor': '#007bff',
                    'backgroundColor': 'rgba(0, 123, 255, 0.1)',
                }]
            }
        }
    
    elif requested_report == 'issue distribution':
        distribution = PROJECT_STATS['issue_distribution']
        message = "Issue Distribution Report:\n\n"
        for category, percentage in distribution.items():
            message += f"{category.title()}: {percentage}%\n"
        
        return {
            'type': 'chart',
            'message': message,
            'data': {
                'chart_type': 'bar',
                'title': 'Issue Distribution',
                'labels': [k.title() for k in distribution.keys()],
                'datasets': [{
                    'label': 'Percentage',
                    'data': list(distribution.values()),
                    'backgroundColor': ['#dc3545', '#28a745', '#17a2b8', '#6c757d'],
                }]
            }
        }
    
    elif requested_report == 'skill coverage':
        coverage = PROJECT_STATS['skill_coverage']
        message = "Team Skill Coverage Report:\n\n"
        for skill, percentage in coverage.items():
            message += f"{skill}: {percentage}%\n"
        
        return {
            'type': 'chart',
            'message': message,
            'data': {
                'chart_type': 'radar',
                'title': 'Team Skill Coverage',
                'labels': list(coverage.keys()),
                'datasets': [{
                    'label': 'Coverage (%)',
                    'data': list(coverage.values()),
                    'backgroundColor': 'rgba(54, 162, 235, 0.2)',
                    'borderColor': 'rgb(54, 162, 235)',
                }]
            }
        }
    
    elif requested_report == 'resource utilization':
        over_utilized = UTILIZATION_DATA['overutilized']
        under_utilized = UTILIZATION_DATA['underutilized']
        
        # Get all team members
        all_members = TEAM_MEMBERS.copy()
        
        # Create utilization data for chart
        names = [member['name'] for member in all_members]
        utilization = []
        
        for member in all_members:
            # Find utilization value
            util_value = None
            
            # Check in over-utilized
            for over in over_utilized:
                if over['id'] == member['id']:
                    util_value = over['utilization']
                    break
            
            # Check in under-utilized
            if util_value is None:
                for under in under_utilized:
                    if under['id'] == member['id']:
                        util_value = under['utilization']
                        break
            
            # If not found, generate a random value between 40-80
            if util_value is None:
                util_value = 100 - member['availability']
            
            utilization.append(util_value)
        
        message = "Resource Utilization Report:\n\n"
        message += "Over-utilized resources (>80%):\n"
        for resource in over_utilized:
            message += f"- {resource['name']}: {resource['utilization']}%\n"
        
        message += "\nUnder-utilized resources (<40%):\n"
        for resource in under_utilized:
            message += f"- {resource['name']}: {resource['utilization']}%\n"
        
        return {
            'type': 'chart',
            'message': message,
            'data': {
                'chart_type': 'bar',
                'title': 'Team Resource Utilization',
                'labels': names,
                'datasets': [{
                    'label': 'Utilization (%)',
                    'data': utilization,
                    'backgroundColor': [
                        '#28a745' if util < 70 else ('#ffc107' if util < 85 else '#dc3545')
                        for util in utilization
                    ],
                }]
            }
        }
    
    # If no specific report is requested, provide a list of available reports
    message = "I can generate the following custom reports:\n\n"
    message += "1. Sprint Progress Report - Current sprint completion status\n"
    message += "2. Team Velocity Report - Performance trends over sprints\n"
    message += "3. Issue Distribution Report - Breakdown of issue types\n"
    message += "4. Skill Coverage Report - Team skill competencies\n"
    message += "5. Resource Utilization Report - Team member workload analysis\n\n"
    message += "Which report would you like to see?"
    
    return {
        'type': 'text',
        'message': message
    }

def generate_issue_tracking_response(entities):
    """Generate issue tracking and standup updates."""
    if 'issue_id' in entities:
        issue_id = int(entities['issue_id'])
        
        # Find the issue
        issue = None
        for i in ISSUES:
            if i['id'] == issue_id:
                issue = i
                break
        
        if not issue:
            return {
                'type': 'text',
                'message': f"I couldn't find issue #{issue_id}. Please verify the issue number and try again."
            }
        
        # Simulate a GitLab issue comment
        message = f"I've added a comment to issue #{issue_id} ({issue['title']}):\n\n"
        message += f"--- GitLab Comment ---\n"
        message += f"Daily Standup Update:\n"
        message += f"- Issue is currently being worked on by {random.choice(TEAM_MEMBERS)['name']}\n"
        message += f"- Status: In Progress\n"
        message += f"- Progress: ~{random.randint(30, 70)}% complete\n"
        message += f"- Next steps: Completing the implementation and preparing for code review\n"
        message += f"- Blockers: None identified at this time\n"
        message += f"---------------------\n\n"
        message += "The issue has been updated and stakeholders have been notified."
        
        return {
            'type': 'issue_update',
            'message': message,
            'data': {
                'issue': issue,
                'update_time': 'just now',
                'status': 'In Progress'
            }
        }
    
    # If no specific issue is requested, provide info about standup process
    standup_summary = "Daily Standup Summary:\n\n"
    
    # Pick 3 random team members for the standup update
    standup_members = random.sample(TEAM_MEMBERS, 3)
    
    for member in standup_members:
        standup_summary += f"{member['name']}:\n"
        
        # Randomly pick if they completed something yesterday
        if random.choice([True, False]):
            completed_issue = random.choice(ISSUES)
            standup_summary += f"- Completed issue #{completed_issue['id']}: {completed_issue['title']}\n"
        else:
            in_progress_issue = random.choice(ISSUES)
            progress = random.randint(30, 90)
            standup_summary += f"- Working on issue #{in_progress_issue['id']}: {in_progress_issue['title']} ({progress}% complete)\n"
        
        # Add what they're working on today
        today_issue = random.choice(ISSUES)
        standup_summary += f"- Today: Continue work on issue #{today_issue['id']}: {today_issue['title']}\n"
        
        # Random blocker (20% chance)
        if random.random() < 0.2:
            standup_summary += f"- Blocker: Waiting for design approval from the UX team\n"
        else:
            standup_summary += f"- No blockers reported\n"
        
        standup_summary += "\n"
    
    message = "I've captured the following standup updates and added them to the relevant GitLab issues:\n\n"
    message += standup_summary
    
    return {
        'type': 'standup',
        'message': message,
        'data': {
            'standup_date': 'today',
            'team_members': [m['name'] for m in standup_members]
        }
    }
