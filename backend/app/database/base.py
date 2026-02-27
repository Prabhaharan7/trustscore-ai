# Import all the models, so that Base has them before being
# imported by Alembic or for database creation logic

from app.database.db import Base

# Model imports
from app.models.user import User
from app.models.assessment import Assessment
from app.models.attempt import Attempt
from app.models.behavior_log import BehaviorLog
from app.models.skill_analytics import SkillAnalytics
