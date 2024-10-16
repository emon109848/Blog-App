from passlib.context import CryptContext


pass_context = CryptContext(schemes='bcrypt', deprecated = 'auto')

class Hash():
    def bcrypt(password: str):
        return pass_context.hash(password)
    
    def verify(hashed_pass, plain_pass):
        return pass_context.verify(plain_pass,hashed_pass)
