# LendingFront

This is the technical test for python developer in LendingFront

## Components

Based on the all the context described in the test, the application should be developed with microservices based architecture, in that way each one of the microservice only have to accomplish an specific goal over the entire loan application flow. This approach allows to has fast deployment and scalable solution based on the demand for each step or phase during the overall process. Next you can find the components description placed on the diagram.

![components](https://github.com/jcardenasc93/LendingFront/blob/main/architecture/components.png)

### Cognito SDK

For all the login/sign up processes I suggest delegating that responsibility to [Cognito](https://aws.amazon.com/cognito/), so the team can focus in develop the real core to handle the business logic for the application. To include this AWS service in the application is necessary to implement the Cognito SDK component that allows connect the application with the service.

### Interfaces

The interfaces are components related to the frontend layer of the application

#### Login Interface

This component is responsible for allows users to perform login and sign up flows with the application. Both components interacts with the Cognito SDK in order to complete each one of the processes.

#### User Interface

The user interface is the main interface of the application. In this interface a logged user can consult any information related to loan applications or funded loans, the current state, previous payments, future payments, etc.

### Loan Application

The Loan Application component is a sub-system component who will handle different flows and decisions about loan applications. According with the test description the application evaluate the loan application based on different info fetched from external systems (from the information given by the user). The several components could be deployed with cloud services that works based on demand (i.e: AWS Lambda functions with serverless framework).

#### Basic Info Reader

This component is one of the microservices suggested. It's responsible for collecting the business related information given by the user during the registration process. That info is stored in Cognito service so to get access to the info this component must interact with the Cognito SDK. This microservice expose an endpoint that allows retrieve the business information, this endpoint will be consumed by the other components.

#### Bank Transaction Checker

Another component with the unique goal of collecting specific business bank transfer information 

#### Credit Report Checker

Other important information that the application should process to evaluate a loan application, is the business credit reports. So this component will be develop to perform that task for every loan application

#### Yelp Integrator

The application collects non-traditional information of the business too. In this specific case collects information from the yelp reviews of the business. This component allows the application to consume the yelp API to get the information of interest for the application process.

#### Application Evaluator

This component gathers all the information from the components described above. Once all the required business information is available, the application could evaluate the loan application to give an answer. This component will keep all the logic for the evaluation process, giving isolation to process the information in order to determines if the loan is viable or not. 

#### Application Descriptor

This component exposes an endpoint that allows the _User Interface_ component to display the current status and other data related to the application process

### Funded Loan

The Funded Loan component handles the different automated processes required for funded loans. This component is a sub-system type (like _Loan Application_) because it is built by other components

#### Payment Collector

The application collects payments daily. So this component handles the process to create the daily file with all due payments and sent it to the ACH network. The component should be runs like a batch scheduled process

#### Payments Update

After the _Payment Collector_ sent the file to the ACH network the application updates the payments based on another file retrieved by the ACH network. Based on that report this component updates the data of each funded loan to keep the loan status updated. Same as the previous component it could be run in a batch scheduled process (if the application receives the ACH report at the same time every day).

#### Loan Descriptor

Similar to the _Application Descriptor_ this component allows that the _User Interface_ could display several data related to the loan status, like payments, current status, dates, etc.





