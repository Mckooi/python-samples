from model import RestaurantShop, FoodMenu
from flask import Flask, render_template, url_for, request, redirect, flash, jsonify
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# making an API Endpoint (GET request)
@app.route('/restaurants/<int:restaurant_id>/menu/JSON')
def restaurantMenuJSON(restaurant_id):
    
    rst = RestaurantShop()
    restaurant = rst.getRestaurant(restaurant_id)

    if restaurant == None:

        return '{}'
    
    mi = FoodMenu()
    foodMenus = mi.getFoodMenus(restaurant.id)

    if foodMenus:

        return jsonify(MenuItems=[item.serialize for item in foodMenus])

    else:

        return '{ "MenuItems": [] }'

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON')
def restaurantMenuItemJSON(restaurant_id, menu_id):
    
    rst = RestaurantShop()
    restaurant = rst.getRestaurant(restaurant_id)

    if restaurant == None:

        return '{}'
    
    mi = FoodMenu()
    foodMenu = mi.getFoodMenu(menu_id)

    if foodMenu:

        return jsonify(MenuItem=foodMenu.serializeMenuItem)

    else:

        return '{ "MenuItems": [] }'

@app.route('/')
@app.route('/hello')
def HelloWorld():
    
    rst = RestaurantShop()
    restaurant = rst.getRestaurant(3)
    
    mi = FoodMenu()
    foodMenus = mi.getFoodMenus(restaurant.id)

    output = ''
    for item in foodMenus:
        output += item.name + '</br>'
        output += item.price + '</br>'
        output += item.description + '</br></br>'

    return output


# Task 1: Create route for newMenuItem function here
@app.route('/restaurants/<int:restaurant_id>/new/', methods = ['GET', 'POST'])
def newMenuItem(restaurant_id):
        
    rst = RestaurantShop()
    restaurant = rst.getRestaurant(restaurant_id)
    
    if request.method == 'POST':
        
        itemName = request.form['itemName']
        itemDescription = request.form['itemDescription']
        itemCourse = request.form['itemCourse']
        itemPrice = request.form['itemPrice']
        restaurantId = request.form['restaurantId']

        f = FoodMenu()
        f.addFoodMenu(name = itemName, description = itemDescription, course = itemCourse, price = itemPrice, restaurantId = restaurantId)

        flash('New menu item %s was created succesfully' % itemName)
        
        return redirect(url_for('restaurantMenu', restaurant_id = restaurant.id))

    else:

        return render_template('newMenuItem.html', restaurant = restaurant)


# Task 2: Create route for editMenuItem function here
@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit/', methods = ['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
        
    rst = RestaurantShop()
    restaurant = rst.getRestaurant(restaurant_id)
    
    f = FoodMenu()
    foodMenu = f.getFoodMenu(menu_id)
    
    foodName = foodMenu.name
    
    if request.method == 'POST':
        
        itemName = request.form['itemName']
        itemDescription = request.form['itemDescription']
        itemCourse = request.form['itemCourse']
        itemPrice = request.form['itemPrice']
        restaurantId = request.form['restaurantId']
        
        f.editFoodMenu(menuid = menu_id, name = itemName, description = itemDescription, course = itemCourse, price = itemPrice, restaurantId = restaurantId)
        
        flash('Menu item %s was updated successfully' % foodName)
        
        return redirect(url_for('restaurantMenu', restaurant_id = restaurant.id))

    else:

        return render_template('editMenuItem.html', restaurant = restaurant, menuitem = foodMenu)


# Task 3: Create a route for deleteMenuItem function here
@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete/', methods = ['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
        
    rst = RestaurantShop()
    restaurant = rst.getRestaurant(restaurant_id)
    
    f = FoodMenu()
    foodMenu = f.getFoodMenu(menu_id)
    
    foodName = foodMenu.name
    
    if request.method == 'POST':
        
        f.deleteFoodMenu(menuid = menu_id)
        
        flash('Menu item %s was deleted successfully' % foodName)
        
        return redirect(url_for('restaurantMenu', restaurant_id = restaurant.id))

    else:

        return render_template('deletemenuitem.html', restaurant_id = restaurant.id, item = foodMenu)
    

@app.route('/')
@app.route('/restaurants/<int:restaurant_id>')
def restaurantMenu(restaurant_id):
    
    rst = RestaurantShop()
    restaurant = rst.getRestaurant(restaurant_id)
    
    mi = FoodMenu()
    foodMenus = mi.getFoodMenus(restaurant.id)
    
    return render_template('menu.html', restaurant = restaurant, items = foodMenus)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 8889)
