# SecuML
# Copyright (C) 2016-2017  ANSSI
#
# SecuML is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# SecuML is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with SecuML. If not, see <http://www.gnu.org/licenses/>.

from flask import jsonify, render_template, send_file
import pandas as pd
import os.path as path

from SecuML.web import app
from SecuML.web.views.experiments import updateCurrentExperiment
from SecuML.web.views.nocache import nocache

from SecuML.experiments.ActiveLearning.ActiveLearningExperiment import ActiveLearningExperiment


@app.route('/getAnnotationsTypes/<experiment_id>/<iteration>/')
@nocache
def getAnnotationsTypes(experiment_id, iteration):
    experiment = updateCurrentExperiment(experiment_id)
    filename = path.join(experiment.getOutputDirectory(),
                         str(iteration),
                         'annotations_types.json')
    return send_file(filename)


@app.route('/getFamiliesInstancesToAnnotate/<experiment_id>/<iteration>/<predicted_label>/')
def getFamiliesInstancesToAnnotate(experiment_id, iteration, predicted_label):
    experiment = updateCurrentExperiment(experiment_id)
    filename = path.join(experiment.getOutputDirectory(),
                         str(iteration),
                         'toannotate_' + predicted_label + '.json')
    return send_file(filename)


@app.route('/getInstancesToAnnotate/<experiment_id>/<iteration>/<predicted_label>/')
def getInstancesToAnnotate(experiment_id, iteration, predicted_label):
    experiment = updateCurrentExperiment(experiment_id)
    if predicted_label == 'None':
        filename = 'toannotate.csv'
    else:
        filename = 'toannotate_%s.csv' % predicted_label
    filename = path.join(experiment.getOutputDirectory(),
                         iteration,
                         filename)
    df = pd.read_csv(filename)
    queries = [int(x) for x in df.instance_id]
    return jsonify({'instances': queries})


@app.route('/individualAnnotations/<experiment_id>/<iteration>/')
def individualAnnotations(experiment_id, iteration):
    experiment = updateCurrentExperiment(experiment_id)
    return render_template('ActiveLearning/individual_annotations.html', project=experiment.project)


@app.route('/ilabAnnotations/<experiment_id>/<iteration>/')
def ilabAnnotations(experiment_id, iteration):
    experiment = updateCurrentExperiment(experiment_id)
    return render_template('ActiveLearning/ilab_annotations.html', project=experiment.project)


@app.route('/rareCategoryDetectionAnnotations/<experiment_id>/<iteration>/')
def rareCategoryDetectionAnnotations(experiment_id, iteration):
    experiment = updateCurrentExperiment(experiment_id)
    return render_template('ActiveLearning/rare_category_detection_annotations.html', project=experiment.project)
