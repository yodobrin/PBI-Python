# PBI-Python
This repository, will walk you through the steps required to create a web application, exposing (or publishing) power BI reports, to mass amount of users without 'Pro' users license. This is a common use case for health organization, public transportation, finance etc. The solution outlines the architecture, the Azure assets requirment, and it will guide you, on how to secure your application.
Power BI Embedded using python. This project is forked from [Samples](https://github.com/Microsoft/PowerBI-Developer-Samples), focusing on the Python flavor.

## Use Case
Your organization collected data, or is aiming to collect. You have a great reporting team, they produce amayzing reports from the collected data, these reports can help other achieve thier goals, save lives, help plan for traffic jams, or any other target. But you have only few 'Pro' licenses, and you dont aim on creating a premium account just yet. With power BI embedded, you can publish the reports to a large community. But, you dont just want anyone to access, you have restrictions requirments, have it regulation or a business decsion.

## Implementation Steps
In order to build your own application, follow these high level guidlines:
+ clone this repo to your local machine
+ Obtain required parameters for your Power BI report
+ Create Service Principal
+ Allow the principal to leverage the embeded capacity
+ Deploy your application to Azure
+ Add authentication to the application
+ Add WAF
+ Invite users to your application
 
## Solution Architecture

![Architecture](https://user-images.githubusercontent.com/37622785/81040881-0c9c0e00-8eb5-11ea-9b48-6cae552efd74.png)

#### Data Repositories
+ Please review the [rich set of datasources](https://docs.microsoft.com/en-us/power-bi/desktop-data-sources#data-sources) that Power BI can connect to.
+ You can connect to on-premises datasources using the [On-Premises Data Gateway](https://docs.microsoft.com/en-us/power-bi/service-gateway-onprem-indepth). 

#### Power BI Embedded Capacity
You will need a dedicated compute resource to render and display your reports. A capacity is attached to a Power BI workspace and can be either a [Power BI Premium](https://docs.microsoft.com/en-us/power-bi/service-premium-what-is#dedicated-capacities) or [Embedded Analytics](https://azure.microsoft.com/en-us/services/power-bi-embedded/) Capacity. 
You can review the differences between the two in this [detailed whitepaper](https://go.microsoft.com/fwlink/?linkid=2057861).

You can plan your deployment size using the [assessment tool](https://docs.microsoft.com/en-us/power-bi/developer/embedded/embedded-capacity-planning) and use these performance best pratices documents for tuning your deployment: [PBI reports](https://docs.microsoft.com/en-us/power-bi/guidance/power-bi-optimization), [PBI Embedded](https://docs.microsoft.com/en-us/power-bi/developer/embedded/embedded-performance-best-practices).
.

#### Web App
[Web app](https://docs.microsoft.com/en-us/azure/app-service/overview), common PaaS solution, allowing developers to host thier code in a quick manner, it let the developr focus on the application, rather than anything else.
Web app can host application written in multiple languages. In this example we are using a Python based application. If this is your first time using one, We suggest you follow a [tutorial](https://docs.microsoft.com/en-us/azure/app-service/containers/quickstart-python?tabs=bash) to get familar with the concepts.
 
#### Key Vault
**Never** write your secrets in your code. Having your secrets in the web app configuration is your minimal secured posture. The recoemnded method to store secrets is using a [Key Vault](https://docs.microsoft.com/en-us/azure/key-vault/general/overview).
As this is simple demo app, we are not using it, rather keeping the secrets in the web app configuration. 


*__Note:__ there are few options to leverage the values stored in the key vault, either via ``` App Configuration ``` and associated it to the KeyVault see [tutorial](https://docs.microsoft.com/en-us/azure/azure-app-configuration/use-key-vault-references-dotnet-core?tabs=cmd%2Ccore2x), you will also need to alter the code, and stop using ```os.environ.get``` and follow this [quick start](https://docs.microsoft.com/en-us/azure/key-vault/secrets/quick-create-python). Another alternative is by using [Azure DevOps](https://docs.microsoft.com/en-us/azure/devops/user-guide/what-is-azure-devops?view=azure-devops).*

#### Identity Provider (Azure Active Directory)
While this repository is focused on AAD, there are multiple identity providers, that are already pre-integrated to Azure web application [see documentation](https://docs.microsoft.com/en-us/azure/app-service/overview-authentication-authorization). In case these means are not sufficent, one can create other ways to authentication and authorize. There are few (at the time this repository was created) limitation in Azure Web App deployment, that might require you to leverage docker deployment, more details later in this document.

#### WAF
This module is in place to allow enhanced security posture, regadless of your data classification, we rather our web site remains safe. WAF provides basic security measures against the common attacks. The Web Application Firewall domain has many vendors, we will be using the [Azure WAF V2](https://docs.microsoft.com/en-us/azure/web-application-firewall/ag/ag-overview)

### Deployment Options
Follow our [Best Practices](https://docs.microsoft.com/en-us/azure/app-service/deploy-best-practices) for deployment. In this repo we used the straightforward deployment from visual studio code.

#### VIsual Studio Code
Once cloned to your local machine, navigate to the created folder and type ```code .``` 
Examine this [tutorial](https://docs.microsoft.com/en-us/azure/javascript/tutorial-vscode-azure-app-service-node-01?tabs=bash) demonstrate the steps for deployment, even though it uses Node.js code, the deployment steps are similar.
you will need to create/update ``` .env ``` file with the following parameters:

```
# Either 'MasterUser' or 'ServicePrincipal' - default is set to ServicePrincipal
AUTHENTICATION_MODE=""
WORKSPACE_ID=""
REPORT_ID=""
TENANT_ID=""
CLIENT_ID=""
# Required only for 'ServicePrincipal' authentication mode
CLIENT_SECRET=""
# Required only for 'MasterUser' authentication mode
POWER_BI_USER=""
POWER_BI_PASS=""
```
Follow steps describes in the following sections on how to obtain these values.


#### Docker deployment
In few cases, where your requirments file contain packages, which cannot be loaded correctly by the app service, you will need to deploy your code as Docker container.
This repo, does not cover how to do so, as there are multiple blogs and tutorials which explains this area. Here is one [example](https://docs.microsoft.com/en-us/azure/javascript/tutorial-vscode-docker-node-01?tabs=bash).

### Active Directory setup
It is recoemnded to utilize Service Principal, as users might move from an organization, their authorization altered etc. In this repository, we cover the steps required to create and enable a service principal access to embedded capacity.
The following [guide](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal) contains step by step instructions on how to create a service principal.

### Power BI - One time setup
There are two options to consume PBI embedded capacity, see [license types](https://docs.microsoft.com/en-us/power-bi/service-features-license-type) for more details.
+ Dedicated 'Pro' user
+ Service Principal - You need a user with [Power BI Admin and Power Platform Admin](https://docs.microsoft.com/en-us/power-bi/service-admin-role#assign-users-to-an-admin-role-in-the-microsoft-365-admin-center) roles in the AAD in order to allow [Service Prinicpal Embedding](https://docs.microsoft.com/en-us/power-bi/developer/embedded/embed-service-principal#step-3---enable-the-power-bi-service-admin-settings).

The MasterAccount user or Service Principal do not automatically have permissions on all your PBI assets and therefore you will need to grant them access to Power BI workspaces where the reports you're going to embed reside.

#### Associate Embedded Capacity
This [document](https://docs.microsoft.com/en-us/power-bi/developer/embedded/embed-service-principal) provide detailed instructions to the entire process, from creating the service principal to associate it to your public Power BI workspace.

Lastly, to wrap it all up - see this [tutorial](https://docs.microsoft.com/en-us/power-bi/developer/embedded/embed-sample-for-customers#embed-content-using-the-sample-application) for associating the capacity.


### WAF setup
Follow this [quick start](https://docs.microsoft.com/en-us/azure/web-application-firewall/ag/application-gateway-web-application-firewall-portal) to deploy a WAF V2.

*__Note:__ when configuring the ```http``` setting toggle the ```Override with new host name``` to **Yes***



