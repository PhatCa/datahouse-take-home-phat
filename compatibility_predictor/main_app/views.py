from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers.multi_member import MultiMemberSerializer


class ScoringView(APIView):
    def post(self, request):
        serializer = MultiMemberSerializer(data=request.data)
        if serializer.is_valid():
            applicant_list = serializer.validated_data.get('applicants')
            output_list = []
            for applicant in applicant_list:
                name = applicant['name']
                attr = applicant['attributes']
                intelligence = attr['intelligence']
                strength = attr['strength']
                endurance = attr['endurance']
                spicy_food_tolerance = attr['spicyFoodTolerance']
                sorted_list = sorted([
                    intelligence,
                    strength,
                    endurance,
                    spicy_food_tolerance
                    ])
                highest_num = sorted_list[3]
                second_highest_num = sorted_list[2]
                score = round(
                    (highest_num-second_highest_num)/highest_num,
                    1
                )
                applicant_score_dict = {
                    "name": name,
                    "score": score
                }
                output_list.append(applicant_score_dict)
            return Response({
                'output': output_list
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
