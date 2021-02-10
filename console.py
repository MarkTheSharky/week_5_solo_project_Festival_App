import pdb

from models.country import Country
from models.festival import Festival
from models.user import User
from models.attendees import Attendee

import repositories.country_repository as country_repository
import repositories.festival_repository as festival_repository
import repositories.user_repository as user_repository
import repositories.attendee_repository as attendee_repository

# festival_repository.delete_all()
# country_repository.delete_all()
# user_repository.delete_all()

country_1 = Country("Serbia", "RS")
country_repository.save(country_1)
country_2 = Country("United Kingdom", "UK")
country_repository.save(country_2)

festival_1 = Festival("TITP", country_2)
festival_repository.save(festival_1)
festival_2 = Festival("Exit Festival", country_1)
festival_repository.save(festival_2)

user_1 = User("Mark", "Burns", 33)
user_repository.save(user_1)
user_2 = User("Heather", "MacSween", 33)
user_repository.save(user_2)

# print(country_repository.select_all())
# print(country_repository.select_by_id(10).name)
# country_repository.delete_by_id(10)

# print(festival_repository.select_all())
# print(festival_repository.select_by_id(22).name)
# festival_repository.delete_by_id(3)

# print(user_repository.select_all())
# print(user_repository.select_by_id(48).first_name)
# user_repository.delete_by_id(2)


# country_update1 = Country("Serbiaaaaaa", "EK", 33)
# country_repository.update(country_update1)

# festival_update1 = Festival("T In The Park", 'UK' )
# festival_repository.update(festival_update1)

attendee1 = Attendee(user_1, festival_1)
attendee_repository.save(attendee1)

attendee2 = Attendee(user_1, festival_2)
attendee_repository.save(attendee2)

attendee3 = Attendee(user_2, festival_1)
attendee_repository.save(attendee3)

attendee4 = Attendee(user_2, festival_2)
attendee_repository.save(attendee4)

print(user_repository.festivals(user_1))