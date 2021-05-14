from django.shortcuts import render

def error_404(request, exception):
        data = {}
        return render(request,'ship_o_cereal/404.html', data)

#def error_500(request,  exception):
 #       data = {}
  #      return render(request,'ship_o_cereal/500.html', data)


def error_400(request, exception):
    data = {}
    return render(request, 'ship_o_cereal/400.html', data)

def error_403(request, exception):
    data = {}
    return render(request, 'ship_o_cereal/403.html', data)