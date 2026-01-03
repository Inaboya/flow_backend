-1 Running on Docker
# From the project root
docker-compose up --build

-2 NestJS API Setup (Data Orchestration)
Follow these steps to initialize the primary backend and database schema:

# Navigate to the nest-api directory
cd apps/nest-api

# Setup environment variables
cp .env.example .env # Ensure DATABASE_URL is set in this file

# Install dependencies
yarn install

# Synchronize Drizzle schema with PostgreSQL
npx drizzle-kit push

# Populate the database with heuristic test data
yarn seed

# Start the NestJS development server
yarn start:dev

-3 Python Engine Setup (Heuristic Scoring)
The scoring engine is responsible for the algorithmic comparison of data. Use the following steps to prepare the environment:

# Navigate to the python-engine directory
cd apps/python-engine

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate 
# On Windows: 
.\venv\Scripts\activate

# Install dependencies for SQLAlchemy 2.0 and Strawberry GraphQL
pip install -r requirements.txt

# Launch the FastAPI service
python -m src.main