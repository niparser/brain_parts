"""
Configurations for *parcellation* pipeline
"""

INPUT_NODE_FIELDS = [
    "base_dir",
    "analysis_type",
    "participant_label",
    "anatomical_reference",
    "mni_to_native_transformation",
    "gm_probability",
    "probability_masking_threshold",
    "parcellation_scheme",
    "parcellation_image",
]

NATIVE_PARCELLATION_NAMING_KWARGS = dict(
    input_names=[
        "base_dir",
        "reference",
        "parcellation_scheme",
        "analysis_type",
    ],
    output_names=["whole_brain", "gm_cropped"],
)

ANTS_APPLY_TRANSFORM_KWARGS = dict(interpolation="NearestNeighbor")

PROBSEG_TO_MASK_KWARGS = dict(direction="below")
CROP_TO_MASK_KWARGS = dict(output_datatype="int")