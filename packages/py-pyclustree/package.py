# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPyclustree(PythonPackage):
	"""Visualize cluster assignments at different resolutions"""
	
	homepage = "https://github.com/complextissue/pyclustree"
	pypi = "pyclustree/pyclustree-0.3.2-py3-none-any.whl" 

	version("0.2.2", sha256="928ad0838ae0a768a62726563ecf4c4c8c0bd62af701c3038b51e657ec663427", expand=False, url="https://files.pythonhosted.org/packages/be/6f/3baf8c61dd97b67328c50ee023d9252e0d53c8c52b3111144b41a776a06a/pyclustree-0.2.2-py3-none-any.whl")
	version("0.3.0", sha256="d9c7d9b1bd99160aba2d13537c4893f9fc0997ffc766fd0a283f8115822c6380", expand=False, url="https://files.pythonhosted.org/packages/65/7b/efd87145a66a6a1717ba80204fa757e8a398d81af5ed98e735888c415f1c/pyclustree-0.3.0-py3-none-any.whl")
	version("0.3.2", sha256="7458ecfbea4d7685741c4c32d73f98c16e4de0bc1afc6a7a6ed4df634b35d0c7", expand=False, url="https://files.pythonhosted.org/packages/53/65/568de5a4e4b57644045fe47a19e56241cea9d2e3baf94e748dffe4afcddd/pyclustree-0.3.2-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@3.9:", type=("build", "run"))
	depends_on("py-anndata", type=("build", "run"))
	depends_on("py-matplotlib", type=("build", "run"))
	depends_on("py-networkx", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))
	depends_on("py-pandas", type=("build", "run"))
	depends_on("py-seaborn", type=("build", "run"))
	depends_on("py-session-info", type=("build", "run"))

# {'anndata': ['0.2.2', '0.3.0', '0.3.2'], 'matplotlib': ['0.2.2', '0.3.0', '0.3.2'], 'networkx': ['0.2.2', '0.3.0', '0.3.2'], 'numpy': ['0.2.2', '0.3.0', '0.3.2'], 'pandas': ['0.2.2', '0.3.0', '0.3.2'], 'seaborn': ['0.2.2', '0.3.0', '0.3.2'], 'session-info': ['0.2.2', '0.3.0', '0.3.2'], 'coverage;extra=="dev"': ['0.2.2', '0.3.0', '0.3.2'], 'docutils>=0.8,!=0.18.*,!=0.19.*;extra=="dev"': ['0.2.2', '0.3.0', '0.3.2'], 'flit;extra=="dev"': ['0.2.2', '0.3.0', '0.3.2'], 'furo;extra=="dev"': ['0.2.2', '0.3.0', '0.3.2'], 'ipykernel;extra=="dev"': ['0.2.2', '0.3.0', '0.3.2'], 'ipython;extra=="dev"': ['0.2.2', '0.3.0', '0.3.2'], 'myst-parser;extra=="dev"': ['0.2.2', '0.3.0', '0.3.2'], 'nbsphinx;extra=="dev"': ['0.2.2', '0.3.0', '0.3.2'], 'pandas;extra=="dev"': ['0.2.2', '0.3.0', '0.3.2'], 'pandoc;extra=="dev"': ['0.2.2', '0.3.0', '0.3.2'], 'pre-commit;extra=="dev"': ['0.2.2', '0.3.0', '0.3.2'], 'pytest;extra=="dev"': ['0.2.2', '0.3.0', '0.3.2'], 'python-igraph;extra=="dev"': ['0.2.2', '0.3.0', '0.3.2'], 'scanpy;extra=="dev"': ['0.2.2', '0.3.0', '0.3.2'], 'setuptools;extra=="dev"': ['0.2.2', '0.3.0', '0.3.2'], 'sphinx>=4;extra=="dev"': ['0.2.2', '0.3.0', '0.3.2'], 'sphinx-autoapi;extra=="dev"': ['0.2.2', '0.3.0', '0.3.2'], 'sphinx-autodoc-typehints;extra=="dev"': ['0.2.2', '0.3.0', '0.3.2'], 'sphinx-book-theme>=1;extra=="dev"': ['0.2.2', '0.3.0', '0.3.2'], 'sphinx-copybutton;extra=="dev"': ['0.2.2', '0.3.0', '0.3.2'], 'sphinx-design;extra=="dev"': ['0.2.2', '0.3.0', '0.3.2'], 'sphinx-rtd-theme;extra=="dev"': ['0.2.2', '0.3.0', '0.3.2'], 'sphinx-tabs;extra=="dev"': ['0.2.2', '0.3.0', '0.3.2'], 'sphinxcontrib-bibtex>=1;extra=="dev"': ['0.2.2', '0.3.0', '0.3.2'], 'sphinxext-opengraph;extra=="dev"': ['0.2.2', '0.3.0', '0.3.2'], 'twine>=4.0.2;extra=="dev"': ['0.2.2', '0.3.0', '0.3.2']}