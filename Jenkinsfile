pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "pavankumar1605/devops-project-workspace"
        DOCKER_TAG = "v1"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/dpavankumar29/DevOps-Project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // ✅ Building from workspace folder
                    docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}", "workspace")
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: '5c8551d3-d619-4f23-b9a4-df28138660a4',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    bat """
                        echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin
                    """
                }
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                bat "docker push ${DOCKER_IMAGE}:${DOCKER_TAG}"
            }
        }
    }

    post {
        always {
            bat 'docker logout'
        }
    }
}
