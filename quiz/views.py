import secrets
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Quiz, Result, Rank


def index(request):
    """Главная страница."""
    return render(request, 'quiz/index.html')


def profile(request):
    return render(request, 'quiz/profile.html')


def quiz_list(request):
    """Список тестов"""
    quizzes = Quiz.objects.all()

    context = {
        'quizzes': quizzes
    }

    return render(request, 'quiz/test.html', context=context)


def quiz_detail(request, slug):
    """Детальная страница теста."""
    quiz = get_object_or_404(Quiz, slug=slug)

    context = {
        'quiz': quiz
    }

    return render(request, 'quiz/healtest.html', context=context)


def get_result(request, code):
    """Получение результата по code"""
    info = get_object_or_404(Result, code=code)
    quiz = get_object_or_404(Quiz, id=info.quiz_id)

    # Найдите соответствующий ранг для данной мощности
    result = Rank.objects.filter(quiz=quiz, min_power__lte=info.value, max_power__gte=info.value).first()

    context = {
        'result': result,
        'quiz': quiz
    }

    return render(request, 'quiz/result.html', context=context)


@require_POST
def result_create(request):
    """Получение результата, добавление кода и перенаправление на показ результата
    quizId - id теста
    power - мощность ответа
    """
    try:
        quiz = int(request.POST.get('quizId'))
        power = int(request.POST.get('power'))

        # Найдите тест по его ID
        quiz = get_object_or_404(Quiz, id=quiz).id

        # Сохранение результата в бд
        code = secrets.token_hex(5)
        Result.objects.create(code=code, quiz_id=quiz, value=power)

        return JsonResponse({'status': 'ok', 'code': code})
        # return redirect('result', code=code)
    except ValueError:
        # if None in (quiz_id, power) and not isinstance(power, str):
        return JsonResponse({'status': 'error'})
    except Exception as e:
        # print(e)
        return JsonResponse({'status': 'error'})
