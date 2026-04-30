import configuration
import requests
import data


# Función para crear un nuevo usuario y obtener la respuesta completa
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


# Función para crear un kit de producto
def post_new_client_kit(kit_body, auth_token):
    # Copiamos los encabezados base y agregamos el token de autorización
    headers_with_token = data.headers.copy()
    headers_with_token["Authorization"] = f"Bearer {auth_token}"

    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=headers_with_token)
