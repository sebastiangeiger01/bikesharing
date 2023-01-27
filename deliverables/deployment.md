# Deployment
Before starting any containers, you want to make sure everything is configured correctely. This involves database, mail and security configuration. Configure following files from our repository:

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

For more details for the environment variables and their function read [here](/deliverables/doc.md/#databaseconf). 

**IMPORTANT: For a safe public deployment, change the default admin password after setting up. The ```SECRET_KEY``` and ```SECURITY_PASSWORD_SALT``` must be changed before deployment as well.**

## Local
Deploying the software locally can be helpful for development and involves several steps that use Docker and Docker Compose.:

1. Install Docker: Install Docker on your local machine. This is required to run the Docker containers for your application and its dependencies. Alternatively, install Docker Desktop under https://www.docker.com/products/docker-desktop/ and go to step 3.
1. Install Docker Compose: Install Docker Compose on your local machine. This is used to manage the relationships between the services in your application.
1. Clone the Repository: Clone the repository containing the code for your application, the docker-compose.yml file, and the env_files. The release branch is for full versions of the software, the master branch is for further development.
1. Build the Images: In the root directory of your cloned repository, use the command `docker-compose build` to build the images for the webapp, database and adminer services.
1. Start the Services: In the root directory of your cloned repository, use the command `docker-compose up` to start the services defined in the docker-compose.yml.
1. Verify the Deployment: Verify that your application is running by visiting http://localhost in your web browser. The adminer service is available at http://localhost:8080.
1. Stop the Services: To stop the services use the command `docker-compose down`. 

Please note that the above steps are just an example and the commands may differ depending on the specific configurations.

## Public deployment on Azure
For deployment into Azure, start with the `feature/AzureDeployment` branch.
The following steps are a summary of the following Microsoft Learn Articles: [Tutorial: Deploy a multi-container group using Docker Compose](https://learn.microsoft.com/en-us/azure/container-instances/tutorial-docker-compose) and [Mount an Azure file share in Azure Container Instances](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-volume-azure-files). Please read them for further information.

**Prerequisites: Azure account & (student) subscription as well as Azure CLI and Docker Desktop installed on your device.**

Deploying this software to Azure involves the following steps:

1. Create a new Azure File Share i.e. by using the following PowerShell script (You need an existing Resource Group for this to work, see step 3):
```sh
# Change these four parameters as needed
ACI_PERS_RESOURCE_GROUP=myResourceGroup
ACI_PERS_STORAGE_ACCOUNT_NAME=mystorageaccount$RANDOM
ACI_PERS_LOCATION=eastus
ACI_PERS_SHARE_NAME=acishare

# Create the storage account with the parameters
az storage account create \
    --resource-group $ACI_PERS_RESOURCE_GROUP \
    --name $ACI_PERS_STORAGE_ACCOUNT_NAME \
    --location $ACI_PERS_LOCATION \
    --sku Standard_LRS

# Create the file share
az storage share create \
  --name $ACI_PERS_SHARE_NAME \
  --account-name $ACI_PERS_STORAGE_ACCOUNT_NAME
```
2. Get the storage account key via the following command. You will need it for step 4.
```sh
STORAGE_KEY=$(az storage account keys list --resource-group $ACI_PERS_RESOURCE_GROUP --account-name $ACI_PERS_STORAGE_ACCOUNT_NAME --query "[0].value" --output tsv)
echo $STORAGE_KEY
```
3. Go to your share via the Azure Portal and create the directory `home/postgres` 
4. Configure the credentials in the `volume` settings in the `docker-compose.yaml`:
```
...
volumes:
  data:
    driver: azure_file
    driver_opts:
      share_name: [myResourceGroup]
      storage_account_name: [mystorageaccount$RANDOM]
      storage_account_key: [YOUR_STORAGE_KEY]
```
4. Create a new Azure Resource Group and container registry via the Azure CLI or the Azure Portal. This will be used to store the container images for your application. CLI usage example:
```sh
az group create --name myResourceGroup --location eastus
az acr create --resource-group myResourceGroup --name <acrName> --sku Basic
```
5. Log in to your container Registry
```sh
az acr login --name <acrName>
```
6. Configure the docker-compose.yaml file so that the webapp name points to your container registry
```
...
  webapp:
    image: <acrName>.azurecr.io/bike-sharing-webapp
...
```
7. Build the images with `docker-compose build` and push container images to the ACR using the `docker push` command.
1. To use Docker commands to run containers in Azure Container Instances, use `docker login azure` to login to Azure.
1. Create an ACI context by running `docker context create aci <myAciContext>`.
1. Select the new context via `docker context use <myAciContext>`
1. Start your container group via the `docker compose up` command. (Make sure to not insert a hyphen between docker and compose, since then the command would run locally. Insted, 'docker compose up' is a command implemented by the Azure CLI. Be aware that the Azure CLI for MacOS is currently not working correctly with ACI, so try to do this on a Windows machine if you experience that the webapp container does not start up).
1. Verify the deployment: Verify that your application is running and accessible by visiting the Azure Portal. You can see your service under "container insantces". In the overview you can see the IP adress the application is accessible from. To see wether all conainers are running and to access the logs, view the "container" tab unter settings.

You should now have a cloud-deployed version of BikeRental. See our version of the running software under 20.242.168.6.

**Please note that we are not security experts when it comes to cloud deployment. Further development will be needed to secure the application. We advice against using this deployment method for production without having the proper knowledge..**

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

Please note that the AWS deployment manual was not yet implemented by us, ist is just based on initial research done by us.
