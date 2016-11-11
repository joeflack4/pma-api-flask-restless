from app.models import db, AppConfig
from app.config import sk_generator
# from psycopg2 import IntegrityError
# from sqlalchemy.exc import IntegrityError
# from sqlalchemy import update

### Notes ###
# The following code is an example of a way that works to update a db value.
# user = User.query.filter_by(id='9').update(dict(username='newname'))

integrity_error = "* IntegrityError: (({})) - Exception occurred while trying to add 1+ default sets of values. Perhaps they already exist."
errors = []

# DB creation.
# - Creates DB schema if it does not already exist.
db.create_all()

def add_rows_to_config_table(table_name, table_class, table_rows):

    commit_errors = False
    for key, value, permission_level, active in table_rows:
        try:
            db.session.add(table_class(key, value, permission_level, active))
            db.session.commit()
        except:
            commit_errors = True
            db.session.rollback()
    if commit_errors == True:
        errors.append(integrity_error.format(table_name))

# App config initialization.
# IMPORTANT! - Post-deployment, you will want to make sure that you change the secret key value in your database.
app_config_rows = [["App Name", "PMA API", 1, True],
    ["App Icon", "glyphicon glyphicon-equalizer", 1, True],
    ["App Title", "PMA API", 1, True],
    ["App Short-Title", "PMA API", 1, True],
    ["Secret Key", sk_generator(size=24), 1, True]]
add_rows_to_config_table('App Config', AppConfig, app_config_rows)

# - Summary
print("")
print("# # # Database creation and initialization complete. # # #")
print("")
if len(errors) > 0:
    print("Summary of exceptions: ")
    for error in errors:
        print(error)
    print("")
