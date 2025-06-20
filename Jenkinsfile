pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.9'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                script {
                    // Essayer différentes commandes Python selon l'OS
                    if (isUnix()) {
                        sh '''#!/bin/bash
                            # Essayer python3, puis python, puis installer si nécessaire
                            if command -v python3 >/dev/null 2>&1; then
                                PYTHON_CMD=python3
                            elif command -v python >/dev/null 2>&1; then
                                PYTHON_CMD=python
                            else
                                echo "Python non trouvé, installation nécessaire"
                                # Sur Ubuntu/Debian
                                if command -v apt-get >/dev/null 2>&1; then
                                    apt-get update
                                    apt-get install -y python3 python3-venv python3-pip
                                    PYTHON_CMD=python3
                                # Sur CentOS/RHEL
                                elif command -v yum >/dev/null 2>&1; then
                                    yum install -y python3 python3-pip
                                    PYTHON_CMD=python3
                                fi
                            fi

                            echo "Utilisation de: $PYTHON_CMD"
                            $PYTHON_CMD --version
                            $PYTHON_CMD -m venv venv
                            . venv/bin/activate
                            pip install --upgrade pip
                            pip install -r requirements.txt
                        '''
                    } else {
                        // Windows
                        bat '''
                            python --version
                            python -m venv venv
                            call venv\\Scripts\\activate.bat
                            pip install --upgrade pip
                            pip install -r requirements.txt
                        '''
                    }
                }
            }
        }

        stage('Lint Code') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''#!/bin/bash
                            . venv/bin/activate
                            pip install flake8
                            flake8 src tests --max-line-length=88 --exclude=venv || echo "Linting warnings found"
                        '''
                    } else {
                        bat '''
                            call venv\\Scripts\\activate.bat
                            pip install flake8
                            flake8 src tests --max-line-length=88 --exclude=venv || echo "Linting warnings found"
                        '''
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''#!/bin/bash
                            . venv/bin/activate
                            mkdir -p reports
                            python -m pytest --verbose --junit-xml=reports/junit.xml --cov=src --cov-report=html --cov-report=xml
                        '''
                    } else {
                        bat '''
                            call venv\\Scripts\\activate.bat
                            if not exist reports mkdir reports
                            python -m pytest --verbose --junit-xml=reports/junit.xml --cov=src --cov-report=html --cov-report=xml
                        '''
                    }
                }
            }
        }

        stage('Generate Reports') {
            steps {
                // Publication du rapport de couverture
                publishHTML([
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'htmlcov',
                    reportFiles: 'index.html',
                    reportName: 'Coverage Report'
                ])

                // Publication des résultats de tests
                publishTestResults(
                    testResultsPattern: 'reports/junit.xml'
                )
            }
        }
    }

    post {
        always {
            cleanWs()
        }
        failure {
            echo 'Build failed! Check the console output for details.'
            // Notification sans email
            script {
                currentBuild.result = 'FAILURE'
                echo "Build #${env.BUILD_NUMBER} failed"
            }
        }
        success {
            echo 'Build successful! All tests passed.'
            script {
                echo "Build #${env.BUILD_NUMBER} completed successfully"
            }
        }
    }
}
