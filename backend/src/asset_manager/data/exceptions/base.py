class AssetManagerException(Exception):
    message: str

    def __init__(self):
        super().__init__(self.message)


class ItemNotFound(AssetManagerException):
    def __init__(self, id):
        self.id = id
        self.message = f"Item {id} not found"
        super().__init__()


class MethodShouldNotBeImplemented(AssetManagerException):
    def __init__(self, method: str):
        self.method = method
        self.message = f"Method {method} should not be implemented"
        super().__init__()


class AssetHasAssignedException(AssetManagerException):
    def __init__(self, asset_id):
        self.message = f"Asset {asset_id} just have a user!"
        super().__init__()


class UserJustHaveLicenseException(AssetManagerException):
    def __init__(self, license_id, dev_id):
        self.message = (
            f"License({license_id}) has just been assigned to User({dev_id})"
        )
        super().__init__()


class UserJustHaveAssetException(AssetManagerException):
    def __init__(self, dev_id, asset_id):
        self.message = (
            f"Developer {dev_id} just have a this asset ({asset_id})!"
        )
        super().__init__()


class DeveloperInactiveException(AssetManagerException):
    def __init__(self, dev_id):
        self.message = f"Developer {dev_id} is not activated!"
        super().__init__()
