## Вопрос 1

Ответ: 1896

## Вопрос 2

Ответ: Athletics

## Вопрос 3

Ответ: Soviet Union

## Вопрос 4

Ответ: 21

## Вопрос 5

(неуверен ТК странно, чуть-чуть попозже с код перечитаю и может быть исправлю)

Ответ: 0

## Вопрос 6

Ответ: 24

## Вопрос 7

Ответ:

```python
def medal_weight(medal):
	if medal == 'Gold':
		return 3
	elif medal == 'Silver':
		return 2
	elif medal == 'Bronze':
		return 1
	else:
		return 0


df['MedalWeight'] = df['Medal'].apply(medal_weight)

print(df[['Medal', 'MedalWeight']].head())
```

## Вопрос 8

Ответ:

```python
olmp['Medal_score'] = olmp['Medal'].apply(medal_weight)
```

## Вопрос 9

Ответ: числовой дискретный

## Вопрос 10

Ответ: Michael Fred Phelps, II