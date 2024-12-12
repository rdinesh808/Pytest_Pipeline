pipeline {
    agent any

    environment {
        PROJECT_FOLDER = "D:/PythonPyTest"
        REQUIREMENTS_FILE = "requirements.txt"
        REPORT_FILE = "report.html"
    }

    stages {
        stage('Clone Repository') {
            steps {
                script {
                    bat """
                    if not exist "%PROJECT_FOLDER%" (
                        mkdir "%PROJECT_FOLDER%"
                    )
                    """
                    dir("${PROJECT_FOLDER}") {
                        git branch: 'master', url: 'https://github.com/rdinesh808/Pytest_Pipeline.git'
                    }
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    dir("${PROJECT_FOLDER}") {
                        bat "pip install -r ${REQUIREMENTS_FILE}"
                    }
                }
            }
        }

        stage('Run Pytest and Generate Report') {
            steps {
                script {
                    dir("${PROJECT_FOLDER}") {
                        bat "pytest -x -v -s --html=${REPORT_FILE} --self-contained-html"
                    }
                }
            }
        }

        stage('Archive HTML Report') {
            steps {
                script {
                    dir("${PROJECT_FOLDER}") {
                        archiveArtifacts artifacts: "${REPORT_FILE}", allowEmptyArchive: false
                    }
                }
            }
        }
    }

    post {
        success {
            echo "Pipeline executed successfully."
        }
        failure {
            echo "Pipeline execution failed."
        }
        always {
            cleanWs()
        }
    }
}
