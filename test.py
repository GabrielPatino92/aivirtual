import numpy as np
print(f"numpy version: {np.__version__}") 

import pandas as pd
import os
print(f"pandas version: {pd.__version__}")  
# Ensure pandas is installed
try:
    import pandas as pd
except ImportError:
    os.system('pip install pandas')