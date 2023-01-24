# Deployment
Before starting any containers, you want to make sure everything is configured correctely. This involves database, mail and security configuration. If you use Docker Compose create the following three files:

**database.conf**
```
POSTGRES_USER=admin
POSTGRES_PASSWORD=example
POSTGRES_HOST=database
POSTGRES_PORT=5432
POSTGRES_DB=postgres

```
**mail.conf**
```
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=true
MAIL_USERNAME=noreply.bikerental@gmail.com
MAIL_PASSWORD=rwfigoblrwefirkb
SECURITY_EMAIL_SENDER=noreply.bikerental@gmail.com

```
**security.conf**
```
SECRET_KEY=pf9Wkove4IKEAXvy-cQkeDPhv9Cb3Ag-wyJILbq_dFw
SECURITY_PASSWORD_SALT=146585145368132386173505678016728509634
```
Docker Compose will create environment variables containing these values. Alternatively you can create environment variables as you want. Note that the webapp container needs access to all environment variables, the database container only to the ones listet in database.conf. 

Change the default admin password after setting up. 

## Local
Deploying this software architecture locally involves several steps that use Docker and Docker Compose:

1. Install Docker: Install Docker on your local machine. This is required to run the Docker containers for your application and its dependencies.
1. Install Docker Compose: Install Docker Compose on your local machine. This is used to manage the relationships between the services in your application.
1. Clone the Repository: Clone the repository containing the code for your application, the docker-compose.yml file, and the env_files.
1. Build the Images: In the root directory of your cloned repository, use the command `docker-compose build` to build the images for the webapp, database and adminer services.
1. Start the Services: In the root directory of your cloned repository, use the command `docker-compose up` to start the services defined in the docker-compose.yml.
1. Verify the Deployment: Verify that your application is running by visiting http://localhost in your web browser. The adminer service is available at http://localhost:8080.
1. Stop the Services: To stop the services use the command `docker-compose down`. 

Please note that the above steps are just an example and the commands may differ depending on the specific configurations.

It's important to also consider security, monitoring and scaling when deploying locally, you should also create a backup strategy for the data in the database and implement monitoring and logging to ensure that the system is running smoothly.

## AWS
Deploying this software architecture to the cloud involves several steps, which can vary depending on the cloud provider you are using. Here is an example of how to deploy this architecture to AWS using Elastic Container Service (ECS):

1. Create an ECS cluster: Log in to the AWS Management Console and create a new ECS cluster. This is where your Docker containers will be deployed.
1. Create a task definition: In the ECS dashboard, create a new task definition for your application. This defines the container images and configurations for the webapp, database, and adminer services. You can use the configuration from your docker-compose.yml file as a reference.
1. Create a service: In the ECS dashboard, create a new service for your task definition. This will create a new task for each service and will ensure that the task is running and healthy.
1. Create a load balancer: Create a new Application Load Balancer and configure it to route traffic to your webapp service. This will ensure that traffic is distributed evenly across all tasks running in your service.
1. Create a RDS: Create a new RDS instance and configure it to use the same configurations as your task definition for the database service.
1. Create a volume: Create a new Elastic Block Store (EBS) volume and configure it to use the same configurations as your task definition for the postgres_volume.
1. Create a security group: Create a new security group and configure it to allow traffic to the ports used by your services.
1. Update the env_file: Update the env_file with the RDS endpoint and security group.
1. Deploy your application: Use the ECS console to deploy your application. This will create new tasks for your services, start the tasks, and register them with the load balancer.
1. Verify the deployment: Verify that your application is running and accessible by visiting the load balancer endpoint.

Please note that this is just an example and the steps may differ depending on the cloud provider and specific configurations. It's also worth noting that some cloud providers have a managed service for the ECS and RDS, which can simplify the process and provide additional features.

It's important to also consider security, monitoring, and scaling when deploying to the cloud. You should also create a backup strategy for the data in the RDS, and implement monitoring and logging to ensure that the system is running smoothly.

## Azure
Deploying this software architecture to Azure involves several steps, which can vary depending on the specific configuration. Here is an example of how to deploy this architecture to Azure using Azure Container Service (AKS) and Azure Database for PostgreSQL:

1. Create a new AKS cluster: Log in to the Azure portal and create a new AKS cluster. This is where your Docker containers will be deployed.
1. Create a new Azure Database for PostgreSQL: In the Azure portal, create a new Azure Database for PostgreSQL. This will be used as the backend for the database service.
1. Create a new Azure Container Registry (ACR): In the Azure portal, create a new ACR. This will be used to store the container images for your application.
1. Push container images to the ACR: Using the `docker push` command, push the container images for the webapp, database and adminer services to the ACR.
1. Create a Kubernetes deployment and service: Use kubectl or Azure CLI to create a new deployment and service for the webapp and adminer services. This will create new pods for each service and will ensure that the pods are running and healthy.
1. Create a secret for the env_file: Use kubectl or Azure CLI to create a new secret for the env_file and provide the connection strings and credentials for the Azure Database for PostgreSQL.
1. Create an Azure Load Balancer: Create a new Azure Load Balancer and configure it to route traffic to the webapp service. This will ensure that traffic is distributed evenly across all pods running in the service.
1. Update the env_file: Update the env_file with the Azure Database for PostgreSQL endpoint and credentials.
1. Scale the deployment: Use the AKS dashboard to scale the deployment as needed.
1. Verify the deployment: Verify that your application is running and accessible by visiting the load balancer endpoint.

Please note that this is just an example and the steps may differ depending on the specific configurations. It's also worth noting that AKS provides a managed Kubernetes service which can simplify the process and provide additional features.

It's important to also consider security, monitoring, and scaling when deploying to azure. You should also create a backup strategy for the data in the Azure Database for PostgreSQL, and implement monitoring and logging to ensure that the system is running smoothly.
