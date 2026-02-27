pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "pavankumar1605/devops-project-workspace"
        DOCKER_TAG = "v1"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/dpavankumar29/DevOps-Project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}")
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh """
                        echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                    """
                }
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                script {
                    sh "docker push ${DOCKER_IMAGE}:${DOCKER_TAG}"
                }
            }
        }
    }

    post {
        always {
            sh 'docker logout'
        }
    }
}
