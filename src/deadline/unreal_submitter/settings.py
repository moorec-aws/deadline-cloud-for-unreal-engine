#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
import os

TEMPLATES_DIRECTORY = f"{os.path.dirname(__file__)}/templates".replace("\\", "/")

DEFAULT_JOB_TEMPLATE_FILE_NAME = "default_unreal_job_template_v07.yaml"
DEFAULT_JOB_TEMPLATE_FILE_PATH = f"{TEMPLATES_DIRECTORY}/{DEFAULT_JOB_TEMPLATE_FILE_NAME}"

DEFAULT_JOB_STEP_TEMPLATE_FILE_NAME = "default_unreal_step_template_v06.yaml"
DEFAULT_JOB_STEP_TEMPLATE_FILE_PATH = f"{TEMPLATES_DIRECTORY}/{DEFAULT_JOB_STEP_TEMPLATE_FILE_NAME}"
