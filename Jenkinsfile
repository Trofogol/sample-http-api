pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                // since working directory is cloned repository's folder,
                // I use local path:
                // set virtual environment
                sh '''if [ ! -d "venv"] 
                      then
                      python3 -m venv venv
                      fi
                      . venv/bin/activate
                      pip3 install flask pymysql cryptography pyyaml
                   '''
            }
        }
    }
}
