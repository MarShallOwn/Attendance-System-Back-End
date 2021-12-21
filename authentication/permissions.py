def IsEmployer(request):
    if str(request.user.role)=="f2438952-9698-45b5-8c19-47bc5a1cd1ea":
        return True
    return False
          

def IsManager(request):
    if str(request.user.role)=="1c1a9a99-1498-41cd-a8d6-6292b58867b0":
        return True
    return False