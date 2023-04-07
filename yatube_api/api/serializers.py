from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from posts.models import Comment, Post, Group, Follow, User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        fields = '__all__'
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Group


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        read_only_fields = ('post', 'author',)
        fields = '__all__'
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        read_only=False,
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        fields = '__all__'
        model = Follow
        validators = (
            serializers.UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following',),
            ),
        )

    def validate(self, attrs):
        if self.context['request'].user == attrs['following']:
            raise serializers.ValidationError(
                'Вы не можете подписаться на самого себя'
            )
        return attrs
