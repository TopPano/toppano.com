node ('master') {
   stage 'Checkout'
   echo 'Checkout'
   // Get some code from a GitHub repository
   git url: 'git@github.com:uniray7/verpix.me.git', credentialsId:'verpix-me-cred'

   stage 'Check'
   echo 'Check docker compose'

   docker.withServer('tcp://dockerd:4243') {
      sh 'docker-compose'

   }
}
