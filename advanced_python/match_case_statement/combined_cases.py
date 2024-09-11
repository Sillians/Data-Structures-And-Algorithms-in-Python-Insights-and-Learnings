def access(user: str) -> str:
    match user.lower():
        case "admin" | "manager": return "Full Access"
        case "Guest": return "Limited Access"
        case "_": return "No access granted"


print(access("Admin"))