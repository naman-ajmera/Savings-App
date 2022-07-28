# Savings-App
Tortoise Savings App API

As part of the requirements mentioned in the assignment: Standard Views is also available from django at respective endpoints.

**1. Functionality on the brand partner side**

**Brand partner creates A plan - POST /plan/plan-create/**

**Description**
   It takes the following fields as input -{planName, benefitPercentage, benefitType, amountOptions, tenureOptions}
   -amountOptions(I have created this to be a separate model as to store values such as 500, 1000, 1500, 2000, so that brand partner can select the options he want the       user to select from), tenureOptions(I have created this to be a separate model as to store values such as 1, 3, 6 for months, so that brand partner can select the options he want the user to select from), later user can select from the brand partner provided options.
   ![Screenshot 2022-07-27 174514](https://user-images.githubusercontent.com/36277015/181451221-b7521486-2a0b-4744-ad94-9140bd850f0c.png)

**Update a plan by adding promotion to it. - PUT /plan/plan-update/id/**

**Description**
   It takes the following fields as input -{promotionType, promotionStartDate, promotionEndDate, benefitPercentage, promotionCountByUser}
  -Depending on the promotionType -(timeRange/usersCount), brand partner needs to input the startDate and endDate of the promotion or the countOfUsers which can register for the promoted plan.
  ![Screenshot 2022-07-27 185103](https://user-images.githubusercontent.com/36277015/181451299-2bc86368-2334-428d-8635-02de5ca06559.png)
![Screenshot 2022-07-27 185222](https://user-images.githubusercontent.com/36277015/181451348-622e10cd-04da-48b4-bdc3-46b90eac4df7.png)


**2. Functionality on the end-user side**

**List the available plans on the platform - GET /plan/plan-list/**

**Description**
   It returns the list of available plans on the platform and the promotion if any attached to it.
![Screenshot 2022-07-27 190726](https://user-images.githubusercontent.com/36277015/181451405-94b12d0a-ca51-4ae2-9008-c846ec5348dd.png)

**List the available plans on the platform - POST /customer/add-plan/**

**Description**
   It takes the following fields as input -{planID, selectedAmount, selectedTenure, depositedAmount}
   It takes the benefitType, benefitPercentage from the selected plan.
   If the plan has no promotion attached to it, the API will add the plan to user goals.![Screenshot 2022-07-27 195054](https://user-images.githubusercontent.com/36277015/181452306-85b832ed-299a-4097-8c5c-92b00a102290.png)
   If the plan has any promotion attached to it, the APi will check if it is in the limits of the promotion.
   
![Screenshot 2022-07-28 132517](https://user-images.githubusercontent.com/36277015/181453530-ad4b8f15-c72b-49e2-b6d0-6e9b32bb3d21.png)
![Screenshot 2022-07-28 133012](https://user-images.githubusercontent.com/36277015/181453540-8b039a47-f060-42cc-aee2-ff164edab656.png)
