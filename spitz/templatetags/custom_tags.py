from django import template
import random
from django.contrib.sessions.models import Session

register = template.Library()

@register.filter
def random_image(lst):
    lst = list(lst.split(','))
    return random.choice(lst)

@register.filter
def format_tags(tags):
    tags = tags.replace(" или", "").replace("(", "").replace(")", "").split()
    tags = list(dict.fromkeys(tags))
    return ", ".join(tags)

@register.simple_tag
def random_fact():
    lst = [
        "Есть легенда, по которой волхвы пришли поклониться Иисусу в компании шпицев (об этом говорится в книге о породе авторства Алисы Гатакре).",
        "Само название породы переводится с немецкого как «острый».",
        "Когда порода только начала развиваться, эти собаки были крупнее и жили у бедняков, помогая им охранять стада. Это потом, через 100 лет, они переселятся из лачуг в королевские покои и станут любимыми «игрушками» у знати.",
        "Померанский шпиц был у Исаака Ньютона, того самого, что открыл закон всемирного тяготения. Однажды пес (его звали Даймонд) опрокинул свечу, и на столе загорелись ценнейшие рукописи. Но Ньютон не ругал своего пса даже за это, ведь он сильно его любил.",
        "Много голливудских звезд, актрис, певиц и даже спортсменок выбирают себе этих милашек в качестве компаньонов. Некоторые даже заводят сразу по 2-3 собаки. Среди поклонников породы – Кристен Стюард из «Сумерек», теннисистка Мария Шарапова, Юлия Началова и Шерон Осборн, Николь Ричи и Ева Лонгория.",
        "Если вам кажется, что такие песики подходят только девушкам, вы ошибаетесь. Так, шпицы живут у Микки Рурка и Сильвестра Сталлоне. Мужчинам тоже приятна такая компания! Кстати, этих собачек вполне оправданно называют «маленькими Наполеонами» за решительных характер.",
        "В рассказах «Дама с собачкой» и «Легенда об Уленшпигеле» говорится как раз о питомцах этой породы.",
        "Несмотря на свой небольшой размер, «померанцы» очень умные. Они прекрасно поддаются дрессировке и могут выполнять даже сложную работу. Например, известны случаи, когда шпицы работали спасателями.",
        "С тонущего «Титаника» спаслось всего 3 собаки, и две из них – были именно шпицы (они принадлежали Ротшильдам)."
    ]
    return random.choice(lst)

@register.simple_tag
def get_session_counter():
    return len(Session.objects.all())
