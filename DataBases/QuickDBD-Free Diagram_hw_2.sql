-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/7868tA
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

use hw_2_dt_19_dec_2020;
go

SET XACT_ABORT ON

BEGIN TRANSACTION QUICKDBD

CREATE TABLE [good] (
    [id] int  NOT NULL ,
    [upc] int  NOT NULL ,
    [name] varchar(35)  NOT NULL ,
    [model] varchar(25)  NOT NULL ,
    [price] float  NOT NULL ,
    [status] varchar(3)  NOT NULL ,
    CONSTRAINT [PK_good] PRIMARY KEY CLUSTERED (
        [id] ASC
    )
)

CREATE TABLE [category] (
    [id] int  NOT NULL ,
    [category_id] int  NOT NULL ,
    [name] varchar(35)  NOT NULL ,
    [description] varchar(40)  NOT NULL ,
    CONSTRAINT [PK_category] PRIMARY KEY CLUSTERED (
        [id] ASC
    )
)

CREATE TABLE [cart] (
    [id] int  NOT NULL ,
    [good] varchar(35)  NOT NULL ,
    CONSTRAINT [PK_cart] PRIMARY KEY CLUSTERED (
        [id] ASC
    )
)

CREATE TABLE [order] (
    [id] int  NOT NULL ,
    [order_number] int  NOT NULL ,
    [date] datetime  NOT NULL ,
    [good] varchar(35)  NOT NULL ,
    [quantity_of_units] int  NOT NULL ,
    CONSTRAINT [PK_order] PRIMARY KEY CLUSTERED (
        [id] ASC
    )
)

CREATE TABLE [customer] (
    [id] int  NOT NULL ,
    [first_name] varchar(25)  NOT NULL ,
    [last_name] varchar(25)  NOT NULL ,
    [date_of_birth] datetime  NOT NULL ,
    [gender] varchar(5)  NOT NULL ,
    [phone] int  NOT NULL ,
    [login] varchar(25)  NOT NULL ,
    [password] varchar(25)  NOT NULL ,
    CONSTRAINT [PK_customer] PRIMARY KEY CLUSTERED (
        [id] ASC
    )
)

ALTER TABLE [category] WITH CHECK ADD CONSTRAINT [FK_category_category_id] FOREIGN KEY([category_id])
REFERENCES [good] ([id])

ALTER TABLE [category] CHECK CONSTRAINT [FK_category_category_id]

ALTER TABLE [cart] WITH CHECK ADD CONSTRAINT [FK_cart_id] FOREIGN KEY([id])
REFERENCES [order] ([id])

ALTER TABLE [cart] CHECK CONSTRAINT [FK_cart_id]

ALTER TABLE [order] WITH CHECK ADD CONSTRAINT [FK_order_id] FOREIGN KEY([id])
REFERENCES [good] ([id])

ALTER TABLE [order] CHECK CONSTRAINT [FK_order_id]

ALTER TABLE [customer] WITH CHECK ADD CONSTRAINT [FK_customer_id] FOREIGN KEY([id])
REFERENCES [cart] ([id])

ALTER TABLE [customer] CHECK CONSTRAINT [FK_customer_id]

COMMIT TRANSACTION QUICKDBD