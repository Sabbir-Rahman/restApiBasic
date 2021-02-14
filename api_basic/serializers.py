from rest_framework import serializers
from .models import Article

# class ArticleSerializers(serializers.Serializer):
#      title = serializers.CharField(max_length = 100)
#      author = serializers.CharField(max_length = 100)
#      email = serializers.EmailField()
#      date = serializers.DateTimeField()

#     #create 
#     #a = Article(title = 'Another new  one', author = 'Sabbir', email='mdsabbirrahman1998@gmail.com')

#     #show all
#     #serializer = ArticleSerializers(Article.objects.all(), many=True) 


#      def create(self, validated_data):
#          return Article.objects.create(validated_data)

#      def update(self, instance, validated_data):
#          instance.title = validated_data.get('title', instance.title)
#          instance.author = validated_data.get('author', instance.author)
#          instance.email = validated_data.get('email', instance.email)
#          instance.date = validated_data.get('date', instance.date)
#          instance.save()
#          return instance



class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'author', 'email', 'date']

        #printing representation
        #print(repr(serializer))