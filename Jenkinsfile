pipeline {
    agent any

    environment {
        DOCKERHUB_USER = 'vishnurupi'
    }

    stages {

        stage('Build Docker Image') {
            steps {
                script {
                    bat """
                    docker build -t ${DOCKERHUB_USER}/devkart:latest .
                    """
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                        bat """
                        echo %PASS% | docker login -u %USER% --password-stdin
                        docker push %USER%/devkart:latest
                        """
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat "kubectl apply -f deployment.yaml --validate=false"
                bat "kubectl apply -f service.yaml --validate=false"

            }
        }
    }
}
