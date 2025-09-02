pipeline {
    agent any
    environment {
        VENV_DIR = 'venv'
    }
    stages{

        stage("Cloning from github...."){
            steps{
                script{
                    echo 'Cloning from github....'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/yasiruLakruwan/Hybrid-anime-recommender-system.git']])
                }
            }
        }

        stage("Creating virtual environment...."){
            steps{
                script{
                    echo 'Creating virtual environment....'
                    sh'''
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    pip install dvc
                    '''
                }
            }
        }

        
    }
}