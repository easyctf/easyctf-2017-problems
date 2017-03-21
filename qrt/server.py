from flask import Flask, request
from qrt import generate
from base64 import b64encode
from binascii import b2a_base64
from cStringIO import StringIO
from traceback import format_exc

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
	try:
		html = "<title>hex qr</title><form method=post>enter a string: <input type=text name=text value='%s' autocomplete=off autofocus /></form>"
		if request.method == "POST":
			if not request.form.get("text"):
				html %= ""
				html += "<p>empty</p>"
			else:
				html %= request.form["text"]
				im = generate(request.form["text"])
				buf = StringIO()
				im.save(buf, format="JPEG")
				html += "<img src='data:image/jpeg;base64,%s'>" % b2a_base64(buf.getvalue())
		else:
			html %= ""
		return html
	except:
		return "<!--\nthere's a problem, here's the details:\n%s\n-->" % format_exc()

app.run(host="0.0.0.0", port=5000)