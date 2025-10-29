from dotenv import load_dotenv
import os
import deepl

load_dotenv()

auth_key = os.getenv("API_KEY")
deepl_client = deepl.DeepLClient(auth_key)

input_path = os.getenv("INPUT_PATH")
output_path = os.getenv("OUTPUT_PATH")
try:
    deepl_client.translate_document_from_filepath(input_path, output_path, target_lang="EN-GB")

except deepl.DocumentTranslationException as error:
    doc_id = error.document_handle.id
    doc_key = error.document_handle.key
    print(f"Error after uploading ${error}, id: ${doc_id} key: ${doc_key}")

except deepl.DeepLException as error:
    print(error)