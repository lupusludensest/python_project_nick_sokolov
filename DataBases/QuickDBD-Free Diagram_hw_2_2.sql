-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/7868tA
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


SET XACT_ABORT ON

BEGIN TRANSACTION QUICKDBD

CREATE TABLE [products] (
    [id] int  NOT NULL ,
    [product_name] varchar(50)  NOT NULL ,
    [product_brand] varchar(40)  NOT NULL ,
    [year_of_manufacture] int  NOT NULL ,
    [color] char(25)  NOT NULL ,
    [description] text  NOT NULL ,
    [price] money  NOT NULL ,
    CONSTRAINT [PK_products] PRIMARY KEY CLUSTERED (
        [id] ASC
    )
)

CREATE TABLE [products_catecories] (
    [id] int  NOT NULL ,
    [product_id] int  NOT NULL ,
    [category_id] int  NOT NULL ,
    CONSTRAINT [PK_products_catecories] PRIMARY KEY CLUSTERED (
        [id] ASC
    )
)

CREATE TABLE [categories] (
    [id] int  NOT NULL ,
    [category] varchar(30)  NOT NULL ,
    [description] text  NOT NULL ,
    CONSTRAINT [PK_categories] PRIMARY KEY CLUSTERED (
        [id] ASC
    )
)

CREATE TABLE [orders] (
    [id] int  NOT NULL ,
    [client_id] int  NOT NULL ,
    [date] datetime  NOT NULL ,
    [pyment_method] char(20)  NOT NULL ,
    [delivery_method] char(30)  NOT NULL ,
    [delivery_date] datetime  NOT NULL ,
    [total_price] money  NOT NULL ,
    CONSTRAINT [PK_orders] PRIMARY KEY CLUSTERED (
        [id] ASC
    )
)

CREATE TABLE [carts] (
    [id] int  NOT NULL ,
    [order_id] int  NOT NULL ,
    [product_id] int  NOT NULL ,
    [date] datetime  NOT NULL ,
    [item_price] money  NOT NULL ,
    [product_quantity] int  NOT NULL ,
    [sub_total] money  NOT NULL ,
    CONSTRAINT [PK_carts] PRIMARY KEY CLUSTERED (
        [id] ASC
    )
)

CREATE TABLE [client] (
    [id] int  NOT NULL ,
    [first_name] char(60)  NOT NULL ,
    [last_name] char(60)  NOT NULL ,
    [nick_name] varchar(60)  NOT NULL ,
    [email] varchar(60)  NOT NULL ,
    [password] varchar(25)  NOT NULL ,
    [address] varchar(40)  NOT NULL ,
    [city] char(80)  NOT NULL ,
    [provice] char(50)  NOT NULL ,
    [country] char(40)  NOT NULL ,
    [postal_code] varchar(7)  NOT NULL ,
    CONSTRAINT [PK_client] PRIMARY KEY CLUSTERED (
        [id] ASC
    )
)

ALTER TABLE [products_catecories] WITH CHECK ADD CONSTRAINT [FK_products_catecories_product_id] FOREIGN KEY([product_id])
REFERENCES [products] ([id])

ALTER TABLE [products_catecories] CHECK CONSTRAINT [FK_products_catecories_product_id]

ALTER TABLE [products_catecories] WITH CHECK ADD CONSTRAINT [FK_products_catecories_category_id] FOREIGN KEY([category_id])
REFERENCES [categories] ([id])

ALTER TABLE [products_catecories] CHECK CONSTRAINT [FK_products_catecories_category_id]

ALTER TABLE [orders] WITH CHECK ADD CONSTRAINT [FK_orders_client_id] FOREIGN KEY([client_id])
REFERENCES [client] ([id])

ALTER TABLE [orders] CHECK CONSTRAINT [FK_orders_client_id]

ALTER TABLE [carts] WITH CHECK ADD CONSTRAINT [FK_carts_order_id] FOREIGN KEY([order_id])
REFERENCES [orders] ([id])

ALTER TABLE [carts] CHECK CONSTRAINT [FK_carts_order_id]

ALTER TABLE [carts] WITH CHECK ADD CONSTRAINT [FK_carts_product_id] FOREIGN KEY([product_id])
REFERENCES [products] ([])

ALTER TABLE [carts] CHECK CONSTRAINT [FK_carts_product_id]

COMMIT TRANSACTION QUICKDBD