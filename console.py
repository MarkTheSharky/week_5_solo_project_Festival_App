import pdb

from models.country import Country
from models.festival import Festival
from models.user import User

import repositories.country_repository as country_repository
import repositories.festival_repository as festival_repository
import repositories.user_repository as user_repository

country_repository.delete_all()
festival_repository.delete_all()
# user_repository.delete_all()

country_1 = Country("Serbia", "RS")
country_repository.save(country_1)
country_2 = Country("United Kingdom", "UK")
country_repository.save(country_2)

festival_1 = Festival("TITP", country_2)
festival_repository.save(festival_1)
festival_2 = Festival("Exit Festival", country_1)
festival_repository.save(festival_2)


# print(country_repository.select_all())
# print(country_repository.select_by_id(10).name)
# country_repository.delete_by_id(10)

print(festival_repository.select_all())
# print(festival_repository.select_by_id(15).name)

country_update1 = Country("Serbiaaaaaa", "EK", 33)
country_repository.update(country_update1)

