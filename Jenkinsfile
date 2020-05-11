pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                // since working directory is cloned repository's folder,
                // I use local path:
                // set virtual environment
                sh '''
                      if [ ! -d venv ]
                      then
                              python3 -m venv venv
                      fi
                      . venv/bin/activate
                      python3 -m pip install -r requirements.txt
                   '''
            }
        }
        stage('unit tests') {
            steps {
                sh '''
                      . venv/bin/activate
                      python3 sample_unittest.py
                   '''
            }
        }
    }
}
