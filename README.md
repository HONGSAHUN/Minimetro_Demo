# Minimetro_Demo
Minimetro 모방 게임 제작

## 현재 구현 범위
- 기차 편성 규칙: 최소 2량, 최대 12량
- 객차 정원 규칙: 객차당 최대 100명
- 도시/시스템 모방 확장용 템플릿 제공
  - `Seoul Metro` 템플릿
  - `Tokyo Metro` 템플릿

## 사용 예시
```python
from minimetro import Train, SEOUL_METRO_TEMPLATE

train = Train(car_count=8)
train.board(car_index=0, passengers=100)  # 객차 정원 한도
print(train.max_capacity)  # 800
print(SEOUL_METRO_TEMPLATE)
```
