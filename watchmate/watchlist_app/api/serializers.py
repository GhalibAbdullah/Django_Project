from rest_framework import serializers
from watchlist_app.models import Watchlist, StreamingPlatform, Review

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = '__all__'
        
        
class WatchlistSerializer(serializers.ModelSerializer):
    
    reviews = ReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = Watchlist
        fields = "__all__"                          #To disply all fields
        # fields = ["id", "name", "description"]      #To disply only the feilds mentioned
        # exclude = ["active"]                        #To disply every feild except the feild mentioned
        
class StreamingPlatformSerializer(serializers.ModelSerializer):
    
    Watchlist = WatchlistSerializer(many=True, read_only=True)
    
    # Watchlist = serializers.HyperlinkedRelatedField(
    #     many = True,
    #     read_only = True,
    #     view_name = "movie-detail"
    # )
    
    class Meta:
        model = StreamingPlatform
        fields = "__all__"

        
    # def get_len_names(self, obj):
    #     return len(obj.name)
    
    # def validate(self, data):
    #     if  data['name'] == data['description']:
    #         raise serializers.ValidationError("Title and Description should be different :( ")
    #     return data    
    
    # def validate_name(self, value):
    #     if len(value) < 3:
    #         raise serializers.ValidationError("Name is too short :(")
    #     return value
    
    

# def name_length(value):
#     if len(value) < 3:
#         raise serializers.ValidationError("Name is too short :(")
#     return value

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
        
#     def update(self, instance, validated_data): #instance = oldvalue, validated_data = newvalue
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
        
#     def validate(self, data):
#         if  data['name'] == data['description']:
#             raise serializers.ValidationError("Title and Description should be different :( ")
#         return data
    
    
    
        