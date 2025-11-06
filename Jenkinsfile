pipeline {
    agent any

    environment {
        DOCKERHUB_USER = 'vishnurupi'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/vishnuvardhandumma/devkart.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh '''
                    docker build -t ${DOCKERHUB_USER}/devkart:latest .
                    '''
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                        sh '''
                        echo $PASS | docker login -u $USER --password-stdin
                        docker push ${USER}/devkart:latest
                        '''
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
            }
        }
    }
}
