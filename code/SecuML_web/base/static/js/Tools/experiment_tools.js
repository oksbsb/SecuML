function getValidationDataset(project, dataset, experiment_id) {
    var query = buildQuery('getValidationDataset',
                    [project, dataset, experiment_id]);
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open('GET', query, false);
    xmlHttp.send(null);
    var validation_dataset = xmlHttp.responseText;
    return validation_dataset;
}

function getAlertsClusteringExperimentId(project, dataset, 
                experiment_id) {
    var query = buildQuery('getAlertsClusteringExperimentId',
                    [project, dataset, experiment_id]);
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open('GET', query, false);
    xmlHttp.send(null);
    var clustering_experiment_id = xmlHttp.responseText;
    return clustering_experiment_id;
}

function getExperimentId(project, dataset, experiment_name) {
    var query = buildQuery('getExperimentId', 
                    [project, dataset, experiment_name]);
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open('GET', query, false);
    xmlHttp.send(null);
    var experiment_id = xmlHttp.responseText;
    return experiment_id;
}

function getExperimentName(project, dataset, experiment_id) {
    var query = buildQuery('getExperimentName', 
                    [project, dataset, experiment_id]);
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open('GET', query, false);
    xmlHttp.send(null);
    var experiment_name = xmlHttp.responseText;
    return experiment_name;
}

function getExperimentLabelId(project, dataset, experiment_id) {
    var query = buildQuery('getExperimentLabelId', 
                    [project, dataset, experiment_id]);
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open('GET', query, false);
    xmlHttp.send(null);
    var experiment_label_id = xmlHttp.responseText;
    return experiment_label_id;
}

function getChildren(project, dataset, experiment_id) {
    var query = buildQuery('getChildren', 
                    [project, dataset, experiment_id]);
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open('GET', query, false);
    xmlHttp.send(null);
    return xmlHttp.responseText.split(' ');
}

function datasetHasSublabels(project, dataset, experiment_label_id) {
    var families_monitoring_query = buildQuery('datasetHasSublabels',
            [project, dataset, experiment_label_id]);
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open('GET', query, false);
    xmlHttp.send(null);
    var families_monitoring = xmlHttp.responseText == 'True';
    return families_monitoring;
}
