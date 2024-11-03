#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack
from imports.azurerm import (
    provider,
    resource_group
)
from variables import Variables
from modules.network import NetworkModule

class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)
        
        vars = Variables()

        # Configure Azure Provider
        provider.AzurermProvider(self, "Azure",
            features={}
        )

        # Create Resource Group
        rg = resource_group.ResourceGroup(self, "rg",
            name=f"{vars.environment}-rg",
            location=vars.location,
            tags={
                "managed_by": "terraform-cdk"
            }
        )

        # Create Network using Module
        network = NetworkModule(self, "network",
            name="terraform-vnet",
            resource_group_name=rg.name,
            location=vars.location,
            vnet_address_space=vars.vnet_address_space,
            frontend_subnet_prefixes=vars.frontend_subnet_prefixes,
            backend_subnet_prefixes=vars.backend_subnet_prefixes,
            environment=vars.environment
        )

    

app = App()
MyStack(app, "terraform-cdk")
app.synth()