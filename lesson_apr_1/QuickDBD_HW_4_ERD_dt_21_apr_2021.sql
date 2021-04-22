-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/7868tA
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


SET XACT_ABORT ON

BEGIN TRANSACTION QUICKDBD

-- 1
CREATE TABLE [user] (
    [id] int  NOT NULL ,
    [title] varchar(50)  NOT NULL ,
    [description] varchar(250)  NOT NULL ,
    [time_create] datetime  NOT NULL ,
    [time_update] datetime  NOT NULL ,
    CONSTRAINT [PK_user] PRIMARY KEY CLUSTERED (
        [id] ASC
    )
)

-- 2
CREATE TABLE [posts] (
    [id] int  NOT NULL ,
    [post_id] int  NOT NULL ,
    [friend_id] int  NOT NULL ,
    [blog_id] int  NOT NULL ,
    [title] varchar(50)  NOT NULL ,
    [post_body] text  NOT NULL ,
    [time_create] datetime  NOT NULL ,
    [time_update] datetime  NOT NULL ,
    CONSTRAINT [PK_posts] PRIMARY KEY CLUSTERED (
        [id] ASC
    )
)

-- 3
CREATE TABLE [friends] (
    [id] int  NOT NULL ,
    [post_id] int  NOT NULL ,
    [friend_id] int  NOT NULL ,
    [title] varchar(50)  NOT NULL ,
    [time_connect] datetime  NOT NULL ,
    [time_disconnect] datetime  NOT NULL ,
    CONSTRAINT [PK_friends] PRIMARY KEY CLUSTERED (
        [id] ASC
    )
)

-- 4
CREATE TABLE [boards] (
    [id] int  NOT NULL ,
    [board_id] int  NOT NULL ,
    [title] varchar(250)  NOT NULL ,
    [is_active] bool  NOT NULL ,
    CONSTRAINT [PK_boards] PRIMARY KEY CLUSTERED (
        [id] ASC
    )
)

-- 5
CREATE TABLE [blogs] (
    [id] int  NOT NULL ,
    [description] varchar(250)  NOT NULL ,
    [time_create] datetime  NOT NULL ,
    [time_update] datetime  NOT NULL ,
    CONSTRAINT [PK_blogs] PRIMARY KEY CLUSTERED (
        [id] ASC
    )
)

-- 6
CREATE TABLE [board_templates] (
    [id] int  NOT NULL ,
    [title] varchar(50)  NOT NULL ,
    CONSTRAINT [PK_board_templates] PRIMARY KEY CLUSTERED (
        [id] ASC
    )
)

-- 7
CREATE TABLE [status_board_templates] (
    [id] int  NOT NULL ,
    [title] varchar(50)  NOT NULL ,
    [board_template_id] int  NOT NULL ,
    CONSTRAINT [PK_status_board_templates] PRIMARY KEY CLUSTERED (
        [id] ASC
    )
)

ALTER TABLE [posts] WITH CHECK ADD CONSTRAINT [FK_posts_post_id] FOREIGN KEY([post_id])
REFERENCES [user] ([id])

ALTER TABLE [posts] CHECK CONSTRAINT [FK_posts_post_id]

ALTER TABLE [posts] WITH CHECK ADD CONSTRAINT [FK_posts_friend_id] FOREIGN KEY([friend_id])
REFERENCES [friends] ([friend_id])

ALTER TABLE [posts] CHECK CONSTRAINT [FK_posts_friend_id]

ALTER TABLE [posts] WITH CHECK ADD CONSTRAINT [FK_posts_blog_id] FOREIGN KEY([blog_id])
REFERENCES [blogs] ([id])

ALTER TABLE [posts] CHECK CONSTRAINT [FK_posts_blog_id]

ALTER TABLE [friends] WITH CHECK ADD CONSTRAINT [FK_friends_friend_id] FOREIGN KEY([friend_id])
REFERENCES [user] ([id])

ALTER TABLE [friends] CHECK CONSTRAINT [FK_friends_friend_id]

ALTER TABLE [boards] WITH CHECK ADD CONSTRAINT [FK_boards_board_id] FOREIGN KEY([board_id])
REFERENCES [user] ([id])

ALTER TABLE [boards] CHECK CONSTRAINT [FK_boards_board_id]

ALTER TABLE [status_board_templates] WITH CHECK ADD CONSTRAINT [FK_status_board_templates_board_template_id] FOREIGN KEY([board_template_id])
REFERENCES [board_templates] ([id])

ALTER TABLE [status_board_templates] CHECK CONSTRAINT [FK_status_board_templates_board_template_id]

COMMIT TRANSACTION QUICKDBD