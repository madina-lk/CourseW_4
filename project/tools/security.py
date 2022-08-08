import base64
import hashlib
import jwt
import hmac
from flask import current_app, abort, request
from flask import current_app


def __generate_password_digest(password: str) -> bytes:
    return hashlib.pbkdf2_hmac(
        hash_name="sha256",
        password=password.encode("utf-8"),
        salt=current_app.config["PWD_HASH_SALT"],
        iterations=current_app.config["PWD_HASH_ITERATIONS"],
    )


def generate_password_hash(password: str) -> str:
    return base64.b64encode(__generate_password_digest(password)).decode('utf-8')

# TODO: [security] Описать функцию compose_passwords(password_hash: Union[str, bytes], password: str)


def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]
        try:
            jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=current_app.config['ALGORITHM'])
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)
        return func(*args, **kwargs)

    return wrapper


def admin_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]
        try:
            user = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=current_app.config['ALGORITHM'])
            role = user.get("role")
            if role != "admin":
                abort(400)
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)
        return func(*args, **kwargs)

    return wrapper


def compare_passwords(password_hash, other_password) -> bool:
    return hmac.compare_digest(
        base64.b64decode(password_hash),
        hashlib.pbkdf2_hmac(
            'sha256',
            other_password.encode('utf-8'),
            current_app.config['PWD_HASH_SALT'],
            current_app.config['PWD_HASH_ITERATIONS']
        )
    )


def check_token(token):
    try:
        res_token = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=current_app.config['ALGORITHM'])
        return res_token
    except Exception:
        abort(401)
