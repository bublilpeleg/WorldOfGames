pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('pelegb999-dockerhub')
        }
    stages {
        stage('checkout_repo') {
            steps {
                git branch: 'main', url: 'https://github.com/bublilpeleg/WorldOfGames.git'
            }
        }
        stage('build docker image') {
            steps {
                sh 'docker build -t world_of_games /app .'
            }
        }
        stage ('dummy score.txt') {
            steps {
                sh 'echo 50 > Scores.txt'
            }
        }
        stage('run & expose docker image') {
            steps {
                sh 'docker run -p 8777:5000 world_of_games'
            }
        }
        stage('run test python script ') {
            steps {
                sh 'python3.8 e2e.py'
            }
        }
        stage('terminate and push') {
            steps {
                sh 'docker rm -f world_of_games'
            }
        }
        stage('Login') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }
        stage('Push') {
            steps {
                sh 'docker push pelegb999/world_of_games:latest'
                sh 'docker logout'
            }
        }
    }
}