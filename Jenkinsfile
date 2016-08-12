node ('master') {
   stage 'Checkout'
   echo 'Checkout'
   // Get some code from a GitHub repository
   git url: 'git@github.com:uniray7/verpix.me.git', credentialsId:'verpix-me-cred'

   stage 'Integration Test'
   echo 'Integration test'
   docker.withServer('tcp://dockerd:4243') {
      sh 'docker-compose create verpix-dev-webui-mongodb'
      sh 'docker-compose start verpix-dev-webui-mongodb'
      sh 'integration_test.sh'
      sh 'docker-compose stop verpix-dev-webui-mongodb'
      sh 'docker-compose rm verpix-dev-webui-mongodb'
   }
}
