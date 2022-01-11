pipeline {
  agent any
  stages {
    stage('versioncheck') {
      steps {
        bat(script: 'mvn -v', returnStatus: true, returnStdout: true)
      }
    }

  }
}