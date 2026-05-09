def has_permission(user, required_role):
    return user["role"] == required_role