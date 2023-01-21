# Change these four parameters as needed
$ACI_PERS_RESOURCE_GROUP="bikesharing"
$ACI_PERS_STORAGE_ACCOUNT_NAME="bikestorageaccount$RANDOM"
$ACI_PERS_LOCATION="eastus"
$ACI_PERS_SHARE_NAME="bikeshare"

# Create the storage account with the parameters
az storage account create --resource-group $ACI_PERS_RESOURCE_GROUP --name $ACI_PERS_STORAGE_ACCOUNT_NAME --location $ACI_PERS_LOCATION --sku Standard_LRS

# Create the file share
az storage share create --name $ACI_PERS_SHARE_NAME --account-name $ACI_PERS_STORAGE_ACCOUNT_NAME

echo $ACI_PERS_STORAGE_ACCOUNT_NAME