import bjoern

import resonanzkontrolle.resonanzkontrolle as resonanzkontrolle


# Run WSGI server with app
app = resonanzkontrolle.create_app()
bjoern.run(app, 'localhost', 8002)
