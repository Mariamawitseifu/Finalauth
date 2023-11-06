from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer
from datetime import datetime
from records.models import CustomUser
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
def post_list(request):
    queryset = Post.objects.all()
    serializer = PostSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def post_detail(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_post(request):
    # request.data['published_date'] = datetime.now()  # Set the current date
    serializer = PostSerializer(data=request.data)
    
   

    print(request.data)
    
    if serializer.is_valid():
        # author = CustomUser.objects.get(username=request.user.username) 
        # print(author)# Assuming username is used for authentication
        print(request.user)
        serializer.save(author=CustomUser.objects.get(username=request.user.username))
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def delete_all_posts(request):
    Post.objects.all().delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def delete_post(request, id):
    try:
        post = Post.objects.get(id=id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    