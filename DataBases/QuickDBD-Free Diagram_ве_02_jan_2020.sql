-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/7868tA
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


-- 1
CREATE TABLE `contact` (
    `id` int  NOT NULL ,
    `first_name` char(60)  NOT NULL ,
    `last_name` char(60)  NOT NULL ,
    `middle_name` char(60)  NOT NULL ,
    `prefix` char(10)  NOT NULL ,
    `company_name` char(80)  NOT NULL ,
    `contact_type` char(60)  NOT NULL ,
    `address` char(200)  NOT NULL ,
    `city` char(40)  NOT NULL ,
    `state` char(40)  NOT NULL ,
    `country` char(40)  NOT NULL ,
    `postal_code` char(7)  NOT NULL ,
    `phone` varchar(60)  NOT NULL ,
    `email` varchar(30)  NOT NULL ,
    `create_time` datatime(10)  NOT NULL ,
    PRIMARY KEY (
        `id`
    )
);

-- 2
CREATE TABLE `supplier` (
    `id` int  NOT NULL ,
    `contact_id` int  NOT NULL ,
    `contract_no` varchar(45)  NOT NULL ,
    `contract_title` varchar(50)  NOT NULL ,
    `suplier_type` char(40)  NOT NULL ,
    `contr_eff_date` datetime(10)  NOT NULL ,
    `contr_exp_date` datetime(10)  NOT NULL ,
    `logo` image  NOT NULL ,
    PRIMARY KEY (
        `id`
    )
);

-- 3
CREATE TABLE `client` (
    `id` int  NOT NULL ,
    `contact_id` int  NOT NULL ,
    `date_entered` datetime(10)  NOT NULL ,
    `password` varchar(25)  NOT NULL ,
    `birthday` datetime(10)  NOT NULL ,
    `client_type` varchar(40)  NOT NULL ,
    PRIMARY KEY (
        `id`
    )
);

-- 4
CREATE TABLE `shipper` (
    `id` int  NOT NULL ,
    `contact_id` int  NOT NULL ,
    `contract_no` varchar(45)  NOT NULL ,
    `contract_title` varchar(50)  NOT NULL ,
    `shipper_type` char(40)  NOT NULL ,
    `contr_eff_date` datetime(10)  NOT NULL ,
    `contr_exp_date` datetime(10)  NOT NULL ,
    `logo` image  NOT NULL ,
    PRIMARY KEY (
        `id`
    )
);

-- 5
CREATE TABLE `products` (
    `id` int  NOT NULL ,
    `suplier_id` int  NOT NULL ,
    `product_name` varchar(50)  NOT NULL ,
    `product_brand` varchar(40)  NOT NULL ,
    `year_of_manufacture` int  NOT NULL ,
    `color` char(25)  NOT NULL ,
    `description` text  NOT NULL ,
    `quantity_per_ubit` int  NOT NULL ,
    `unit_price` money  NOT NULL ,
    `product_image` image  NOT NULL ,
    `size` varchar(30)  NOT NULL ,
    `weight` decimal(7,3)  NOT NULL ,
    PRIMARY KEY (
        `id`
    )
);

-- 6
CREATE TABLE `categories` (
    `id` int  NOT NULL ,
    `category` varchar(30)  NOT NULL ,
    `description` text  NOT NULL ,
    PRIMARY KEY (
        `id`
    )
);

-- 7
CREATE TABLE `products_catecories` (
    `id` int  NOT NULL ,
    `product_id` int  NOT NULL ,
    `category_id` int  NOT NULL ,
    PRIMARY KEY (
        `id`
    )
);

-- 8
CREATE TABLE `rating` (
    `id` int  NOT NULL ,
    `client_id` int  NOT NULL ,
    `product_id` int  NOT NULL ,
    `date_posted` datetime(10)  NOT NULL ,
    `rating` decimal(2,1)  NOT NULL ,
    `comment` text  NOT NULL ,
    PRIMARY KEY (
        `id`
    )
);

-- 9
CREATE TABLE `order` (
    `id` int  NOT NULL ,
    `client_id` int  NOT NULL ,
    `shipper_id` int  NOT NULL ,
    `order_date` datetime  NOT NULL ,
    `payment_method` char(20)  NOT NULL ,
    `delivery_method` char(30)  NOT NULL ,
    `delivery_date` datetime  NOT NULL ,
    `total_price` money  NOT NULL ,
    `sale_tax` money  NOT NULL ,
    `discount` decimal(3,2)  NOT NULL ,
    `total_discount` money  NOT NULL ,
    `paid` money  NOT NULL ,
    `transaction_status` varchar(20)  NOT NULL ,
    PRIMARY KEY (
        `id`
    )
);

-- 10
CREATE TABLE `cart` (
    `id` int  NOT NULL ,
    `order_id` int  NOT NULL ,
    `product_id` int  NOT NULL ,
    `date` datetime  NOT NULL ,
    `item_price` money  NOT NULL ,
    `product_quantity` int  NOT NULL ,
    `sub_total` money  NOT NULL ,
    `sale_tax` money  NOT NULL ,
    `discount` decimal(3,2)  NOT NULL ,
    `total_discount` money  NOT NULL ,
    PRIMARY KEY (
        `id`
    )
);

ALTER TABLE `supplier` ADD CONSTRAINT `fk_supplier_contact_id` FOREIGN KEY(`contact_id`)
REFERENCES `contact` (`id`);

ALTER TABLE `client` ADD CONSTRAINT `fk_client_contact_id` FOREIGN KEY(`contact_id`)
REFERENCES `contact` (`id`);

ALTER TABLE `shipper` ADD CONSTRAINT `fk_shipper_contact_id` FOREIGN KEY(`contact_id`)
REFERENCES `contact` (`id`);

ALTER TABLE `products` ADD CONSTRAINT `fk_products_suplier_id` FOREIGN KEY(`suplier_id`)
REFERENCES `supplier` (`id`);

ALTER TABLE `products_catecories` ADD CONSTRAINT `fk_products_catecories_product_id` FOREIGN KEY(`product_id`)
REFERENCES `products` (`id`);

ALTER TABLE `products_catecories` ADD CONSTRAINT `fk_products_catecories_category_id` FOREIGN KEY(`category_id`)
REFERENCES `categories` (`id`);

ALTER TABLE `rating` ADD CONSTRAINT `fk_rating_client_id` FOREIGN KEY(`client_id`)
REFERENCES `client` (`id`);

ALTER TABLE `rating` ADD CONSTRAINT `fk_rating_product_id` FOREIGN KEY(`product_id`)
REFERENCES `products` (`id`);

ALTER TABLE `order` ADD CONSTRAINT `fk_order_client_id` FOREIGN KEY(`client_id`)
REFERENCES `client` (`id`);

ALTER TABLE `order` ADD CONSTRAINT `fk_order_shipper_id` FOREIGN KEY(`shipper_id`)
REFERENCES `shipper` (`id`);

ALTER TABLE `cart` ADD CONSTRAINT `fk_cart_order_id` FOREIGN KEY(`order_id`)
REFERENCES `order` (`id`);

ALTER TABLE `cart` ADD CONSTRAINT `fk_cart_product_id` FOREIGN KEY(`product_id`)
REFERENCES `products` (`id`);

