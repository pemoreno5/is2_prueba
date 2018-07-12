require 'sequel'

#Sequel::Model.plugin :json_serializer

DB = Sequel.connect('sqlite://db/db_chasquirunner.db')
