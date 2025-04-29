document.addEventListener('DOMContentLoaded', function() {
    // Create dashboard charts
    createSprintProgressChart();
    createTeamVelocityChart();
    createIssueDistributionChart();
    createResourceUtilizationChart();
    createSkillCoverageChart();
});

// Sprint Progress Chart
function createSprintProgressChart() {
    const ctx = document.getElementById('sprint-progress-chart').getContext('2d');
    
    const data = {
        labels: ['Completed', 'In Progress', 'To Do'],
        datasets: [{
            data: [68, 22, 10],
            backgroundColor: ['#28a745', '#ffc107', '#6c757d'],
            borderWidth: 1
        }]
    };
    
    new Chart(ctx, {
        type: 'pie',
        data: data,
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                title: {
                    display: true,
                    text: 'Sprint Progress',
                    color: '#fff',
                    font: {
                        size: 16
                    }
                },
                legend: {
                    position: 'right',
                    labels: {
                        color: '#fff'
                    }
                }
            }
        }
    });
}

// Team Velocity Chart
function createTeamVelocityChart() {
    const ctx = document.getElementById('team-velocity-chart').getContext('2d');
    
    const data = {
        labels: ['Sprint -7', 'Sprint -6', 'Sprint -5', 'Sprint -4', 'Sprint -3', 'Sprint -2', 'Sprint -1'],
        datasets: [{
            label: 'Story Points',
            data: [21, 24, 22, 25, 23, 26, 28],
            borderColor: '#007bff',
            backgroundColor: 'rgba(0, 123, 255, 0.1)',
            tension: 0.1,
            fill: true
        }]
    };
    
    new Chart(ctx, {
        type: 'line',
        data: data,
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                title: {
                    display: true,
                    text: 'Team Velocity (Last 7 Sprints)',
                    color: '#fff',
                    font: {
                        size: 16
                    }
                },
                legend: {
                    labels: {
                        color: '#fff'
                    }
                }
            },
            scales: {
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
                    },
                    beginAtZero: true
                }
            }
        }
    });
}

// Issue Distribution Chart
function createIssueDistributionChart() {
    const ctx = document.getElementById('issue-distribution-chart').getContext('2d');
    
    const data = {
        labels: ['Bugs', 'Features', 'Tech Debt', 'Docs'],
        datasets: [{
            label: 'Percentage',
            data: [15, 45, 25, 15],
            backgroundColor: ['#dc3545', '#28a745', '#17a2b8', '#6c757d'],
            borderWidth: 1
        }]
    };
    
    new Chart(ctx, {
        type: 'bar',
        data: data,
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                title: {
                    display: true,
                    text: 'Issue Distribution',
                    color: '#fff',
                    font: {
                        size: 16
                    }
                },
                legend: {
                    display: false
                }
            },
            scales: {
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
                    },
                    beginAtZero: true
                }
            }
        }
    });
}

// Resource Utilization Chart
function createResourceUtilizationChart() {
    const ctx = document.getElementById('resource-utilization-chart').getContext('2d');
    
    const data = {
        labels: [
            'Alex Johnson', 
            'Sam Williams', 
            'Taylor Brown', 
            'Jordan Smith', 
            'Casey Miller', 
            'Riley Davis', 
            'Morgan Wilson'
        ],
        datasets: [{
            label: 'Utilization (%)',
            data: [95, 40, 65, 90, 25, 60, 70],
            backgroundColor: [
                '#dc3545', // Over 85% - Red
                '#28a745', // Under 70% - Green
                '#ffc107', // Between 70-85% - Yellow
                '#dc3545', // Over 85% - Red
                '#28a745', // Under 70% - Green
                '#28a745', // Under 70% - Green
                '#ffc107'  // Between 70-85% - Yellow
            ],
            borderWidth: 1
        }]
    };
    
    new Chart(ctx, {
        type: 'bar',
        data: data,
        options: {
            indexAxis: 'y',
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                title: {
                    display: true,
                    text: 'Team Resource Utilization',
                    color: '#fff',
                    font: {
                        size: 16
                    }
                },
                legend: {
                    display: false
                }
            },
            scales: {
                x: {
                    ticks: {
                        color: '#ccc'
                    },
                    grid: {
                        color: 'rgba(255, 255, 255, 0.1)'
                    },
                    max: 100
                },
                y: {
                    ticks: {
                        color: '#ccc'
                    },
                    grid: {
                        color: 'rgba(255, 255, 255, 0.1)'
                    }
                }
            }
        }
    });
}

// Skill Coverage Chart
function createSkillCoverageChart() {
    const ctx = document.getElementById('skill-coverage-chart').getContext('2d');
    
    const data = {
        labels: ['Python', 'JavaScript', 'DevOps', 'Java', 'QA'],
        datasets: [{
            label: 'Coverage (%)',
            data: [85, 70, 60, 50, 65],
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            borderColor: 'rgb(54, 162, 235)',
            pointBackgroundColor: 'rgb(54, 162, 235)',
            pointBorderColor: '#fff',
            pointHoverBackgroundColor: '#fff',
            pointHoverBorderColor: 'rgb(54, 162, 235)'
        }]
    };
    
    new Chart(ctx, {
        type: 'radar',
        data: data,
        options: {
            responsive: true,
            maintainAspectRatio: false,
            elements: {
                line: {
                    borderWidth: 3
                }
            },
            plugins: {
                title: {
                    display: true,
                    text: 'Team Skill Coverage',
                    color: '#fff',
                    font: {
                        size: 16
                    }
                },
                legend: {
                    display: false
                }
            },
            scales: {
                r: {
                    pointLabels: {
                        color: '#ccc',
                        font: {
                            size: 12
                        }
                    },
                    grid: {
                        color: 'rgba(255, 255, 255, 0.1)'
                    },
                    ticks: {
                        color: '#ccc',
                        backdropColor: 'transparent'
                    }
                }
            }
        }
    });
}
