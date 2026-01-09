import os

# ===============================
# Flask Configuration
# ===============================
FLASK_SECRET_KEY = os.getenv(
    "FLASK_SECRET_KEY",
    "dev-secret-key-change-this"
)

# ===============================
# Supabase Configuration
# ===============================
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Fail fast if Supabase is not configured
if not SUPABASE_URL or not SUPABASE_KEY:
    raise RuntimeError(
        "Supabase credentials not found. "
        "Please set SUPABASE_URL and SUPABASE_KEY as environment variables."
    )

# ===============================
# RapidAPI Configuration (Movies)
# ===============================
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_HOST = os.getenv("RAPIDAPI_HOST")

# ===============================
# Environment Info
# ===============================
ENVIRONMENT = os.getenv("ENVIRONMENT", "production")
DEBUG = ENVIRONMENT == "development"
