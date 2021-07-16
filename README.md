# Work with us!
This is a quick challenge to test your abilities as a developer to design and craft a solution based on a problem, software requirements or user stories.

## Scenario
You work for ACME, a company that has a huge team of developers around the world. We are developing an application to track the assets and licenses that each employee has assigned.

#### Glossary
**Asset**: It is a physical resource which is assigned and shipped to the developer.
**License**: Digital resource assigned to a developer which gives the possibility to use or interact with third party software.

## Requirements
You must create an App to give to an admin the possibility to manage the assets and licenses of the staff. This App will be made of an API and a UI. The requirements of each component will be listed below.

### API Required Endpoints
- **Login admin user:** _As a user, I can login with my credentials to manage the company resources_.
- **Add and disable developers:** _As an authenticated admin user, I can add new developers and or set them as inactive_.
- **Get, Add and Delete of asset assignments:** _As an authenticated admin user, I can add, delete and list any developer's asset_.
- **Get, Add, and delete of license assignments:** _As an authenticated admin user, I can add, delete and list any developer's license_.
Important: When you disable any developer, you should revoke their assignments and clean them up.

#### API Constraints
  - You don't need to create an endpoint to create a user. You can create a global user access in somewhere in the code and validate her/him credentials at login time.
  - Assets and Licenses are static catalogs and they are already written in other files of this repository, so you can include them in your code as well.
  - There is no need to implement a database to store the result of the actions of the admin. You can store data in memory since this app has a short lifecycle. You can also add a database if you want for extra points.

### UI requirements
  - **Login view:** _A view to enter credentials of user admin_
  - **Developer List:**_A list of developers with their name and status_
  - **Add developer:** _A place to create developers. It could be a modal or a standalone view_
  - **Manage developer:**_A view to manage the developers, their assets and licenses_

#### UI Constraints
  - Use a UI framework such as React or Angular.
  - You can use any components library you want
  - You can use any css framework you want

### Entity Attributes
**Asset Attributes:**
  - id: string | number
  - brand: string
  - model: string
  - type: enum<string> ['laptop', 'keyboard', 'mouse', 'headset', 'monitor']

**License Attributes:**
  - id: string | number
  - software: string

**Developer Attributes:**
  - id: string | number
  - fullname: string
  - active: boolean

# Deliverables
You should send to us a public or private repository which should include the following items:
  - Source code of application.
  - Installation guide(in English)
  - Explanation document(in English)

### Nice to have
  - Typescript
  - Tests
  - Public URL(deployed solution)
  - Docker and Docker Compose
  - Any database implemented(MongoDB, Postgres, MySQL)