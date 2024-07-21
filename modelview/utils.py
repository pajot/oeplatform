from django.urls import reverse

from modelview.models import Energyframework, Energymodel


def get_url(sheettype, obj_id):
    kwargs = {"sheettype": sheettype, "model_name": obj_id}
    detail_url = reverse(
        "modelview:show-factsheet",
        kwargs=kwargs,
    )
    return detail_url


def get_model_class(model_type: str):
    if model_type == "energymodel":
        return Energymodel
    elif model_type == "energyframework":
        return Energyframework
    else:
        raise ValueError(f"Model type '{model_type}' is not recognized.")


def get_model_metadata_by_id(id_model: int, model_type: str):
    model_class = get_model_class(model_type)
    model_instance = (
        model_class.objects.filter(id=id_model).values("model_name", "acronym").first()
    )

    if model_instance is None:
        return None  # Handle the case when the model is not found

    model_metadata = {
        "id": id_model,
        "name": model_instance["model_name"],
        "acronym": model_instance["acronym"],
        "urn": get_url("framework", id_model),
    }

    return model_metadata


def get_framework_metadata_by_id(id_framework: int, model_type: str):
    model_class = get_model_class(model_type)
    model_instance = (
        model_class.objects.filter(id=id_framework)
        .values("model_name", "acronym")
        .first()
    )

    if model_instance is None:
        return None  # Handle the case when the model is not found

    model_metadata = {
        "id": id_framework,
        "name": model_instance["model_name"],
        "acronym": model_instance["acronym"],
        "urn": get_url("model", id_framework),
    }

    return model_metadata
