# -*- coding: utf-8 -*-
import os

from flask import Blueprint, render_template

mod = Blueprint(
    '{{{ name }}}', __name__, url_prefix='/{{{ name }}}',
    template_folder=os.path.join(os.pardir, {{{ name }}})
)


@mod.route('/')
def index():
    return render_template('index.html')
