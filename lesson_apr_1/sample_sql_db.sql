# 1
user
---
id int PK
title varchar(50)
description varchar(250)
time_create datetime
time_update datetime
d_of_b date

# 2
posts
---
id int PK
user_id int FK >- user.id 
blog_id int FK >- blogs.id
title varchar(50)
post_body text
time_create datetime
time_update datetime


# 3
blogs
---
id int PK
title varchar(150)
description varchar(250)
time_create datetime
time_update datetime

# 4
categories
---
id int PK
title varchar(150)
description varchar(250)
time_create datetime
time_update datetime
category_img_url varchar(200)

# 5
postCategories
---
id int PK
post_id int FK >- posts.id
categories_id int FK -< categories.id
time_create datetime
time_update datetime

# 6
comments
---
id int PK
reference_comment_id int FK >- comments.id
user_id int FK >- user.id
posts_id int FK >- posts.id
comment_txt varchar(150)
time_create datetime
time_update datetime

# 7
tags
---
id int PK
title varchar(150)
description varchar(250)
time_create datetime
time_update datetime
category_img_url varchar(200)

# 8
postsTags
---
id int PK
post_id int FK >- posts.id
tags_id int FK >- tags.id

