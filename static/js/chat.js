document.addEventListener('DOMContentLoaded', function() {
    const chatForm = document.getElementById('chat-form');
    const userInput = document.getElementById('user-input');
    const chatMessages = document.getElementById('chat-messages');
    const suggestedQueries = document.querySelectorAll('.suggested-query');
    
    // Initial greeting
    addBotMessage({
        type: 'text',
        message: "Hello! I'm your Capacity Management Assistant. I can help with resource allocation, provide historical references, generate custom reports, and assist with issue tracking. How can I help you today?"
    });
    
    // Handle form submission
    chatForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const message = userInput.value.trim();
        if (!message) return;
        
        // Add user message to chat
        addUserMessage(message);
        
        // Clear input
        userInput.value = '';
        
        // Show typing indicator
        addTypingIndicator();
        
        // Send message to server
        fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: message })
        })
        .then(response => response.json())
        .then(data => {
            // Remove typing indicator
            removeTypingIndicator();
            
            // Add bot response
            addBotMessage(data);
        })
        .catch(error => {
            console.error('Error:', error);
            removeTypingIndicator();
            addBotMessage({
                type: 'text',
                message: "Sorry, there was an error processing your request. Please try again."
            });
        });
    });
    
    // Handle suggested queries
    suggestedQueries.forEach(query => {
        query.addEventListener('click', function() {
            const queryText = this.textContent;
            userInput.value = queryText;
            chatForm.dispatchEvent(new Event('submit'));
        });
    });
    
    // Function to add user message to chat
    function addUserMessage(message) {
        const messageElement = document.createElement('div');
        messageElement.className = 'message user-message';
        messageElement.innerHTML = `
            <div class="message-content">
                <p>${escapeHtml(message)}</p>
            </div>
        `;
        chatMessages.appendChild(messageElement);
        scrollToBottom();
    }
    
    // Function to add bot message to chat
    function addBotMessage(data) {
        const messageElement = document.createElement('div');
        messageElement.className = 'message bot-message';
        
        let content = `<p>${formatMessage(data.message)}</p>`;
        
        // If it's a chart type, add a chart container
        if (data.type === 'chart' && data.data) {
            const chartId = 'chart-' + Date.now();
            content += `<div class="chart-container"><canvas id="${chartId}"></canvas></div>`;
            
            // Defer chart creation until after the element is added to DOM
            setTimeout(() => {
                createChart(chartId, data.data);
            }, 100);
        }
        
        messageElement.innerHTML = `
            <div class="message-avatar">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-cpu"><rect x="4" y="4" width="16" height="16" rx="2" ry="2"></rect><rect x="9" y="9" width="6" height="6"></rect><line x1="9" y1="1" x2="9" y2="4"></line><line x1="15" y1="1" x2="15" y2="4"></line><line x1="9" y1="20" x2="9" y2="23"></line><line x1="15" y1="20" x2="15" y2="23"></line><line x1="20" y1="9" x2="23" y2="9"></line><line x1="20" y1="14" x2="23" y2="14"></line><line x1="1" y1="9" x2="4" y2="9"></line><line x1="1" y1="14" x2="4" y2="14"></line></svg>
            </div>
            <div class="message-content">
                ${content}
            </div>
        `;
        
        chatMessages.appendChild(messageElement);
        scrollToBottom();
    }
    
    // Add typing indicator
    function addTypingIndicator() {
        const typingElement = document.createElement('div');
        typingElement.className = 'message bot-message typing-indicator';
        typingElement.innerHTML = `
            <div class="message-avatar">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-cpu"><rect x="4" y="4" width="16" height="16" rx="2" ry="2"></rect><rect x="9" y="9" width="6" height="6"></rect><line x1="9" y1="1" x2="9" y2="4"></line><line x1="15" y1="1" x2="15" y2="4"></line><line x1="9" y1="20" x2="9" y2="23"></line><line x1="15" y1="20" x2="15" y2="23"></line><line x1="20" y1="9" x2="23" y2="9"></line><line x1="20" y1="14" x2="23" y2="14"></line><line x1="1" y1="9" x2="4" y2="9"></line><line x1="1" y1="14" x2="4" y2="14"></line></svg>
            </div>
            <div class="message-content">
                <div class="dots">
                    <span class="dot"></span>
                    <span class="dot"></span>
                    <span class="dot"></span>
                </div>
            </div>
        `;
        chatMessages.appendChild(typingElement);
        scrollToBottom();
    }
    
    // Remove typing indicator
    function removeTypingIndicator() {
        const typingIndicator = document.querySelector('.typing-indicator');
        if (typingIndicator) {
            typingIndicator.remove();
        }
    }
    
    // Format message with newlines
    function formatMessage(message) {
        return escapeHtml(message).replace(/\n/g, '<br>');
    }
    
    // Escape HTML to prevent XSS
    function escapeHtml(unsafe) {
        return unsafe
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;")
            .replace(/"/g, "&quot;")
            .replace(/'/g, "&#039;");
    }
    
    // Scroll chat to bottom
    function scrollToBottom() {
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
});

// Function to create charts
function createChart(chartId, chartData) {
    const ctx = document.getElementById(chartId).getContext('2d');
    
    let chartConfig = {
        type: chartData.chart_type,
        data: {
            labels: chartData.labels,
            datasets: chartData.datasets
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                title: {
                    display: true,
                    text: chartData.title,
                    color: '#fff'
                },
                legend: {
                    labels: {
                        color: '#fff'
                    }
                }
            },
            scales: {}
        }
    };
    
    // Add specific options for different chart types
    if (chartData.chart_type === 'line' || chartData.chart_type === 'bar') {
        chartConfig.options.scales = {
            x: {
                ticks: {
                    color: '#ccc'
                },
                grid: {
                    color: 'rgba(255, 255, 255, 0.1)'
                }
            },
            y: {
                ticks: {
                    color: '#ccc'
                },
                grid: {
                    color: 'rgba(255, 255, 255, 0.1)'
                }
            }
        };
    }
    
    if (chartData.chart_type === 'radar') {
        chartConfig.options.scales = {
            r: {
                pointLabels: {
                    color: '#ccc'
                },
                grid: {
                    color: 'rgba(255, 255, 255, 0.1)'
                },
                ticks: {
                    color: '#ccc',
                    backdropColor: 'transparent'
                }
            }
        };
    }
    
    new Chart(ctx, chartConfig);
}
