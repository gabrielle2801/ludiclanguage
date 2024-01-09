from rest_framework import serializers
from .models import RecorderMessage, Exercise


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('id',
                  'name',
                  'description',
                  'title_game',
                  'description_game',
                  'picture1',
                  'picture2',
                  'therapist',
                  'pathology'
                  )


class RecorderSerializer(serializers.ModelSerializer):

    class Meta:
        model = RecorderMessage
        fields = ('id',
                  'audio_file',
                  'sentence',
                  'exercise',
                  'patient')


'''

 name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    title_game = models.CharField(max_length=500, blank=True)
    description_game = models.TextField(blank=True)
    picture1 = models.ImageField('picture1', blank=True)
    picture2 = models.ImageField('picture2', blank=True)
    therapist = models.ForeignKey(
        'profiles.Profile', on_delete=models.CASCADE,
        related_name='therapist_exercice',
        null=True, blank=True)
    pathology = models.ForeignKey(
        'Pathology', on_delete=models.CASCADE, null=True)

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def create(self, validated_data):
        validated_data['exercise_id'] = self.kwargs['pk']
        return super(RecorderSerializer, self).create(validated_data)
'''
