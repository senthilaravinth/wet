pipeline {
    agent any

    environment {
        // Defining variables for easier management
        IMAGE_NAME = "factorial-app"
        DEPLOY_FILE = "deployment.yaml"
    }

    stages {
        // STAGE 1: Check if files actually exist in the root folder
        stage('Debug Workspace') {
            steps {
                echo "--- CURRENT WORKSPACE FILES ---"
                // This will print the list of files to the Jenkins console
                bat "dir" 
            }
        }

        // STAGE 2: Build the Docker image
        stage('Docker Build') {
            steps {
                echo "Starting Docker Build for %IMAGE_NAME%..."
                // The '.' tells Docker to look for the Dockerfile and app.py in the root
                bat "docker build -t %IMAGE_NAME%:latest ."
            }
        }

        // STAGE 3: Deploy to Kubernetes
        stage('Kubernetes Deploy') {
            steps {
                script {
                    echo "Applying Kubernetes Manifest: %DEPLOY_FILE%"
                    // Applies the deployment.yaml located in the root folder
                    bat "kubectl apply -f %DEPLOY_FILE%"
                    
                    // Force a restart to ensure the pod uses the latest build
                    bat "kubectl rollout restart deployment/factorial-app"
                }
            }
        }

        // STAGE 4: Verification
        stage('Verify K8s Status') {
            steps {
                echo "Checking Pod status..."
                bat "kubectl get pods"
                bat "kubectl get service factorial-service --ignore-not-found"
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed. Please check the 'Debug Workspace' stage output to see if app.py was missing."
        }
    }
}