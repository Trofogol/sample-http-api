pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                // since working directory is cloned repository's folder,
                // I use local path:
                // create virtual environment 'venv' in repo directory
                sh 'python3 -m venv venv'
                sh 'ls -lh'  // kind of debug
                // activate it
                sh 'source venv/bin/activate'
                // and install necessary modules
                sh 'pip3 install flask pymysql cryptography pyyaml'
            }
        }
    }
}
