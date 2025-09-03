pipeline {
    agent any
    environment {
        VENV_DIR = 'venv'
        GCP_PROJECT = 'steam-glass-467515-t4'
        GCLOUD_PATH = '/var/jenkins_home/google-cloud-sdk/bin'
        KUBECTL_AUTH_PLUGIN = '/usr/lib/google-cloud-sdk/bin'
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

        stage("DVC pull...."){
            steps{
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]){
                    script{
                        echo 'DVC pull.....'
                        sh'''
                        . ${VENV_DIR}/bin/activate
                        dvc pull
                        '''
                    }
                }
            }
        }

        stage("Build and push image to GCR...."){
            steps{
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]){
                    script{
                        echo 'Build and push image to GCR....'
                        sh'''
                        export PATH=$PATH:${GCLOUD_PATH}
                        gcloud auth activate-service-account --key-files=${GOOGLE_APPLICATION_CREDENTIALS}
                        gcloud config set project ${GCP_PROJECT}
                        gcloud auth configure-docker --quit
                        docker built -t gcr.io/${GCP_PROJECT}/ml-anime:latest .
                        docker push gcr.io/${GCP_PROJECT}/ml-anime:latest
                        '''
                    }
                }
            }
        }

        stage("Deploy to kubernaties...."){
            steps{
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]){
                    script{
                        echo 'Deploy to kubernaties....'
                        sh'''
                        export PATH=$PATH:${GCLOUD_PATH}:${KUBECTL_AUTH_PLUGIN}
                        gcloud auth activate-service-account --key-files=${GOOGLE_APPLICATION_CREDENTIALS}
                        gcloud config set project ${GCP_PROJECT}
                        gcloud container clusters get-credentials ml-app-cluster --region us-central1
                        kubectl apply -f deployment.yaml
                        '''
                    }
                }
            }
        }
    }
}