from utils.helpers import *
from config.path_config import *

similar_users = find_similar_users(6,USER_WEIGHTS_PATH,USER2USER_ENCODED,USER2USER_DECODED,n=10 , return_dist=False,neg=False)
print(similar_users)
user_pref = get_user_preferences(6,RATING_DF,DF)
print(user_pref)

