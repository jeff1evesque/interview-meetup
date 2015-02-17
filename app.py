## @app.py
# This file loads corresponding logic, and html template file(s), which
# allows the presentation of (asynchronous) content.
from flask import Flask, render_template, request
from package.database.data_adjust_fave import Adjust_Fave

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

    data_update  = Adjust_Fave()

    # initialize database
    data_update.db_initialize()

    # save fave
    if 'fa-star' in fave_classes:
      data_update.db_fave_add( {'uid': fave_uid, 'group_id': fave_gid} )
      return 'fave stored'

    # remove fave
    elif 'fa-star-o' in fave_classes:
      data_update.db_fave_remove( {'uid': fave_uid, 'group_id': fave_gid} )
      return 'fave removed'

# Execute: run application directly, instead of import
if __name__ == '__main__':
  app.run(
  debug=True
)
