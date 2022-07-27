# Savings-App
Tortoise Savings App API

As part of the requirements mentioned in the assignment:

1. Functionality on the brand partner side,
  I have created 2 APIs
   **PUT /plan/plan-create**
   It takes the following fields as input -{planName, benefitPercentage, benefitType, amountOptions, tenureOptions}
   -amountOptions(I have created this to be a separate model as to store values such as 500, 1000, 1500, 2000, so that brand partner can select the options he want the       user to select from), tenureOptions(I have created this to be a separate model as to store values such as 1, 3, 6 for months, so that brand partner can select the       options he want the user to select from), later user can
        "amountOptions": [
            1,![Screenshot 2022-07-27 174514](https://user-images.githubusercontent.com/36277015/181244449-e8b9c7c9-29f6-40c1-b45c-c2d23e635d3f.png)

            2
        ],
        "tenureOptions": [
            2,
            3
        ]
} 
