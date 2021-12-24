from Common_Responses import Bad_Response, Created_Response, No_Content_Response, Ok_Response
from rest_framework.decorators import api_view
from .models import LeaveRequest
from .serializers import LeaveRequestSerializer, LeaveRequestUpdateSerializer
from systemControl.models import Control
from weekend.models import weekend
from holiday.models import holiday
from datetime import date, timedelta

# Create your views here.
def adduserNameToModel(serializer):
    if str(type(serializer.data))=="<class 'rest_framework.utils.serializer_helpers.ReturnList'>":
        for leave in serializer.data:
            lv= LeaveRequest.objects.get(id = leave['id'])
            if lv.user !=None:
                leave['UserFullName'] =lv.user.firstname + ' ' + lv.user.lastname
        return True
    else:
        leave = serializer.data
        lv= LeaveRequest.objects.get(id = leave['id'])
        if lv.user !=None:
            leave['UserFullName'] = lv.user.firstname + ' ' + lv.user.lastname
        return leave
#check if current Leave Request Can be made or not.
def CanMakeLeaveRequest(request):
    weekendDaysInLeaveRequest=[]
    allLeaveRequestDaysStr = []
    allLeaveRequestDaysDate = {}
    holydaysInLeaveRangeStr = []
    holydaysInLeaveRangeDates ={}
    ReachMaxNumOfLeave = False
    countDaysOfLeave = 0
    start_date = request.validated_data['startDate']
    end_date = request.validated_data['endDate']
    CountLeaveRequestDays = (end_date - start_date).days
    try:
        weekenddays = weekend.objects.first()
        holydays = holiday.objects.all().filter(startDate = request.validated_data['startDate'])
        #get all user's leaveRequests which is accepted in one year
        leaveForUser = LeaveRequest.objects.all().filter(user = request.validated_data['user'],status = 'accepted')
        requestYear= date.today().year
        ##
        leaveForUser.get(startDate__year = requestYear)
    except weekend.DoesNotExist:
        return Bad_Response(data="Create Weekend Days First")
    except holiday.DoesNotExist:
        holydaysInLeaveRangeDates = {}
    except LeaveRequest.DoesNotExist:
        leaveForUser = []
    
    #count num of leave request day user take in this one year
    if len(leaveForUser)>0:
        for leave in leaveForUser:
            countDaysOfLeave +=int(leave.numOfDay)

    #check if user reach max numOfLeaveRequest in one year
    if countDaysOfLeave==int(Control.objects.first().numOfLeaveRequest):
        ReachMaxNumOfLeave = True
    else:
        ReachMaxNumOfLeave= False

    #GET all leaveRequests Days in string and date
    a = 0
    for day in range(CountLeaveRequestDays):
        allLeaveRequestDaysStr.append(str.lower((start_date+timedelta(days=day)).strftime("%A")))
        allLeaveRequestDaysDate[f'day{a}']=start_date+timedelta(days=day)
        a+=1

    #how many days of leaveRequest are weekend?
    if len(weekendDaysInLeaveRequest)>0:
        for v in allLeaveRequestDaysStr:
            print(v)
            if v =='saturday' and weekenddays.saturday:
                weekendDaysInLeaveRequest.append(weekenddays.saturday)
                break
            elif  v =='sunday' and weekenddays.sunday:
                weekendDaysInLeaveRequest.append(weekenddays.sunday)
                break
            elif  v =='monday' and weekenddays.monday:
                weekendDaysInLeaveRequest.append(weekenddays.monday)
                break
            elif  v =='tuesday' and weekenddays.tuesday:
                weekendDaysInLeaveRequest.append(weekenddays.tuesday)
                break
            elif  v =='wednesday' and weekenddays.wednesday:
                weekendDaysInLeaveRequest.append(weekenddays.wednesday)
                break
            elif  v =='thursday' and weekenddays.thursday:
                weekendDaysInLeaveRequest.append(weekenddays.thursday)
                break
            elif  v =='friday' and weekenddays.friday:
                weekendDaysInLeaveRequest.append(weekenddays.friday)
                break

    #get  all holidays that start with same time of leave request startdate
    for h in holydays:
        holydaysInLeaveRangeDates[f'holyday'] = {'startDate':h.startDate,'endDate':h.endDate}
        break
    
    #how many days of leaveRequest are holyday?
    if len(holydaysInLeaveRangeDates)>0:
        for leaveRequestDay in allLeaveRequestDaysDate:
            if allLeaveRequestDaysDate[leaveRequestDay] >=holydaysInLeaveRangeDates[f'holyday']['startDate'] or allLeaveRequestDaysDate[leaveRequestDay] <=holydaysInLeaveRangeDates[f'holyday']['endDate']:
                holydaysInLeaveRangeStr += leaveRequestDay
                break

    #can make leave-request if leaveRequest date is not in (holyday,weekend) or it isn't reachmaxleaverequest.   
    hasHolyday = False if len(holydaysInLeaveRangeStr)==0 else True
    hasWeekend = False if len(weekendDaysInLeaveRequest)==0 else True
    canMakeLeaveRequest = hasHolyday or hasWeekend or ReachMaxNumOfLeave
    if canMakeLeaveRequest:
        return False
    else:
        return True

@api_view(['POST','GET'])
def LeaveRequestGP(request):
    try:
        leaveRequests = LeaveRequest.objects.all()
        # print(leaveRequests.typeOfLeave)
    except:
        return Bad_Response(From="Get all Leave Requests")
    if request.method =='GET':
        serializer= LeaveRequestSerializer(instance=leaveRequests,many=True)
        adduserNameToModel(serializer)
        return Ok_Response(data=serializer.data)
    elif request.method == 'POST':
        deserializer = LeaveRequestSerializer(data=request.data)
        if deserializer.is_valid():
            if CanMakeLeaveRequest(deserializer):
                if leaveRequests.filter(user = deserializer.validated_data['user'],status='pending').exists() !=True:
                    deserializer.validated_data['status'] = 'pending'
                    deserializer.save()
                    return Created_Response()
                else:
                    return Bad_Response(data="Cancel old pending Leave Request,So You can make another")
            else:
                return Bad_Response(data=f"Leave Request is in Holyday,Weekend,or reach Max Number of Leave Request This Year Which is {Control.objects.first().numOfLeaveRequest}")
        else:
            return Bad_Response(data=deserializer.errors)
    else:
        return Bad_Response(From="Request")

@api_view(['PUT','GET','DELETE'])
def LeaveRequest_pk(request,pk):
    try:
        LeaveReq = LeaveRequest.objects.get(pk=pk)
    except:
        return Bad_Response(From="GET The Leave Request")
    if request.method =='GET':
        desrializer = LeaveRequestSerializer(LeaveReq)
        lv = adduserNameToModel(desrializer)
        return Ok_Response(data=lv)
    elif request.method =='PUT':
        desrializer = LeaveRequestUpdateSerializer(request.data)
        if desrializer.is_valid():
            desrializer.save()
            return No_Content_Response()
        else:
            return Bad_Response(data=desrializer.errors)
    elif request.menthod == 'DELETE':
        LeaveReq.delete()
        return No_Content_Response()
    else:
        return Bad_Response(From="Request")


@api_view(['POST'])
def GetUserLeaveRequest(request):
    def checkDateAndAttribute():
        hasAttrs = True if (int(str(request.body).find("user"))>0 and int(str(request.body).find("startDate"))>0 and int(str(request.body).find("endDate"))>0) else False
        fromLess = True if request.data['endDate'] >request.data['startDate'] else False
        noError = hasAttrs and fromLess
        return True if noError==True else False
    try:
        if checkDateAndAttribute() ==False:
            return Bad_Response(data={"user":"require id or null","startDate":["required","startDate Must Be Greater Than Or Equal endDate"],"endDate":"date required"})
        isUserNotNull = True if request.data['user']!=None else False
        if isUserNotNull:
            userLeaveReq = LeaveRequest.objects.all().filter(user=request.data['user'],startDate__range=[request.data['startDate'],request.data['endDate']])
        else:
            userLeaveReq = LeaveRequest.objects.all().filter(startDate__range=[request.data['startDate'],request.data['endDate']])
    except:
        return Bad_Response(From="GET User Leave Requests")
    serializer = LeaveRequestSerializer(instance= userLeaveReq,many=True)
    adduserNameToModel(serializer)
    return Ok_Response(data=serializer.data)