import pdb

from models.country import Country
from models.festival import Festival
from models.user import User

import repositories.country_repository as country_repository
import repositories.festival_repository as festival_repository
import repositories.user_repository as user_repository

# country_repository.delete_all()
# festival_repository.delete_all()
# user_repository.delete_all()

country_1 = Country("Serbia", "RS")
country_repository.save(country_1)