from ninja import NinjaAPI
#from .v1 import router as v1_router
from .v1.endpoints import router as v1_router

# Initialize the API instances for each version
#api_v1 = NinjaAPI(version="1.0.0", title="API v1")
api_v1 = NinjaAPI()

# Add the routers to the API instances
api_v1.add_router("/", v1_router)

# Optionally, you can define common routes or global exception handlers here if needed
