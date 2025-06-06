# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyFormulaicContrasts(PythonPackage):
	"""Build contrasts for models defined with formulaic"""
	
	homepage = "https://github.com/scverse/formulaic-contrasts"
	pypi = "formulaic-contrasts/formulaic_contrasts-1.0.0-py3-none-any.whl" 

	version("0.1.0", sha256="a04bf12d8278c36166c08c79c702f9dd3cd764cbf21b8e99ff1fb5a6785a54fa", expand=False, url="https://files.pythonhosted.org/packages/12/97/dd905f85a53002d393ae79f2f140ab85be99b915e21b14cf7ddfd7cce458/formulaic_contrasts-0.1.0-py3-none-any.whl")
	version("0.2.0", sha256="8cd3019f329ff02f08a7f326c5851dc6f84f097aed3f2753aaf3564271c3044c", expand=False, url="https://files.pythonhosted.org/packages/33/a3/c213ea6d8ec13d59a4dbf840958b41c1749db019c4c87ce2933163be4d36/formulaic_contrasts-0.2.0-py3-none-any.whl")
	version("1.0.0", sha256="e1220d315cf446bdec9385375ca4da43896e4ba68114ebea1b2a37efa5d097f5", expand=False, url="https://files.pythonhosted.org/packages/40/7b/639411281256c84e8111bf6cb9676c44dbf5d8ad4cb042f4359b7e7b9e74/formulaic_contrasts-1.0.0-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@3.10:", type=("build", "run"))
	depends_on("py-formulaic", type=("build", "run"))
	depends_on("py-pandas", type=("build", "run"))
	depends_on("py-session-info", type=("build", "run"))

# {'formulaic': ['0.1.0', '0.2.0', '1.0.0'], 'pandas': ['0.1.0', '0.2.0', '1.0.0'], 'session-info': ['0.1.0', '0.2.0', '1.0.0'], "pre-commit;extra=='dev'": ['0.1.0', '0.2.0', '1.0.0'], "twine>=4.0.2;extra=='dev'": ['0.1.0', '0.2.0', '1.0.0'], "docutils!=0.18.*,!=0.19.*,>=0.8;extra=='doc'": ['0.1.0', '0.2.0', '1.0.0'], "ipykernel;extra=='doc'": ['0.1.0', '0.2.0', '1.0.0'], "ipython;extra=='doc'": ['0.1.0', '0.2.0', '1.0.0'], "myst-nb>=1.1;extra=='doc'": ['0.1.0', '0.2.0', '1.0.0'], "pandas;extra=='doc'": ['0.1.0', '0.2.0', '1.0.0'], "setuptools;extra=='doc'": ['0.1.0', '0.2.0', '1.0.0'], "sphinx-autodoc-typehints;extra=='doc'": ['0.1.0', '0.2.0', '1.0.0'], "sphinx-book-theme>=1;extra=='doc'": ['0.1.0', '0.2.0', '1.0.0'], "sphinx-copybutton;extra=='doc'": ['0.1.0', '0.2.0', '1.0.0'], "sphinx-tabs;extra=='doc'": ['0.1.0', '0.2.0', '1.0.0'], "sphinx>=4;extra=='doc'": ['0.1.0', '0.2.0', '1.0.0'], "sphinxcontrib-bibtex>=1;extra=='doc'": ['0.1.0', '0.2.0', '1.0.0'], "sphinxext-opengraph;extra=='doc'": ['0.1.0', '0.2.0', '1.0.0'], "statsmodels;extra=='doc'": ['0.1.0', '0.2.0', '1.0.0'], "coverage;extra=='test'": ['0.1.0', '0.2.0', '1.0.0'], "numpy;extra=='test'": ['0.1.0', '0.2.0', '1.0.0'], "pytest;extra=='test'": ['0.1.0', '0.2.0', '1.0.0']}