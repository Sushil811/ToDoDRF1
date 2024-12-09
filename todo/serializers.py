from rest_framework import serializers
from .models import ToDoItem, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ToDoItemSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = ToDoItem
        fields = '__all__'

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        todo_item = ToDoItem.objects.create(**validated_data)
        for tag_data in tags_data:
            tag, _ = Tag.objects.get_or_create(name=tag_data['name'])
            todo_item.tags.add(tag)
        return todo_item

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', [])
        instance = super().update(instance, validated_data)
        if tags_data:
            instance.tags.clear()
            for tag_data in tags_data:
                tag, _ = Tag.objects.get_or_create(name=tag_data['name'])
                instance.tags.add(tag)
        return instance
