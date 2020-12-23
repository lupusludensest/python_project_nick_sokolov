-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/7868tA
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

use practice_dt_18_dec_2020;
go

SET XACT_ABORT ON

BEGIN TRANSACTION QUICKDBD

CREATE TABLE [users] (
    [id] int  NOT NULL ,
    [login] varchar(25)  NOT NULL ,
    [password] varchar(32)  NOT NULL ,
    CONSTRAINT [PK_users] PRIMARY KEY CLUSTERED (
        [id] ASC
    )
)

CREATE TABLE [person_data] (
    [id] int  NOT NULL ,
    [user_id] int  NOT NULL ,
    [name] varchar(40)  NOT NULL ,
    [age] int  NOT NULL ,
    [b_day] datetime  NOT NULL ,
    [salary] decimal  NOT NULL ,
    CONSTRAINT [PK_person_data] PRIMARY KEY CLUSTERED (
        [id] ASC
    )
)

CREATE TABLE [contacts] (
    [id] int  NOT NULL ,
    [first_name] varchar(50)  NOT NULL ,
    [last_name] varchar(50)  NOT NULL ,
    CONSTRAINT [PK_contacts] PRIMARY KEY CLUSTERED (
        [id] ASC
    )
)

CREATE TABLE [users_contacts] (
    [id] int  NOT NULL ,
    [user_id] int  NOT NULL ,
    [contacts_id] int  NOT NULL ,
    CONSTRAINT [PK_users_contacts] PRIMARY KEY CLUSTERED (
        [id] ASC
    )
)

CREATE TABLE [phones] (
    [id] int  NOT NULL ,
    [contact_id] int  NOT NULL ,
    [phone] int  NOT NULL ,
    [time_update] datetime  NOT NULL ,
    CONSTRAINT [PK_phones] PRIMARY KEY CLUSTERED (
        [id] ASC
    )
)

ALTER TABLE [person_data] WITH CHECK ADD CONSTRAINT [FK_person_data_user_id] FOREIGN KEY([user_id])
REFERENCES [users] ([id])

ALTER TABLE [person_data] CHECK CONSTRAINT [FK_person_data_user_id]

ALTER TABLE [users_contacts] WITH CHECK ADD CONSTRAINT [FK_users_contacts_user_id] FOREIGN KEY([user_id])
REFERENCES [users] ([id])

ALTER TABLE [users_contacts] CHECK CONSTRAINT [FK_users_contacts_user_id]

ALTER TABLE [users_contacts] WITH CHECK ADD CONSTRAINT [FK_users_contacts_contacts_id] FOREIGN KEY([contacts_id])
REFERENCES [contacts] ([id])

ALTER TABLE [users_contacts] CHECK CONSTRAINT [FK_users_contacts_contacts_id]

ALTER TABLE [phones] WITH CHECK ADD CONSTRAINT [FK_phones_contact_id] FOREIGN KEY([contact_id])
REFERENCES [contacts] ([id])

ALTER TABLE [phones] CHECK CONSTRAINT [FK_phones_contact_id]

COMMIT TRANSACTION QUICKDBD

