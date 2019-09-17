from pandas import read_csv, DataFrame
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Инициализация объектов DataFrame
iris = read_csv('iris.data')
wine = read_csv('wine.data')
zoo = read_csv('zoo.data')
mushrooms = read_csv('mushrooms.data')
car = read_csv('car.data')
# Процедура случайного перемешивания и деления выборки на тестовую и обучающую
wine_sample = DataFrame.sample(wine, frac=1)
wine_train, wine_test = train_test_split(wine_sample, test_size=0.2)

zoo_sample = DataFrame.sample(zoo, frac=1)
zoo_train, zoo_test = train_test_split(zoo_sample, test_size=0.2)

car_sample = DataFrame.sample(car, frac=1)
car_train, university_test = train_test_split(car, test_size=0.2)
# Процедура назначений номеров классов для символьных значений
label = LabelEncoder()
column_with_symbols = None
done = False
for key in iris:
    for q in iris[key]:
        if type(q) == str:
            done = True
            column_with_symbols = key
            break
    if done:
        break
if column_with_symbols is not None:
    label.fit(iris[column_with_symbols].drop_duplicates())
    iris[column_with_symbols] = label.transform(iris[column_with_symbols])
else:
    print('Нету столбцов с символами')


# Процедура замены пропущенных значений
column_with_none = None
done = False
for key in mushrooms:
    for q in mushrooms[key]:
        if q == '?':
            done = True
            column_with_none = key
            break
    if done:
        break

if column_with_symbols is not None:
    mushrooms.dropna(subset=[column_with_none])
    k = mushrooms[column_with_none].value_counts().idxmax()
    mushrooms[column_with_none].replace('?', k, inplace=True)
else:
    print('Нету столбцов с пропущенными значениями')


