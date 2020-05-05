# PBI-Python
This repository, will walk you through the steps required to create a web application, exposing (or publishing) power BI reports, to mass amount of users without 'Pro' users license. This is a common use case for health organization, public transportation, finance etc. The solution outlines the architecture, the Azure assets requirment, and it will guide you, on how to secure your application.
Power BI Embedded using python. This project is forked from [Samples](https://github.com/Microsoft/PowerBI-Developer-Samples), focusing on the Python flavor.

## Use Case
Your organization collected data, or is aiming to collect. You have a great reporting team, they produce amayzing reports from the collected data, these reports can help other achieve thier goals, save lives, help plan for traffic jams, or any other target. But you have only few 'Pro' licenses, and you dont aim on creating a premium account just yet. With power BI embedded, you can publish the reports to a large community. But, you dont just want anyone to access, you have restrictions requirments, have it regulation or a business decsion.

## Solution Architecture

![Architecture](https://user-images.githubusercontent.com/37622785/81040881-0c9c0e00-8eb5-11ea-9b48-6cae552efd74.png)

### Solution Componenets
+ Documentation overview for each component

#### Data Repositories
+ Documnetation for PBI connectors
+ Documentation for connecting using the ENT Data GW

#### Power BI embedded capacity

#### Web App

#### Key Vault

#### Identity Provider (Azure Active Directory)
While this repository is focused on AAD, there are multiple identity providers, that are already pre-integrated to Azure web application [see documentation](https://docs.microsoft.com/en-us/azure/app-service/overview-authentication-authorization). In case these means are not sufficent, one can create other ways to authentication and authorize. There are few (at the time this repository was created) limitation in Azure Web App deployment, that might require you to leverage docker deployment, more details later in this document.
#### WAF
This module is in place to allow enhanced security posture, regadless of your data classification, we rather our web site remain safe. WAF provide basic security measures against the common attacks.
#### Optional - On prem / other clouds - Data Repositories

### Deployment Options

#### VIsual Studio Code

#### Docker deployment

### Active Directory setup
PAVELA: required role for assignment (tennat, spn, roles)

### Power BI - One time setup
admin settings
#### Associate Embedded Capacity

### WAF setup
http/s
access restriction for web apps

