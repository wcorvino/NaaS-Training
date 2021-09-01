from user import User
from post import Post

app_user_one = User("johndoe@xyzzy.com", "John Doe", "pwd1", "DevOps Engineer")
app_user_one.get_user_info()

app_user_one.change_job_title("DevOps Trainer")
app_user_one.get_user_info()

app_user_two = User("janedoe@xyxxy.com", "Jane Doe", "pwd2", "DevOps Engineer II")
app_user_two.get_user_info()

new_post = Post("Python tutorial today", app_user_two.name)
new_post.get_post_info()

