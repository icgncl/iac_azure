from dataclasses import dataclass, field
from typing import List

@dataclass
class Variables:
    location: str = "westeurope"
    environment: str = "dev"
    vnet_address_space: List[str] = field(default_factory=lambda: ["10.0.0.0/16"])
    frontend_subnet_prefixes: List[str] = field(default_factory=lambda: ["10.0.1.0/24"])
    backend_subnet_prefixes: List[str] = field(default_factory=lambda: ["10.0.2.0/24"]) 