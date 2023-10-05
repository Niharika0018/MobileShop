from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View
from django.contrib.auth.hashers import check_password
from shop.models.customer import Customer

class Login(View):

    def get(self, request):
        # Login.return_url = request.GET.get('return_url')
        # print('*************', Login.return_url)
        return render(request, 'login.html')
    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message=None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                # print('1111111111111', Login.return_url)
                # if Login.return_url:
                #     print('22222222222', Login.return_url)
                #     return HttpResponseRedirect(Login.return_url)
                # else:
                #     print('3333333333333', Login.return_url)
                #     Login.return_url = None
                return redirect('homepage')
            else:
                error_message = 'Invalid !!'
        else:
            error_message = 'Invalid !!'

        print(email, password)
        return render(request, 'login.html', {'error': error_message})

def logout(request):
    request.session.clear()
    return redirect('login')