from django.shortcuts import render, redirect


def counter(request):
    if request.method == 'POST':
        text = request.POST['texttocount']

        if text != '':
            word = len(text.split())

            i = True

            return render(request, 'counter.html', {'word': word, 'text': text, 'i': i})
        else:
            return render(request, 'counter.html')
    else:
        return render(request, 'counter.html')


def clear(request):
    return redirect('counter')
