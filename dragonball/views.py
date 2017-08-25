from django.shortcuts import render, redirect
from .models import Dragonball


# Create your views here.
def main(request):
    for num in range(1,8):
        star=str(num)+'성구'
        Dragonball(dragonball = star, detected = 'Not!!').save()
    return render(request, 'main.html')

def radar(request):
    if request.method=='POST':
        DB_num=request.POST['number']
        DB=Dragonball.objects.filter(dragonball=DB_num).update(detected='detected!!')
        return redirect('location')

    else:
        return render(request, 'radar.html')

#def location(request):
