# -*- coding: utf-8 -*-
"""자율과정-토트넘 선수 전력분석.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A3BzEbyJ-drN6yL01J9M3MrUTdZt5Jqi
"""

from IPython.core.prefilter import PrefilterError
# 22-23 시즌 토트넘 소속 선수 전력분석
import pandas as pd
import matplotlib.pyplot as plt

url = ''
def stat(name):
  if name == '손흥민':
    url = "https://www.espn.com/soccer/player/stats/_/id/149945/son-heung-min"
  elif name == '요리스':
    url = 'https://www.espn.com/soccer/player/stats/_/id/43372/hugo-lloris'
  elif name == '포스터':
    url = 'https://www.espn.com/soccer/player/stats/_/id/93193/fraser-forster'
  elif name == '산체스':
    url = 'https://www.espn.com/soccer/player/stats/_/id/197105/davinson-sanchez'
  elif name == '로얄':
    url = 'https://www.espn.com/soccer/player/stats/_/id/246844/emerson-royal'
  elif name == '다이어':
    url = 'https://www.espn.com/soccer/player/stats/_/id/155532/eric-dier'
  elif name == '로메로':
    url = 'https://www.espn.com/soccer/player/stats/_/id/96970/cristian-romero'
  elif name == '포로':
    url = 'https://www.espn.com/soccer/player/stats/_/id/268533/pedro-porro'
  elif name == '탕강가':
    url = 'https://www.espn.com/soccer/player/stats/_/id/256912/japhet-tanganga'
  elif name == '벤데이비스':
    url = 'https://www.espn.com/soccer/player/stats/_/id/6327/ben-davies'
  elif name == '스킵':
    url = 'https://www.espn.com/soccer/player/stats/_/id/261448/oliver-skipp'
  elif name == '호이비에르':
    url = 'https://www.espn.com/soccer/player/stats/_/id/159543/pierre-emile-hojbjerg'
  elif name == '페리시치':
    url = 'https://www.espn.com/soccer/player/stats/_/id/103485/ivan-perisic'
  elif name == '세세뇽':
    url = 'https://www.espn.com/soccer/player/stats/_/id/241328/ryan-sessegnon'
  elif name == '클루셉스키':
    url = 'https://www.espn.com/soccer/player/stats/_/id/272695/dejan-kulusevski'
  elif name == '사르':
    url = 'https://www.espn.com/soccer/player/_/id/297337/pape-matar-sarr'
  elif name == '벤탕쿠르':
    url = 'https://www.espn.com/soccer/player/_/id/215772/rodrigo-bentancur'
  elif name == '비수마':
    url = 'https://www.espn.com/soccer/player/stats/_/id/232810/yves-bissouma'
  elif name == '히샤를리송':
    url = 'https://www.espn.com/soccer/player/stats/_/id/156799/richarlison'
  elif name == '케인':
    url = 'https://www.espn.com/soccer/player/stats/_/id/142200/harry-kane'
  elif name == '단주마':
    url = 'https://www.espn.com/soccer/player/stats/_/id/43372/hugo-lloris'
  elif name == '모우라':
    url = 'https://www.espn.com/soccer/player/stats/_/id/130711/lucas-moura'
  else:
    print('그런 사람은 존재하지 않습니다.')



  tables = pd.read_html(url)
  print(tables[1])
  print("======================================================================")
  print('STRT: Starts, FC: Fouls Committed, FA: Fouls Suffered, YC: Yellow Cards, RC: Red Cards,\nG: Total Goals, A: Assists, SH: Shots, ST: Shots on Target, OF: Offsides')

  x=[]
  for i in range(len(tables[0].season)):
    x.append(tables[0].season[i][2:8])

  y1 = tables[1].G
  y2 = tables[1].A
  y3 = tables[1].SH
  y4 = tables[1].ST
  y5 = tables[1].STRT


  fig, ax = plt.subplots(2, 2, sharex = True)

  plt.subplot(2,2,1)
  bar1 = plt.bar(x, y1)
  for rect in bar1:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%i' % height, ha='center', va='bottom', size = 6)
  plt.title('Goals', size = 8)
  plt.xticks(x, fontsize = 6)
  plt.yticks(y1, fontsize = 6)

  plt.subplot(2,2,3)
  bar2 = plt.bar(x, y2)
  for rect in bar2:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%i' % height, ha='center', va='bottom', size = 6)
  plt.title('Assists', size = 8)
  plt.xticks(x, fontsize = 6)
  plt.yticks(y2, fontsize = 6)

  plt.subplot(2,2,2)
  bar3 = plt.bar(x, y3, label = 'Shots')
  bar4 = plt.bar(x, y4, label = 'Shots on Target')
  for rect in bar3:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%i' % height, ha='center', va='bottom', size = 6)
  for rect in bar4:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%i' % height, ha='center', va='bottom', size = 6)
  plt.title('Shots and Shots on Target', size = 8)
  plt.legend(fontsize = 6)
  plt.xticks(x, fontsize = 6)
  plt.yticks(y3, fontsize = 6)
  plt.yticks(y4, fontsize = 6)

  plt.subplot(2,2,4)
  bar5 = plt.bar(x, y5)
  for rect in bar1:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%i' % height, ha='center', va='bottom', size = 6)
  plt.title('Starts', size = 8)
  plt.xticks(x, fontsize = 6)
  plt.yticks(y5, fontsize = 6)



  plt.suptitle('analysis')
  fig.supxlabel('seasons')
  plt.tight_layout
  plt.show()

a = input('분석할 선수의 이름을 입력하시오: ')
stat(a)

import pandas as pd
import matplotlib.pyplot as plt

url = ''

def stat(name):
    global url  # url을 전역 변수로 사용하기 위해 global 선언

    if name == '손흥민':
        url = "https://www.espn.com/soccer/player/stats/_/id/149945/son-heung-min"
    elif name == '요리스':
        url = 'https://www.espn.com/soccer/player/stats/_/id/43372/hugo-lloris'
    elif name == '포스터':
        url = 'https://www.espn.com/soccer/player/stats/_/id/93193/fraser-forster'
    # 나머지 코드 생략...

    tables = pd.read_html(url)

    # 그래프 그리는 코드
    fig, axs = plt.subplots(2, 2)

    bar1 = axs[0, 0].bar(tables[0].season[2:], tables[1].G[2:])
    axs[0, 0].set_title('Goals', loc='right')

    bar2 = axs[1, 0].bar(tables[0].season[2:], tables[1].A[2:])
    axs[1, 0].set_title('Assists', loc='right')

    bar3 = axs[0, 1].bar(tables[0].season[2:], tables[1].SH[2:])
    axs[0, 1].bar(tables[0].season[1:], tables[1].ST[1:])
    axs[0, 1].set_title('Shots and Shots on Target', loc='right')

    bar4 = axs[1, 1].bar(tables[0].season[2:], tables[1].STRT[2:])
    axs[1, 1].set_title('Starts', loc='right')

    for rect in bar1:
        height = rect.get_height()
        axs[0, 0].text(rect.get_x() + rect.get_width()/2.0, height, '%i' % height, ha='center', va='bottom', size=8)

    for rect in bar2:
        height = rect.get_height()
        axs[1, 0].text(rect.get_x() + rect.get_width()/2.0, height, '%i' % height, ha='center', va='bottom', size=8)

    for rect1, rect2 in zip(bar3, bar4):
        height1 = rect1.get_height()
        height2 = rect2.get_height()
        axs[0, 1].text(rect1.get_x() + rect1.get_width()/2.0, height1, '%i' % height1, ha='center', va='bottom', size=8)
        axs[0, 1].text(rect2.get_x() + rect2.get_width()/2.0, height2, '%i' % height2, ha='center', va='bottom', size=8)

    # x축 눈금과 라벨 설정
    axs[0, 0].set_xticks(range(len(tables[0].season[2:])))
    axs[0, 0].set_xticklabels(list(tables[0].season[2:]), rotation=45)
    axs[1, 0].set_xticks(range(len(tables[0].season[2:])))
    axs[1, 0].set_xticklabels(list(tables[0].season[2:]), rotation=45)
    axs[0, 1].set_xticks(range(len(tables[0].season[2:])))
    axs[0, 1].set_xticklabels(list(tables[0].season[2:]), rotation=45)
    axs[1, 1].set_xticks(range(len(tables[0].season[2:])))
    axs[1, 1].set_xticklabels(list(tables[0].season[2:]), rotation=45)

    fig.suptitle('Analysis')
    plt.tight_layout()
    plt.show()
