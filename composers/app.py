from flask import Blueprint, render_template
import time

composers_bp = Blueprint('composers', __name__, static_folder='', template_folder='')

@composers_bp.route('/', methods=['GET'])
def main():
  return render_template('composers.html')

@composers_bp.route('/', methods=['POST'])
def timer():
  time.sleep(3)
  return 'Played!'
