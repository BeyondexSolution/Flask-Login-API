# import os
# from flask_sqlalchemy import SQLAlchemy

# class Config:
#     # Updated connection string
# #     SQLALCHEMY_DATABASE_URI = (
# #         'mssql+pyodbc://db_9cba9c_bcloud_admin:Bcloud%40123@SQL5111.site4now.net/db_9cba9c_bcloud'
# #         '?driver=ODBC+Driver+17+for+SQL+Server'
# # #     )
# #      SQLALCHEMY_DATABASE_URI = (
# #         'mssql+pyodbc://db_9cba9c_gigi_admin:Gigi%401234@SQL8006.site4now.net/db_9cba9c_gigi'
# #         '?driver=ODBC+Driver+17+for+SQL+Server'
# #      )
# #      SQLALCHEMY_TRACK_MODIFICATIONS = False
#     SQLALCHEMY_DATABASE_URI = (
#         'mssql+pymssql://db_9cba9c_gigi_admin:Gigi%401234@SQL8006.site4now.net/db_9cba9c_gigi'
#     )
#     SQLALCHEMY_TRACK_MODIFICATIONS = False


# db = SQLAlchemy()
# config/settings.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Create an instance of SQLAlchemy

class Config:
    SQLALCHEMY_DATABASE_URI = 'mssql+pymssql://db_9cba9c_gigi_admin:Gigi%401234@SQL8006.site4now.net/db_9cba9c_gigi'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable modification tracking to save memory
