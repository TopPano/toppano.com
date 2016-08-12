node ('master') {
   stage 'Checkout'
   echo 'Checkout'
   // Get some code from a GitHub repository
   git url: 'git@github.com:uniray7/verpix.me.git', credentialsId:'verpix-me-cred'

   stage 'Integration Test'
   echo 'Integration test'
   docker.withServer('tcp://dockerd:4243') {
      sh 'docker-compose up verpix-dev-webui-mongodb &'
      sh 'sh integration_test.sh'
      sh 'docker-compose stop'
      sh 'docker-compose rm -f'
   }
}

