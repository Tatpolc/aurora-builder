from function import function

user_func = input("Select function to use: ")

if user_func == 'all':
    apt = function()
    apt.import_apt()
    wpt = function()
    wpt.import_wpt()
    vor = function()
    vor.import_vor()
    ndb = function()
    ndb.impot_ndb()
    ils = function()
    ils.import_ils()
    rwy = function()
    rwy.import_rwy()
elif user_func == 'apt':
    apt = function()
    apt.import_apt()
elif user_func == 'wpt':
    wpt = function()
    wpt.import_wpt()
elif user_func == 'vor':
    vor = function()
    vor.import_vor()
elif user_func == 'ndb':
    ndb = function()
    ndb.impot_ndb()
elif user_func == 'ils':
    ils = function()
    ils.import_ils()
elif user_func == 'rwy':
    rwy = function()
    rwy.import_rwy()
elif user_func == 'aiw':
    aiw = function()
    aiw.import_airway()
else:
    print('Wrong Function')
