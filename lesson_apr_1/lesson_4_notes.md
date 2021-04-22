# 1 
tasks
---
id int PK
title varchar(200)
description text
is_completed bool
time_create datetime
time_update datetime
priority int
status_id int FK >- status.id
owner_user_id int FK >- users.id
board_id int FK >- boards.id

#2
status
---
id int PK
title varchar(50)
board_id int FK >- boards.id

#3
users
---
id int PK
last_name varchar(100)
first_name varchar(100)
login varchar(100)
email varchar(200)
password varchar(255)

#4
comments
---
id int PK
comment text
user_id int FK >- users.id
task_id int FK >- tasks.id


#5
executers
---
id int PK
task_id int FK >- tasks.id
user_id int FK >- users.id

#6
boards
---
id int PK
title varchar(200)
is_active bool

#7
board_templates
---
id int PK
title varchar(50)

#8
status_board_templates
---
id int PK
title varchar(50)
board_template_id int FK >- board_templates.id

# ********************

# Home_work_4 ERD of some blog
# 1
user
---
id int PK
title varchar(50)
description varchar(250)
time_create datetime
time_update datetime

# 2
posts
---
id int PK
post_id int FK >- user.id 
friend_id int FK >- friends.friend_id
blog_id int FK >- blogs.id
title varchar(50)
post_body text
time_create datetime
time_update datetime

# 3
friends
---
id int PK
post_id int FK
friend_id int FK >- user.id 
title varchar(50)
time_connect datetime
time_disconnect datetime

# 4
boards
---
id int PK
board_id int FK >- user.id
title varchar(250)
is_active bool

# 5
blogs
---
id int PK
description varchar(250)
time_create datetime
time_update datetime


#6
board_templates
---
id int PK
title varchar(50)

#7
status_board_templates
---
id int PK
title varchar(50)
board_template_id int FK >- board_templates.id










