{{ '=' * cookiecutter.project_name|length }}
{{ cookiecutter.project_name }}
{{ '=' * cookiecutter.project_name|length }}

{{ cookiecutter.description }}

Getting started
===============

.. code:: console

   pip install {{ cookiecutter.project_name }}

.. code:: python

   extensions = [
       ...,  # Your extensions
       "{{ cookiecutter.package_fullname }}",
   ]
