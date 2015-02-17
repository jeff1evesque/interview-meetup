## @app.py
# This file loads corresponding logic, and html template file(s), which
# allows the presentation of (asynchronous) content.
from flask import Flask, render_template, request
from package.database.data_adjust_fave import Adjust_Fave
from package.database.data_retrieve import Get_Fave

# Initialize: create flask instance
app = Flask(__name__)

# Define Route: assign corresponding template, or logic to given path
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/my_fave/', methods=['POST', 'GET'])
def my_fave():
  if request.method == 'POST':
    # get POST data
    fave_classes = request.form.get('class').split()
    fave_gid     = request.form.get('gid')
    fave_uid     = request.form.get('uid')

    if fave_gid.startswith( 'gid-' ):
      # get 'group id' integer value
      try:
        fave_gid = int(fave_gid[4:])
        flag_proceed = True
      except Exception, error:
        print error
        flag_proceed = False

      if flag_proceed:
        data_update = Adjust_Fave()

        # initialize database
        data_update.db_initialize()

        # save fave
        if 'fa-star' in fave_classes:
          data_update.db_fave_add( fave_gid, fave_uid )
          return 'fave stored'

        # remove fave
        elif 'fa-star-o' in fave_classes:
          data_update.db_fave_remove( fave_gid, fave_uid )
          return 'fave removed'

@app.route('/get_fave/', methods=['POST', 'GET'])
def get_fave():
  if request.method == 'POST':
    # get POST data
    meetup_events = request.form.get('events')

    # remove 'gid-' prefix, convert each element to 'int' type
    try:
      meetup_events_processed = [int(event.replace('gid-', '')) for event in meetup_events]
      flag_proceed = True
    except Exception, error:
      print error
      flag_proceed = False

    # return favorite intersection
    if flag_proceed:
      get_data = Get_Fave()
      return get_data.fave_intersection( fave_gid )

# Execute: run application directly, instead of import
if __name__ == '__main__':
  app.run(
  debug=True
)
