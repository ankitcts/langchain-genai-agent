from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
import os

PARAMETERS= {
    GenParams.MAX_NEW_TOKENS : 256,
    GenParams.DECODING_METHOD: 'greedy'
}

CREDENTIALS = {
    "url": "https://us-south.ml.cloud.ibm.com",
    "project_id": "81d82fb8-fca5-4eef-8ec5-36ee556325d2"
}

# Model IDs
LLAMA_MODEL_ID = "meta-llama/llama-3-2-11b-vision-instruct"
GRANITE_MODEL_ID = "ibm/granite-4-h-small"
MISTRAL_MODEL_ID = "mistralai/mistral-small-3-1-24b-instruct-2503"