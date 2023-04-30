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

## 4. Features

Please note that the features section contains relevant extracts from the project wireframes. The complete wireframes are included in section 7 of this document.

### 4.1 Navigation Bar

* The navigation bar provides a Home link to return to the home page from any other page. This link will be highlighted to indicate when a user is on the homepage.

* The navigation bar contains the BBS logo. The logo is also a link to the home page in line with likely user expectations.

* When no user is logged in the navigation bar provides links to Register or Log In.

* When a user is logged in the links to My Account and Log Out replace the Register or Log In options.

* The Register, Log In, My Account, and Log Out links are highlighted as active when the appropriate page is open.

* An Admin Only link to the admin log in page is also provided for ease of access. This link will have a different colour to differentiate it from the main user links.

<details><summary>Fig. 4.1.1 Navigation Bar with no user logged in.</summary>
<img src="documents/navbar-logged-out.png"
alt="wireframe of the navigation bar when there is no user logged in"></details>

<details><summary>Fig. 4.1.2 Navigation Bar with a user logged in.</summary>
<img src="documents/navbar-logged-in.png"
alt="wireframe of the navigation bar when there is a user logged in"></details>

### 4.2 Header

* The header contains the business name "Big Boring Shop" as an h1 heading in a prominent location on the page.

* The header contains a h2 sub-heading "Your weekly shopping delivered!".

* The header contains a hero image with a theme related to the purpose of the website.

<details><summary>Fig. 4.2.1 Header</summary>
<img src="documents/header.png"
alt="wireframe of the page header"></details>

### 4.3 Footer

* The footer contains links to social media - Facebook, Instagram, Twitter, YouTube.

* The footer contains the newsletter registration form linking to the mailchimp service.

* The footer is sticky, always appearing at the bottom of the view.

### 4.4 Home Page Main Section

<details><summary>Fig. 4.4.1 Home Page Main Section on Desktop</summary>
<img src="documents/home-main-desktop.png"
alt="wireframe of the home page main section on desktop"></details>

<details><summary>Fig. 4.4.2 Home Page Main Section on Mobile</summary>
<img src="documents/home-main-mobile.png"
alt="wireframe of the home page main section on a mobile device"></details>

### 4.5 Products Page

* Search and filter options are provided.

## 5. Future Features

## 6. Typography and Color Scheme

### 6.1 Typography

### 6.2 Color Scheme

## 7. Wireframes

## 8. Database Entity Relationship Diagram

## 9. Agile Methodology

## 10. Technology

The following technologies were used in developing and deploying the website:

* Python

* HTML

* CSS

* Javascript

* Django

* Posrgres database via elephantsql.com

* AWS Storage

* Bootstrap

* jQuery

* django-allauth v.0.41.0

* Google Fonts

* The IDE used was GITPOD

* The repository used is GITHUB

* GITHUB issues, projects and boards are used to implement Agile practices.

* The website is deployed on Heroku.

* Balsamiq was used to prepare wireframes.

* Lucidchart was used to prepare the Database Entity Relationship Diagram.

* Google Chrome was used as the main web browser both for accessing the IDE and the repository as well as to view the application locally and on Heroku during development.

* Developer Tools in Google Chrome were used to test the application during development and following completion.

* Microsoft Edge and Mozilla Firefox were used to test cross browser compatibility.

* The W3C Markup Validation Service was used for HTML code validation.

* The W3C CSS Validation Service was used for CSS code validation.

* JS Hint was used for javascript/jquery validation.

* The Code Institute Python Linter was used for python validation.

* The amiresponsive website was used to check responsiveness.

## 11. Testing

## 12. Deployment

## 13. References and Credits

### 13.1 References

* The Code Institute student Template for Gitpod provided by Code Institute at https://github.com/Code-Institute-Org/gitpod-full-template. This template allows easy set up of a repository and workspace.

* The Code Institute Hello Django and I Think therefore I Blog example projects provided within the online learning system (LMS). These provide general guidance as to minimun project requirements. They also provide an overview of best practice and industry conventions. Furthermore they outline the key aspects of the Django framework, the process to import Django into the IDE and the process to deploy a production version to Heroku.

* The code Institute Boutique Ado example project provided within the online learning system (LMS). This provides general guidance as to minimun project requirements. It also provides an overview of best practice and industry conventions. In particular it provides boilerplate code for this project as well as the process and code required to link to the Stripe payment platform.

* The Code Institute Principles of Agile Development module provided by Code Institute within its online learning system (LMS). This module provides information on Agile theory as well as systems for its practical implementation that have been applied to this project.

* Django version 3.2 documentation available at https://docs.djangoproject.com/en/3.2/. Django is the full-stack framework technology used to develop this project.

* Python version 3.8 documentation available at https://docs.python.org/3.8/. Python is the backend programming language used in the Django full-stack framework technology used to develop this project.

* Bootstrap version 5.3 documentation available at https://getbootstrap.com/docs/5.3/getting-started/introduction/. Bootstrap has been used throughout this project to create page styles and components.

* jQuery documentation available at https://jquery.com/. jQuery has been used for event handling and DOM manipulation including to aid responsivness.

* django-allauth documentation available at https://django-allauth.readthedocs.io/en/latest/index.html. django-allauth has been used for user sign up/ log in/ authentication.

* fontpair information on font styles and pairings at https://www.fontpair.co/.

* Google Fonts documentation available at https://fonts.google.com/. Google Fonts has been used to import Roboto and Roboto Condensed font styles.

* Answer by username ladhari to a question on Stack Overflow at https://stackoverflow.com/questions/20138049/redirect-user-to-another-url-with-django-allauth-log-in-signal for information on having seperate django redirects for sign up and log in.

* Real Python information on using current user instance in the backend via request.user at https://realpython.com/django-view-authorization/.

* w3schools information on the jQuery val() Method at https://www.w3schools.com/jquery/html_val.asp.

* w3schools information on the jQuery attr() Method at https://www.w3schools.com/jquery/html_attr.asp

* w3schools information on rotate in CSS at https://www.w3schools.com/cssref/css_pr_rotate.php

* Answers by both username "c-smile" and username "Pointy" to a question on Stack Overflow available at https://stackoverflow.com/questions/6131119/jquery-attribute-selector-variable for information on the correct syntax when using the jQuery attribute selector with a variable as the value.

* "How to use Django Messages Framework" by JAYSHA on ORDINARY CODERS available at https://ordinarycoders.com/blog/article/django-messages-framework for information on creating custom alerts using Django messages.

* Answer by Mahdi Zare to a question on Stack Overflow at https://stackoverflow.com/questions/27064206/django-check-if-a-related-object-exists-error-relatedobjectdoesnotexist for information on using ObjectDoesNotExist from django.core.exceptions.

* "Dynamic classes in navbar" from Django World by Yash Patel available at https://www.youtube.com/watch?v=qLG6B6yWH58 for code and information regarding the addition of the active class to the correct link in the navbar of a base template.

* mdn web docs information on the HTML input type "tel" and the pattern attribute available at https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/tel.

* w3schools information on the HTML data-* attribute available at https://www.w3schools.com/tags/att_data-.asp.

* "How to Get the data-id Attribute of an Element Using jQuery" by TutorialRepublic, available at https://www.tutorialrepublic.com/faq/how-to-get-the-data-id-attribute-of-an-element-using-jquery.php#:~:text=Alternatively%2C%20you%20can%20also%20use,the%20statement%20like%20%24(this). This was a source for guidance on combined use of a data attribute with the jQuery attr() method.

* The W3C Markup Validation Service available at https://validator.w3.org/ for HTML code validation.

* The W3C CSS Validation Service available at https://jigsaw.w3.org/css-validator/ for CSS code validation.

* JS Hint available at https://jshint.com/ for javascript/jquery validation.

* The Code Institute Python Linter available at https://pep8ci.herokuapp.com/ for python validation.

* The amiresponsive website available at https://ui.dev/amiresponsive to check responsiveness.

* Contribution by Levon on Stack Overflow available at https://stackoverflow.com/questions/10660435/how-do-i-split-the-definition-of-a-long-string-over-multiple-lines for information on how to split strings over multiple lines so as not to exceed the maximum line length.

* Contribution by Rahul Gupta on Stack Overflow available at https://stackoverflow.com/questions/31925009/django-media-url-not-set-in-template for information on adding the media context processor in settings.py so as to use MEDIA_URL in templates.

### 13.2 Credits

* The hero image is a photo by Sora Shimazaki sourced from Pexels at: https://www.pexels.com/photo/close-up-photo-of-assorted-colored-push-carts-5926217/

* Photo of eggs by Pixabay sourced from Pexels at: https://www.pexels.com/photo/brown-eggs-on-brown-wooden-bowl-on-beige-knit-textile-162712/

* Photo of sugar by Suzy Hazelwood sourced from Pexels at: https://www.pexels.com/photo/close-up-photo-of-sugar-cubes-in-glass-jar-2523650/

* Photo of a water bottle by Steve Johnson sourced from Pexels at: https://www.pexels.com/photo/clear-disposable-bottle-on-black-surface-1000084/

* Photo of a toothbrush by Karolina Grabowska sourced from Pexels at: https://www.pexels.com/photo/photo-of-toothpaste-on-toothbrush-4202927/

* Photo of toilet paper by Vlada Karpovich sourced from Pexels at: https://www.pexels.com/photo/stack-of-toilet-paper-rolls-in-a-basket-3958185/

* Image size and format adjusting by Reduce Images: https://www.reduceimages.com/

* Converting images to webp format by FreeConvert: https://www.freeconvert.com/image-converter

* Favicon generation by favicon.io: https://favicon.io/

* Fellow students in the KCETB-Code Institute cohort for the feedback, advice, and, constant discussion of all things code.

* Ms. Irene Neville, Code Institute cohort facilitator, for the provision of or signposting towards all key pieces of information needed to ensure the successful completion of the project to the required standards.

* Mr. Rohit Sharma (Mentor) for guidance on overall project approach, industry standards and, README requirements.