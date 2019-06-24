import controller as c
import view as v
import city as city

_city = city.City()
view = v.View(_city)
ctrl = c.Controller(_city, view)
ctrl.start()