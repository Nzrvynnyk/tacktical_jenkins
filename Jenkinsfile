 pipeline {
    agent { label 'main' }
    environment {
        API_KEY_RMM = credentials('API_KEY_RMM')
    }
    stages {
        stage('Build') {
            steps {
                sh('docker run -it -d --name rmminstall-${BUILD_NUMBER} rmminstall')
                sh '''
                    docker exec -i rmminstall-${BUILD_NUMBER} python scriptrun.py $User $API_KEY_RMM $SCRIPT_ID $SOFTNAME $ARGS1 $ARGS2
                '''
            }
        }
    }
        post {
        always {
            sh '''
              docker rm rmminstall-${BUILD_NUMBER} -f
            '''
        }
    }
}
