# Portfolio Project 5 - Big Boring Shop README

## 1. Purpose of the Project

Big Boring Shop intends to establish itself as an online grocery store. Its stated aim is to compete with low-cost grocery retailers but in the form of a fully online service including delivery with no high street presence. The lack of a high street presence is a deliberate part of the business model, with the aim of eliminating the high costs associated with this form of retail. Instead a warehouse and delivery system will form the key business infrastructure.

Furthermore, with a view to providing a competive service the store will focus on a narrow selection of popular, high volume, day to day household goods and foods. Niche products will not form part of the offering.

In terms of the marketing of the business the intention is to be quite upfront about the model. The business will be saying to customers that the big weekly shop to buy the usual essentials is also the big, time consuming, not so exciting weekly chore - the Big Boring Shop! So why not spend your precious time doing something a bit more exciting, maybe some proper retail therapy, and let us look after the boring stuff! We will even deliver to your door.

As the model relies entirely on an online presence, the need for a simple easy to use website and payment system together with a comprehensive web marketing strategy is clear.

## 2. E-commerce Model

The proposed e-commerce application type can be defined as follows:

* It is a business-to-customer(B2C) model selling ito individual grocery customers and households.

* It is selling groceries and is therefore a "products" application type.

* It will accept single "one-off" payments.

Based on the above key features that will need to be provided are as follows:

* An easy payment gateway including a shopping cart, purchase summary and a secure, recognised, easy to use debit/credit card payment system.

* Clear product descriptions together with high quality images.

* Product search and filter options.

* Out of stock notices.

* Order notifications.

* Product Ratings/ Reviews.

* Ability to create a user account with appropriate authentication.

As a result the following database tables will be required:

* User
* User Profile
* Products
* Order
* Order Item
* Comment

The above outlines the key elements of the proposed e-commerce model and the remainder of this document is developed with this model in mind.

## 3. User Stories - Minimum Viable Product (MVP)

1. As a **Visiting User** I can **easily view information on the type of business this is** so that **I can quickly determine if the business provides the service/products I require.**

2. As a **Visiting User** I can **view a list of products the business sells** so that **I can choose items I may wish to purchase.**

3. As a **Visiting User** I can **search and filter the products list** so that **I can easily find the products I need.**

4. As a **Visiting User** I can **view the details for a specific product** so that **I can decide if the particular product is the one I wish/need to purchase.**

5. As a **Visiting User** I can **view details, including costs, for delivery** so that **I know what the costs and terms are before I start spending time adding items to a potential purchase list.**

6. As a **Visiting User** I can **add items to a shopping cart** so that **after choosing an item to potentially purchase I can continue to look at other items, add further items, and keep track of the overall potential total.**

7. As a **Visiting User** I can **view my shopping cart purchase summary** so that **I can review all of the items I have added to the cart and the total purchase cost.**

8. As a **Visiting User** I can **adjust the quantity of any item in my cart or remove an item completely** so that **I can easily confirm a final purchase list just prior to making a purchase.**

9. As a **Visiting User** I can **make an online payment with my debit or credit card** so that **I can easily purchase my chosen products.**

10. As a **Visiting User** I can **create an account and save my details** so that **I do not have to enter all of my details each time I make a purchase on this website.**

11. As a **Site Administrator** I can **log in to the admin pages of the website** so that **I can securely carry out admin functions in sections of the site not accessible to the general public.**

12. As a **Site Administrator** I can **add products to the product list** so that **the website can be easily updated with the latest product offerings from the business.**

13. As a **Site Administrator** I can **edit product details** so that **the product details can be easily kept up to date over time.**

14. As a **Site Administrator** I can **delete products from the product list** so that **any products no longer sold by the business are easily removed from the product offering.**