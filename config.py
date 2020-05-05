#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------
import os

class BaseConfig(object):
 # Can be set to 'MasterUser' or 'ServicePrincipal' - default is set to ServicePrincipal
 AUTHENTICATION_MODE = os.getenv('AUTHENTICATION_MODE','ServicePrincipal')

 # Workspace Id for which Embed token needs to be generated
 WORKSPACE_ID = os.environ.get('WORKSPACE_ID')
 
 # Report Id for which Embed token needs to be generated
 REPORT_ID = os.environ.get('REPORT_ID')
 
 # Id of the Azure tenant in which AAD app is hosted
 TENANT_ID = os.environ.get('TENANT_ID')
 
 # Client Id (Application Id) of the AAD app
 CLIENT_ID = os.environ.get('CLIENT_ID')
 
 # Client Secret (App Secret) of the AAD app. Required only for ServicePrincipal authentication mode.
 CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
 
 # Scope of AAD app. Use the below configuration to use all the permissions provided in the AAD app through Azure portal.
 SCOPE = ['https://analysis.windows.net/powerbi/api/.default']
 
 # URL used for initiating authorization request
 AUTHORITY = 'https://login.microsoftonline.com/' + TENANT_ID
 
 # Master user email address. Required only for MasterUser authentication mode
 POWER_BI_USER = os.environ.get('POWER_BI_USER')
 
 # Master user email password. Required only for MasterUser authentication mode
 POWER_BI_PASS = os.environ.get('POWER_BI_PASS')