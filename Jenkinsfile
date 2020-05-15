pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                // since working directory is cloned repository's folder,
                // I use local path:
                // set virtual environment and remove previous (if any)
                sh '''
                      if [ -d venv ]
                      then
                              rm -r venv
                      fi
                      python3 -m venv venv
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
        // here (after build and tests) might be 'packaging' stage: form package for deploy
        // I don't think that this project can be effectively deployed
        // by this way
    }
}
