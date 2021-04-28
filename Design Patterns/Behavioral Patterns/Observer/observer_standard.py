
from abc import ABC, abstractmethod


class IObservable(ABC):
  def __init__(self):
      self.__observers = []

  def subscribe(self, observer):
      self.__observers.append(observer)

  def unsubscribe(self, observer):
      self.__observers.remove(observer)

  def notify (self):
      for observer in self.__observers:
          observer.update()

class Person(IObservable):
  def __init__(self, age=0):
    super().__init__()
    self._age = age

  @property
  def age(self):
    return self._age

  @age.setter
  def age(self, value):
    if self._age == value:
      return
    self._age = value
    self.notify()
    # for ta in self.property_changed:
    #   ta.person_changed(value)
    # self.property_changed('age', value)

class IObserver(ABC):
    @abstractmethod
    def update(self): pass

class TrafficAuthority(IObserver):
  def __init__(self, person):
    self.person = person
    person.subscribe(self)

  def update(self):
      self.person_changed(self.person.age)

  def person_changed(self, value):
      if value < 16:
        print('Sorry, you still cannot drive')
      else:
        print('Okay, you can drive now')
        self.person.unsubscribe(self)
        # self.person.property_changed.remove(
        #   self
        # )

class Bundesministerium(IObserver):
  def __init__(self, person):
    self.person = person
    person.subscribe(self)

  def update(self):
      self.person_changed(self.person.age)

  def person_changed(self, value):
      if value < 18:
        print('Nicht wehrdiensttauglich')
      else:
        print('Wehrdiensttauglich')
        self.person.unsubscribe(self)

if __name__ == '__main__':
  p = Person()
  # ta = TrafficAuthority(p)
  bm = Bundesministerium(p)
  for age in range(14, 20):
    print(f'Setting age to {age}')
    p.age = age