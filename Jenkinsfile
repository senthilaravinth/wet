pipeline {
    agent any

    environment {
        IMAGE_NAME = "logic-app"
        DEPLOY_FILE = "deployment.yaml" // Points to root folder
    }

    stages {
        stage('Docker Build') {
            steps {
                bat "docker build -t %IMAGE_NAME%:latest ."
            }
        }

        stage('Kubernetes Deploy') {
            steps {
                script {
                    // Since deployment.yaml is in the root, we use the filename directly
                    bat "kubectl apply -f %DEPLOY_FILE%"
                    
                    // Force refresh to use the newly built image
                    bat "kubectl rollout restart deployment/logic-deployment"
                }
            }
        }

        stage('Verification') {
            steps {
                script {
                    // List pods to confirm deployment
                    bat "kubectl get pods"
                    
                    // Show logs of the deployment to see the factorial result
                    bat "kubectl logs deployment/logic-deployment"
                }
            }
        }
    }

    post {
        success {
            echo "Successfully deployed using %DEPLOY_FILE% from root!"
        }
    }
}