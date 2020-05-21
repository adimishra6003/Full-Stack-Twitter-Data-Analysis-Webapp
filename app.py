from flask import Flask, render_template
from main import main_func

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def index():
	top_3_world, world_sentiments, top_3_india, india_sentiments= main_func()
	return render_template("Page.html", w_1 = top_3_world[0], w_s_1 = round(world_sentiments[0], 3), w_2 = top_3_world[1], w_s_2 = round(world_sentiments[1], 3), w_3 = top_3_world[2], w_s_3 = round(world_sentiments[2], 3),
		i_1 = top_3_india[0], i_s_1 = round(india_sentiments[0], 3), i_2 = top_3_india[1], i_s_2 = round(india_sentiments[1], 3), i_3 = top_3_india[2], i_s_3 = round(india_sentiments[2], 3))


if __name__=="__main__":
    app.run(debug = True)

# @app.after_request
# def add_header(response):
#     # response.cache_control.no_store = True
#     response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
#     response.headers['Pragma'] = 'no-cache'
#     response.headers['Expires'] = '-1'
#     return response