import sender_stand_request
import data

# Esta función nos devuelve el authToken de un usuario nuevo
def get_new_user_token():
    # 1. Creamos el usuario
    user_response = sender_stand_request.post_new_user(data.user_body)
    # 2. Extraemos el token del cuerpo de la respuesta
    return user_response.json()["authToken"]

# Función base para cambiar el nombre del kit en el cuerpo de la solicitud
def get_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = name
    return current_kit_body


# Para pruebas donde esperamos éxito (201)
def positive_assert(name):
    kit_body = get_kit_body(name)
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    assert response.status_code == 201
    assert response.json()["name"] == name


# Para pruebas donde esperamos error (400)
def negative_assert_code_400(name):
    kit_body = get_kit_body(name)
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    assert response.status_code == 400


# Prueba 1: El número permitido de caracteres (1)
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert(data.one_letter_name)


# Prueba 2: El número permitido de caracteres (511)
def test_create_kit_five_hundred_eleven_letter_in_name_get_success_response():
    positive_assert(data.five_hundred_eleven_letter_name)

# Prueba 3: El número de caracteres es menor que la cantidad permitida (0)
def test_create_kit_minor_to_0_letter_name_get_error_response():
    # Usamos la función de aserción negativa pasándole el dato desde data.py
    negative_assert_code_400(data.zero_letter_name)

# Prueba 4: El número de caracteres es mayor que la cantidad permitida (512)
def test_create_kit_512_letter_name_get_error_response():
    # Optimizamos llamando a la función que ya valida el status 400
    negative_assert_code_400(data.five_hundred_twelve_letter_name)

# Prueba 5: Se permiten caracteres especiales
def test_create_kit_special_characters_in_name_get_success_response():
    positive_assert(data.special_characters_name)

# Prueba 6: Se permiten espacios
def test_create_kit_spaces_are_permitted_in_name_get_success_response():
    positive_assert(data.spaces_name)

# Prueba 7: Se permiten números
def test_create_kit_numbers_in_name_get_success_response():
    positive_assert(data.numbers_name)


# Prueba 8: El parámetro "name" no se pasa en la solicitud
def test_create_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")

    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    # El requisito pide 400, si llega 500, la prueba falla correctamente
    assert response.status_code == 400

# Prueba 9: Se ha pasado un tipo de parámetro diferente (número)
def test_create_kit_different_parameter_type_get_error_response():
    # Usamos la variable con valor numérico definida en data.py
    negative_assert_code_400(data.numbers_name)