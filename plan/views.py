from plan.models import Plan
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from plan.serializer import PlanSerializer

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/plan-list/',
        'Create': '/plan-create/',
        'Update': '/plan-update/<int:pk>/'
    }
    return Response(api_urls)
        
@api_view(['GET'])
def planList(request):
    plan = Plan.objects.all()
    plan_serializer = PlanSerializer(plan, many=True)
    return Response(plan_serializer.data)

@api_view(['POST'])
def planCreate(request):
    plan_data = JSONParser().parse(request)
    plan_serializer = PlanSerializer(data=plan_data)
    if plan_serializer.is_valid():
        plan_serializer.save()
        return Response(plan_serializer.data, status=status.HTTP_201_CREATED) 
    return Response(plan_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
def planUpdate(request, pk):
    try: 
        plan = Plan.objects.filter(id=pk) 
    except Plan.DoesNotExist: 
        return Response({'message': 'The Plan does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    promotionData = JSONParser().parse(request)
    promotionType = promotionData['promotionType']
    if(promotionType == 'usersCount'):
        if plan.update(promotionType = promotionType, isPromotionActive=True, 
            benefitPercentage = promotionData['benefitPercentage'], promotionCountByUser = promotionData['promotionCountByUser']):
            return Response({"status":"success"}, status=status.HTTP_200_OK) 
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif(promotionType == 'timeRange'):
        if promotionData['promotionStartDate'] > promotionData['promotionEndDate']:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if plan.update(promotionType = promotionType, isPromotionActive=True, 
        promotionStartDate = promotionData['promotionStartDate'], benefitPercentage = promotionData['benefitPercentage'],
        promotionEndDate = promotionData['promotionEndDate']):
            return Response({"status":"success"}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': 'Unkown promotion type'}, status=status.HTTP_400_BAD_REQUEST)     