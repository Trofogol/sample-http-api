pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                // since working directory is cloned repository's folder,
                // I use local path:
                // create virtual environment 'venv' in repo directory
                python3 -m venv venv
                // activate it
                source venv/bin/activate
                // and install necessary modules
                pip3 install flask pymysql cryptography pyyaml
            }
        }
    }
}
