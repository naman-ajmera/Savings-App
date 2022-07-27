# Savings-App
Tortoise Savings App API

As part of the requirements mentioned in the assignment:

1. Functionality on the brand partner side,
  I have created 2 APIs
   PUT /plan/plan-create - I takes the following fields, planName, benefitPercentage, benefitType, 
    amountOptions( I have created this to be a separate model as to store values such as )
        "amountOptions": [
            1,
            2
        ],
        "tenureOptions": [
            2,
            3
        ]
} 
