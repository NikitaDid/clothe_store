from rest_framework import serializers

from apps.blog.models import BlogCategory, Article


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ('id', 'name', 'image')


class ArticleWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'id',
            'category',
            'title',
            'text_preview',
            'text',
            'publish_date',
            'image',
        )


class ArticleReadeSerializer(serializers.ModelSerializer):
    category = BlogCategorySerializer

    class Meta:
        model = Article
        fields = (
            'id',
            'category',
            'user',
            'title',
            'text_preview',
            'text',
            'publish_date',
            'image',
            # 'image_thumbnail',
            'created_at',
        )