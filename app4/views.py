from django.shortcuts import render

# Create your views here.
def vk(request):
  data='this my first web page'
  d={'username':data}
  return render(request,'vk.html',context=d)
def virat(request):
   c={'name':'sreenu','age':23}
   return render(request,'virat.html',context=c)


