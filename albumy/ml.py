from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

import os

endpoint = os.environ.get("AZURE_CV_ENDPOINT")
key = os.environ.get("AZURE_CV_KEY")
client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(key))


def generate_alt_text(image_path):
    """Return alt text for an image using Azure Computer Vision"""
    with open(image_path, "rb") as f:
        result = client.describe_image_in_stream(f, max_candidates=1)
    if result.captions:
        return result.captions[0].text
    return "Image"


def detect_objects(image_path):
    """Return list of object tags detected in the image"""
    with open(image_path, "rb") as f:
        analysis = client.analyze_image_in_stream(f, visual_features=[VisualFeatureTypes.objects])
    return [obj.object_property for obj in analysis.objects]
