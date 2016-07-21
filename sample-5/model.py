from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

class RestaurantShop():

    def addRestaurant(self, name):
        newRestaurant = Restaurant(name = name)
        session.add(newRestaurant)
        session.commit()
        print("New restaurant \"" + newRestaurant.name + "\" is added")

    def editRestaurant(self, restaurantid, newName):
        selectedRestaurant = session.query(Restaurant).filter_by(id = restaurantid).one_or_none()
        if selectedRestaurant != []:
            selectedRestaurant.name = newName
            session.add(selectedRestaurant)
            session.commit()
            print("Restaurant ID: " + restaurantid + "'s name was changed to \"" + newName + "\"")

    def deleteRestaurant(self, restaurantid):
        selectedRestaurant = session.query(Restaurant).filter_by(id = restaurantid).one_or_none()
        if selectedRestaurant != []:
            session.delete(selectedRestaurant)
            session.commit()
            print("Restaurant ID: " + restaurantid + " was deleted successfully")
    
    def getRestaurant(self, restaurantid):
        selectedRestaurant = session.query(Restaurant).filter_by(id = restaurantid).one_or_none()
        if selectedRestaurant != []:
            return selectedRestaurant
    
    def listRestaurant(self):
        restaurants = session.query(Restaurant).all()
        return restaurants

class FoodMenu():

    def addFoodMenu(self, name, description, course, price, restaurantId):
        newFoodItem = MenuItem(name = name, description = description, course = course, price = price, restaurant_id = restaurantId)
        session.add(newFoodItem)
        session.commit()
        print("New food item \"" + newFoodItem.name + "\" is added")

    def editFoodMenu(self, menuid, name, description, course, price, restaurantId):
        selectedFoodMenu = session.query(MenuItem).filter_by(id = menuid).one_or_none()
        if selectedFoodMenu != []:
            selectedFoodMenu.name = name
            selectedFoodMenu.description = description
            selectedFoodMenu.course = course
            selectedFoodMenu.price = price
            selectedFoodMenu.restaurant_id = restaurantId
            session.add(selectedFoodMenu)
            session.commit()
            print("Food menu id #" + str(menuid) + " was updated successfully")
        else:
            print("Food menu id #" + str(menuid) + " not found")

    def deleteFoodMenu(self, menuid):
        selectedFoodMenu = session.query(MenuItem).filter_by(id = menuid).one_or_none()
        if selectedFoodMenu != []:
            session.delete(selectedFoodMenu)
            session.commit()
            print("Food menu id #" + str(menuid) + " was deleted successfully")
        else:
            print("Food menu id #" + str(menuid) + " not found")
    
    def getFoodMenu(self, menuid):
        selectedFoodMenu = session.query(MenuItem).filter_by(id = menuid).one_or_none()
        if selectedFoodMenu != []:
            return selectedFoodMenu
    
    def getFoodMenus(self, restaurantid):
        selectedFoodMenus = session.query(MenuItem).filter_by(restaurant_id = restaurantid).all()
        if selectedFoodMenus != []:
            return selectedFoodMenus



'''
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind = engine)
session = DBSession()


# add first restaurant
myFirstRestaurant = Restaurant(name = "Pizza Palace")
session.add(myFirstRestaurant)
session.commit()

firstResult = session.query(Restaurant).first()
#print(firstResult.name)


# add first menu item
cheesepizza = MenuItem(name="Cheese Pizza", description = "Made with all natural ingredients and fresh mozzarella", course="Entree", price="$8.99", restaurant=myFirstRestaurant)
session.add(cheesepizza)
session.commit()

items = session.query(MenuItem).all()
for item in items:
    print item.name


veggieBurgers = session.query(MenuItem).filter_by(name= 'Veggie Burger')
for veggieBurger in veggieBurgers:
    print veggieBurger.id
    print veggieBurger.price
    print veggieBurger.restaurant.name
    print "\n"

UrbanVeggieBurger = session.query(MenuItem).filter_by(id=1).one()
UrbanVeggieBurger.price = '$2.99'
session.add(UrbanVeggieBurger)
session.commit()


spinach = session.query(MenuItem).filter_by(name = 'Cheese Pizza').one()
session.delete(spinach)
session.commit() 


restaurants = session.query(Restaurant).all()
for restaurant in restaurants:
    print restaurant.name 
    print "\n"

burgers = session.query(MenuItem).all()
for burger in burgers:
    print burger.id
    print burger.price
    print burger.restaurant.name
    print "\n"
'''
