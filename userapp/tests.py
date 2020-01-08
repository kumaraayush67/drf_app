from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User
from .serializers import UserSerializer

class UserTestCase(APITestCase):
    def setUp(self):
        test_db = [
            {
                "id": 1,
                "first_name": "James",
                "last_name": "Butt",
                "company_name": "Benton, John B Jr",
                "city": "New Orleans",
                "state": "LA",
                "zip": 70116,
                "email": "jbutt@gmail.com",
                "web": "http://www.bentonjohnbjr.com",
                "age": 70
            },
            {
                "id": 2,
                "first_name": "Josephine",
                "last_name": "Darakjy",
                "company_name": "Chanay, Jeffrey A Esq",
                "city": "Brighton",
                "state": "MI",
                "zip": 48116,
                "email": "josephine_darakjy@darakjy.org",
                "web": "http://www.chanayjeffreyaesq.com",
                "age": 48
            },
        ]
        for item in test_db:
            User.objects.create(**item)

    def list_request_test(self):
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def get_request_test(self):
        for obj in User.objects.all():
            url = reverse('user-detail',kwargs={'pk':obj.id})
            serializer_data = UserSerializer(instance=obj).data
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.json(), serializer_data)
    
    def get_invalid_request_test(self):
        invalid_id = 4000 # non existing id
        url = reverse('user-detail',kwargs={'pk':id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def post_request_test(self):
        url = reverse('user-list')
        data = {
            "id": 3,
            "first_name": "Art",
            "last_name": "Venere",
            "company_name": "Chemel, James L Cpa",
            "city": "Bridgeport",
            "state": "NJ",
            "zip": 80514,
            "email": "art@venere.org",
            "web": "http://www.chemeljameslcpa.com",
            "age": 80
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 3) # two object already created
    
    def post_invalid_request_test(self):
        url = reverse('user-list')
        data = {
            "id": "three", # string in place of integer
            "first_name": "Art",
            "last_name": "Venere",
            "company_name": "Chemel, James L Cpa",
            "city": "Bridgeport",
            "state": "NJ",
            "zip": 80514,
            "email": "art@venere.org",
            "web": "http://www.chemeljameslcpa.com",
            "age": 80
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 2) # two object already created
    
    def put_request_test(self):
        obj_id = 1
        url = reverse('user-detail',kwargs={'pk':obj_id})
        data = {
            "first_name": "Art",
            "last_name": "Venere",
            "age": 80
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # to check if user attributes are changed sucessfully
        resultant_data = {
            "id": 1,
            "first_name": "Art",
            "last_name": "Venere",
            "company_name": "Benton, John B Jr",
            "city": "New Orleans",
            "state": "LA",
            "zip": 70116,
            "email": "jbutt@gmail.com",
            "web": "http://www.bentonjohnbjr.com",
            "age": 80
        }
        serializer_data = UserSerializer(instance=User.objects.get(id=obj_id)).data
        self.assertEqual(resultant_data, serializer_data)
    
    def delete_request_test(self):
        obj_id = 1
        url = reverse('user-detail',kwargs={'pk':obj_id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)