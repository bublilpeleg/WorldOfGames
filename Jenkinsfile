pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('peleg-docker-hub')
//         dockerImage=''
//         registry = 'pelegb999/world_of_games'
        }
    stages {
        stage('checkout_repo') {
            steps {
                git branch: 'main', url: 'https://github.com/bublilpeleg/WorldOfGames.git'
            }
        }
        stage('build docker-compose') {
            steps {
                sh 'docker-compose build'
            }
        }
        stage ('dummy score.txt') {
            steps {
                sh 'echo 50 > Scores.txt'
            }
        }
        stage('run docker-compose') {
            steps {
                sh 'docker-compose up -d'
            }
        }
        stage('run test python script ') {
            steps {
                sh 'ls'
            }
        }
        stage('terminate and push') {
            steps {
                sh 'docker-compose down'
            }
        }
        stage('Login') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }
        stage('Push') {
            steps {
                sh 'docker tag worldofgames pelegb999/worldofgames'
                sh 'docker push pelegb999/worldofgames:latest'
                sh 'docker logout'
            }
        }
    }
}