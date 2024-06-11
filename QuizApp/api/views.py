from rest_framework import generics, filters
from .serializers import QuizListSerializer, QuestionsSerializer, CategorySerializer , QuizDetailSerializer, QuizCreateSerializer, UserEmailSerializer
from rest_framework.views import APIView
from QuizApp.models import Question, Quizzes, Category, UserEmail
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsAuthorOrReadOnly, IsAdminOrReadOnly


class CategoryView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class QuizList(generics.ListAPIView):
    queryset = Quizzes.objects.all()
    serializer_class = QuizListSerializer
    permission_classes = [IsAuthorOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['categories']
    search_fields = ['title']

class QuizCreateView(generics.CreateAPIView):
   
    serializer_class = QuizCreateSerializer
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user) 

class QuizDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthorOrReadOnly]
    lookup_field = 'pk'
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        quiz = Quizzes.objects.get(pk=pk)
        serializer = QuizDetailSerializer(quiz, context={'request': request})
        return Response(serializer.data)

class Questions(APIView):
    def get(self, request, format=None, **kwargs):
        quiz_id = self.kwargs.get('quiz_id')
        questions = Question.objects.filter(quiz_id=quiz_id)
        serializer = QuestionsSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request, **kwargs):
        quiz_id = self.kwargs.get('quiz_id')
        if request.user.is_authenticated:
            email = request.user.email
        else:
            email = request.data.get('email')
        result = request.data.get('result')
        
        try:
            user_email = UserEmail.objects.get(email=email)
            user_email.result = result
            user_email.save()

            serializer = UserEmailSerializer(user_email)
            quiz = Quizzes.objects.get(pk=quiz_id)
            quiz.enrollers = quiz.enrollers +1 
            if user_email.result > 0.8:
                quiz.achievement = quiz.achievement + 1
            else:
                quiz.achievement = quiz.achievement
            quiz.save()
            return Response({ 'response' :"GREAT!, We will send you an email with your results"})
        except UserEmail.DoesNotExist:
            data = {'email': email, 'result': result}
            serializer = UserEmailSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({ 'response' :"GREAT!, We will send you an email with your results"})
            return Response(serializer.errors)
