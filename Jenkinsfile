pipeline {
    agent any
    
    environment {
        OPENWEATHER_API_KEY = credentials('openweather-api-key')
    }
    
    triggers {
        // Run daily at 9:00 AM
        cron('0 9 * * *')
    }
    
    stages {
        stage('Setup Python Environment') {
            steps {
                script {
                    // Create and activate virtual environment
                    sh '''
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install -r requirements.txt
                    '''
                }
            }
        }
        
        stage('Get Weather Data') {
            steps {
                script {
                    // Run the weather script
                    sh '''
                        . venv/bin/activate
                        python get_philly_weather.py
                    '''
                }
            }
        }
        
        stage('Archive Report') {
            steps {
                // Archive the weather report as an artifact
                archiveArtifacts artifacts: 'weather_report.txt', fingerprint: true
            }
        }
    }
    
    post {
        always {
            // Clean up workspace
            cleanWs()
        }
        failure {
            // Send email on failure
            emailext (
                subject: "Pipeline Failed: Philadelphia Weather Report",
                body: "The weather reporting pipeline has failed. Please check the Jenkins logs.",
                recipientProviders: [[$class: 'DevelopersRecipientProvider']]
            )
        }
    }
} 