from datetime import date, datetime
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view
from customerGoals.serializer import CustomerGoalsSerializer
from plan.models import Plan
from rest_framework.response import Response

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Create': '/add-plan/'
    }
    return Response(api_urls)

@api_view(['POST'])
def goalCreate(request):
    goalData = JSONParser().parse(request)
    plan = Plan.objects.filter(id = goalData['planID'])
    planData = plan.values()[0]

    promotionType = planData['promotionType']
    goalData['benefitPercentage'] = planData['benefitPercentage']
    goalData['benefitType'] = planData['benefitType']

    if promotionType == 'usersCount':
        promotionCountByUser = planData['promotionCountByUser']
        if promotionCountByUser == 0:
            return Response({"message": "User limit for this promotion already reached"}, status=status.HTTP_400_BAD_REQUEST)
        newCount = promotionCountByUser - 1
        print(plan.update(promotionCountByUser = newCount))
        if plan.update(promotionCountByUser = newCount) == 0:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    elif promotionType == 'timeRange':
        promotionEndDate = planData['promotionEndDate']
        if promotionEndDate < date.today():
            return Response({"message": "This promotion is already expired on {}".format(promotionEndDate)}, status=status.HTTP_400_BAD_REQUEST)
    
    goal_serializer = CustomerGoalsSerializer(data=goalData)
    if goal_serializer.is_valid():
        goal_serializer.save()
        return Response(goal_serializer.data, status=status.HTTP_201_CREATED) 
    return Response(goal_serializer.errors, status=status.HTTP_400_BAD_REQUEST)