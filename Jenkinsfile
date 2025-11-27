pipeline {
    agent any

    environment {
        DOCKERHUB_USER = 'your_dockerhub_username'
        IMAGE_NAME     = "${DOCKERHUB_USER}/two-tier-flask-app"
        EC2_HOST       = 'ec2-user@YOUR_EC2_PUBLIC_IP'
        APP_DIR        = '/home/ec2-user/two-tier-flask-mysql-docker-jenkins'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build & Test') {
            steps {
                sh '''
                  cd app
                  python -m venv venv
                  . venv/bin/activate
                  pip install -r requirements.txt
                  # pytest || echo "No tests yet"
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$BUILD_NUMBER .'
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                      echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                      docker tag $IMAGE_NAME:$BUILD_NUMBER $IMAGE_NAME:latest
                      docker push $IMAGE_NAME:$BUILD_NUMBER
                      docker push $IMAGE_NAME:latest
                    '''
                }
            }
        }

        stage('Deploy to EC2') {
            steps {
                sshagent (credentials: ['ec2-ssh-key']) {
                    sh '''
                      ssh -o StrictHostKeyChecking=no $EC2_HOST "
                        if [ ! -d $APP_DIR ]; then
                          git clone https://github.com/YOUR_GITHUB_USERNAME/two-tier-flask-mysql-docker-jenkins.git $APP_DIR
                        else
                          cd $APP_DIR && git pull
                        fi
                        cd $APP_DIR
                        docker-compose pull
                        docker-compose up -d --build
                      "
                    '''
                }
            }
        }
    }
}
