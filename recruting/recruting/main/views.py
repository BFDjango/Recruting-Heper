import logging

from rest_framework import generics, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from recruting.main.models import MyUser, Admin, Manager, Employee
from recruting.main.serializers import MyUserFullSerializer, AdminSerializer, ManagerSerializer, EmployeeSerializer

logger = logging.getLogger('log')


class RegistrationView(APIView):
    def post(self, request):
        passwd = request.data.get('password')
        usr = request.data.get('username')
        serializer = MyUserFullSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        my_user = MyUser.objects.get(username=usr)
        my_user.set_password(passwd)
        my_user.save()
        logger.info(f"{self.request.user} registered into the system")
        logger.warning(f"{self.request.user} registered into the system")
        logger.error(f"{self.request.user} registered into the system")
        logger.critical(f"{self.request.user} registered into the system")
        return Response(serializer.data)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MyUserFullSerializer
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return MyUser.objects.all()

    @action(methods=['GET'], detail=False)
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)


class AdminView(generics.ListAPIView):
    serializer_class = AdminSerializer
    queryset = Admin.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ManagerView(generics.ListAPIView):
    serializer_class = ManagerSerializer
    queryset = Manager.objects.all()

    def get(self, request, *args, **kwargs):
        try:
            if request.user.role == 1:
                return self.list(request, *args, **kwargs)
            else:
                return Response('Permission denied!!!')
        except Exception as e:
            print(e)
            return Response('Please Authorized!!!')


class ManagerDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ManagerSerializer
    queryset = Manager.objects.all()

    def get(self, request, *args, **kwargs):
        try:
            if request.user.role == 1:
                return self.retrieve(request, *args, **kwargs)
            else:
                return Response('Permission denied!!!')
        except Exception as e:
            print(e)
            return Response('Please Authorized!!!')

    def put(self, request, *args, **kwargs):
        try:
            if request.user.role == 1:
                return self.update(request, *args, **kwargs)
            else:
                return Response('Permission denied!!!')
        except Exception as e:
            print(e)
            return Response('Please Authorized!!!')

    def delete(self, request, *args, **kwargs):
        try:
            if request.user.role == 1:
                return self.destroy(request, *args, **kwargs)
            else:
                return Response('Permission denied!!!')
        except Exception as e:
            print(e)
            return Response('Please Authorized!!!')


class EmployeeView(generics.ListAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    def get(self, request, *args, **kwargs):
        try:
            if request.user.role == 1:
                return self.list(request, *args, **kwargs)
            elif request.user.role == 2:
                print('***********')
                manager = Manager.objects.get(user=request.user)
                print(manager.department)
                empl = Employee.objects.filter(position__department=manager.department)
                serializer = EmployeeSerializer(empl, many=True)
                return Response(serializer.data)
            else:
                return Response('Permission denied!!!')
        except Exception as e:
            print(e)
            return Response('Please Authorized!!!')