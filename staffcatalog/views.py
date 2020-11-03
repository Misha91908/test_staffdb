import statistics
from django.http import Http404
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from .models import Person, Alphabet
from django.views import generic


class PersonListView(generic.ListView):
    model = Person
    paginate_by = 40


class PersonDetailView(generic.DetailView):
    model = Person


class AlphabetListView(generic.ListView):
    model = Alphabet
    letters = [[['ABCDEFGHIJKLMNOPQRSTUVWXYZ']],
               [['ABCDEFGHIJKLM'], ['NOPQRSTUVWXYZ']],
               [['ABCDEFGHI'], ['JKLMNOPQR'], ['STUVWXYZ']],
               [['ABCDEFG'], ['HIJKLMN'], ['OPQRSTU'], ['VWXYZ']],
               [['ABDCE'], ['FGHIJ'], ['KLMNO'], ['PQRST'], ['UVWXYZ']],
               [['ABCD'], ['EFGH'], ['IJKL'], ['MNOP'], ['QRST'], ['UVWXYZ']],
               [['ABCD'], ['EFGH'], ['IJKL'], ['MNOP'], ['QRST'], ['UVWX'], ['YZ']]]
    _letters = []
    first_letters = []

    def get_queryset(self):
        Alphabet.objects.all().delete()

        all_last_names = list(dict.fromkeys(Alphabet.objects.values_list('last_name', flat=True)))
        all_last_names.sort()

        is_visible_field = []
        all_last_names_sorted = []

        all_last_names_count = []
        stdev = []
        for i in reversed(range(7)):
            for j in range(i + 1):
                all_last_names_sorted.append([])
                for last_name in all_last_names:
                    if last_name[0] in self.letters[i][j][0]:
                        all_last_names_sorted[j].append(last_name)
            for j in range(i + 1):
                all_last_names_count.append(len(all_last_names_sorted[j]))
            if i > 0:
                stdev.append(statistics.stdev(all_last_names_count))
            else:
                stdev.append(float('inf'))
            all_last_names_count.clear()
            all_last_names_sorted.clear()

        stdev_min = float('inf')
        min_index = 0
        for i in range(len(stdev)):
            if stdev[i] < stdev_min:
                stdev_min = stdev[i]
                min_index = len(stdev) - i - 1

        for i in range(len(self.letters)):
            self._letters.append(self.letters[min_index][i][0][0] + '-' + self.letters[min_index][i][-1][-1])

        for last_name in all_last_names:
            self.first_letters.append(last_name[0])
            if last_name[0] in self.letters[min_index][0][0]:
                is_visible_field.append(True)
            else:
                is_visible_field.append(False)
        for i in range(len(all_last_names)):
            Alphabet.objects.create(id=i, last_name=all_last_names[i], is_visible=is_visible_field[i])

        return Alphabet.objects.all()

    def get_context_data(self, **kwargs):
        context = super(AlphabetListView, self).get_context_data(**kwargs)
        context['letters'] = self._letters
        return context


class AlphabetDetailView(generic.DetailView):
    model = Alphabet
    slug_field = 'last_name'
    slug_url_kwarg = 'last_name'

    def get_context_data(self, **kwargs):
        context = super(AlphabetDetailView, self).get_context_data(**kwargs)
        context['persons'] = Person.objects.filter(last_name=self.object.last_name)
        return context


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_employees = Person.objects.all().count()

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_employees': num_employees},
    )