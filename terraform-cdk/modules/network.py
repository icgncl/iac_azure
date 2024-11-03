from constructs import Construct
from imports.azurerm import (
    virtual_network,
    subnet
)
from typing import List

class NetworkModule(Construct):
    def __init__(
        self, 
        scope: Construct, 
        id: str,
        name: str,
        resource_group_name: str,
        location: str,
        vnet_address_space: List[str],
        frontend_subnet_prefixes: List[str],
        backend_subnet_prefixes: List[str],
        environment: str
    ):
        super().__init__(scope, id)
        
        # Create Virtual Network
        self.vnet = virtual_network.VirtualNetwork(self, "vnet",
            name=name,
            resource_group_name=resource_group_name,
            location=location,
            address_space=vnet_address_space,
            tags={
                "managed_by": "terraform-cdk",
                "environment": environment
            }
        )

        # Create Frontend Subnet
        self.frontend_subnet = subnet.Subnet(self, "frontend",
            name="frontend-subnet",
            resource_group_name=resource_group_name,
            virtual_network_name=self.vnet.name,
            address_prefixes=frontend_subnet_prefixes
        )

        # Create Backend Subnet
        self.backend_subnet = subnet.Subnet(self, "backend",
            name="backend-subnet",
            resource_group_name=resource_group_name,
            virtual_network_name=self.vnet.name,
            address_prefixes=backend_subnet_prefixes
        )