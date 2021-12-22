def IsEmployer(request):
    if str(request.user.role.roleName)=="manager":
        return True
    return False
          

def IsManager(request):
    if str(request.user.role.roleName)=="employer":
        return True
    return False