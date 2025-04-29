import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download necessary NLTK data (will only run once)
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('punkt')
    nltk.download('stopwords')

# Define intent patterns
INTENT_PATTERNS = {
    'resource_allocation': [
        r'resource allocation', r'allocate resource', r'top resource', 
        r'who (can|should) (work|be assigned)', r'best (resource|person|team member)',
        r'under ?utilized', r'over ?utilized', r'available resource'
    ],
    'reference': [
        r'reference', r'similar (issue|task|problem)', r'previous (work|issue|task)', 
        r'how was .* done before', r'past examples'
    ],
    'custom_report': [
        r'report', r'status', r'dashboard', r'metrics', r'progress', 
        r'visualization', r'chart', r'graph', r'overview', r'summary'
    ],
    'issue_tracking': [
        r'(gitlab|git) issue', r'standup', r'comment', r'update (issue|task)', 
        r'track', r'progress update'
    ],
    'general': [
        r'hello', r'hi', r'hey', r'greetings', r'help', r'what can you do', 
        r'features', r'capabilities', r'assist', r'thank'
    ]
}

# Entity extraction patterns
ENTITY_PATTERNS = {
    'issue_id': r'issue #?(\d+)',
    'skill': r'skill(?:s)? (?:in )?(\w+(?:\s\w+)*)',
    'experience': r'(\d+)(?:\+)? years? (?:of )?experience',
    'resource_count': r'(?:top|best) (\d+) resources?',
    'utilization': r'(under|over)(?:\s|-)?utilized'
}

def process_query(query):
    """
    Process a user query to determine intent and extract entities.
    
    Args:
        query (str): The user's query
        
    Returns:
        tuple: (intent, entities)
    """
    # Lowercase the query for consistent matching
    query_lower = query.lower()
    
    # Determine intent
    intent = 'general'  # Default intent
    for potential_intent, patterns in INTENT_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, query_lower):
                intent = potential_intent
                break
        if intent != 'general':
            break
    
    # Extract entities
    entities = {}
    for entity_type, pattern in ENTITY_PATTERNS.items():
        match = re.search(pattern, query_lower)
        if match:
            entities[entity_type] = match.group(1)
    
    # Extract issue numbers (special case)
    issue_match = re.search(r'#(\d+)', query)
    if issue_match:
        entities['issue_id'] = issue_match.group(1)
    
    # Look for specific number of resources requested
    resource_count_match = re.search(r'top (\d+)|(\d+) resources?', query_lower)
    if resource_count_match:
        count = resource_count_match.group(1) or resource_count_match.group(2)
        entities['resource_count'] = int(count)
    else:
        # Default to 3 resources for resource allocation requests
        if intent == 'resource_allocation' and 'resource_count' not in entities:
            entities['resource_count'] = 3
    
    return intent, entities
