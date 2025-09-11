from sqlalchemy.ext.asyncio import AsyncSession

class AuthService:
    def __init__(self, session: AsyncSession):
        self.session = session