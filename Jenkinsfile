pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'source venv/bin/activate'
		sh 'echo "checking python version"'
                sh 'python3 --version'
            }
        }
    }
}
