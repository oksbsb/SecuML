Seeting up SecuML
=================


SecuML comes with a web user interface to display the results of the analysis and interact with the Machine Learning models.
The analyses must be run from the command line.
Once they are computed, the results can be displayed in the web user interface.


Database
--------
SecuML requires an access to a database. MySQL and PostgreSQL are supported.
The user must have the following permissions: ``SELECT``, ``INSERT``, ``UPDATE``, ``DELETE``, ``CREATE TEMPORARY TABLES``.
The URI of the database must be specified in SecuML :ref:`configuration file <configuration>`.

*MySQL database*

* MySQL server (>= 5.5.49)
* Python package

    + mysql.connector (>= 2.1.3, <= 2.1.4)

*PostgreSQL database*

* PostgreSQL server (>= 9.4.13)
* Python package

    + psycopg2-binary (>= 2.5.4)


Installation
------------

Requirements
""""""""""""

+ rabbitmq-server (>= 3.3.5) (only for :ref:`ILAB <ILAB>` and :ref:`rare category detection <RCD>`)
+ Python packages

    * celery (>= 3.1.13) (only for :ref:`ILAB <ILAB>` and :ref:`rare category detection <RCD>`)
    * flask (>= 0.10.1)
    * flask_sqlalchemy (>= 1.0)
    * matplotlib (>= 2.1.1)
    * metric-learn (>= 0.4.0)
    * numpy (== 1.12.1)
    * pandas (== 0.19.2)
    * scikit-learn (== 0.19.0)
    * sqlalchemy (>= 1.0.12)
    * yaml (>= 3.11)

Automatic Installation
"""""""""""""""""""""""

.. code-block:: bash

    virtualenv venv_SecuML --no-site-packages --python python3
    source venv_SecuML/bin/activate
    python3 setup.py install

.. warning::

    The dependencies stored in `requirements.txt` are automatically installed by `setup.py`.
    They cannot be installed with `pip install -r requirements.txt` because the required version
    of `metric-learn` has not been released on PyPI yet.


.. _configuration:

Configuration
-------------

SecuML requires a configuration file that follows the following format:

.. code-block:: yaml

    input_data_dir: <directory containing the input datasets>
    output_data_dir: <directory where the results of the experiments are stored>
    db_uri: <URI of the database>
    logger_level: <[optional] DEBUG,INFO,WARNING,ERROR or CRITICAL - default INFO>
    logger_output: <[optional] name of the logging output file - default sys.stderr>

See `SecuML_conf_template.yml <https://github.com/ANSSI-FR/SecuML/blob/master/conf/SecuML_conf_template.yml>`_.

Input and Output Directories
""""""""""""""""""""""""""""
.. warning::

    `input_data_dir` and `output_data_dir` must contain **absolute paths**.


* The input directory contains the datasets that will be analyzed by SecuML. See :ref:`Data <Data>` for more information.

* The output directory contains all the results of the SecuML experiments. Users should not read the results from this directory directly, but rather from the :ref:`web user interface <GUI>`.

.. note::

    ``input_data_dir`` must be set to `input_data <https://github.com/ANSSI-FR/SecuML/tree/master/input_data/>`_
    in the configuration file to test SecuML with the dataset we provide.


Database URI
""""""""""""

The format of the database URI depends on its type:

* MySQL database

  .. code-block:: bash

      mysql+mysqlconnector://<user>:<password>@<host>/<db_name>


* PostgreSQL database

  .. code-block:: bash

      postgresql://<user>:<password>@<host>/<db_name>

Logging Parameters
"""""""""""""""""""

Logging parameters (``logger_level`` and ``logger_output``) are optional.
By default, logging is displayed in the standard error with ``INFO`` level.

.. note::

  The configuration file is required to run SecuML executables (e.g. ``SecuML_server``, ``SecuML_DIADEM``, ``SecuML_ILAB``).
  It can be specified either with the parameter ``--secuml-conf`` for each execution, or globally
  with the environment variable ``SECUMLCONF``.


.. _GUI:

Web User Interface
------------------

SecuML comes with a web user interface to display the results of the experiments, and to interact with machine learning models (see :ref:`ILAB <ILAB>` and :ref:`Rare Category Detection <RCD>`).

``SecuML_server`` must be executed to launch the web server.

``http://localhost:5000/SecuML/`` gives access to SecuML menu.
It displays the list of projects and datasets available.
Besides, for each dataset, it displays the list of experiments gathered by type.

``http://localhost:5000/SecuML/<experiment_id>/`` displays directly
the results of an experiment identified by ``experiment_id``.

