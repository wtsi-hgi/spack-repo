# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyTranslationstring(PythonPackage):
	"""Utility library for i18n relied on by various Repoze and Pyramid packages"""
	
	homepage = "https://github.com/Pylons/translationstring"
	pypi = "translationstring/translationstring-1.4-py2.py3-none-any.whl" 

	version("0.1", sha256="3a15028662edd4c2bd9b438ccdb616548ace01d4efd0e574b949480706fdd540")
	version("0.2", sha256="cf66bcaf23a65d73411eeaab2015855c0c0a1b0d201bcbc788fa4c81da79285d")
	version("0.3", sha256="ef5aff7b977b3995abd822e9eb0469b5d26ea3508f64a30b801fccd84fe02a5a")
	version("0.4", sha256="765eba6d152ec8cd1ec11b0b24dca38585b3afb96f0670574fbf16a16b412ee5")
	version("1.0", sha256="1463e8609ada4d76ff8558e6e8c9b5186f84c907377875b06a79ccbe5f1fac26")
	version("1.1", sha256="8147c47e8091bc7b8168758a01c049581959faba9d56cafde8734de44e98711c")
	version("1.2", sha256="74cf954f28e44866e1628b48c9797bca0e2836bff2656e2ee8a04f78cbe56f71")
	version("1.3-py2.7", sha256="e26c7bf383413234ed442e0980a2ebe192b95e3745288a8fd2805156d27515b4", expand=False, url="https://files.pythonhosted.org/packages/26/e7/9dcf5bcd32b3ad16db542845ad129c06927821ded434ae88f458e6190626/translationstring-1.3-py2.py3-none-any.whl")
	version("1.4", sha256="5f4dc4d939573db851c8d840551e1a0fb27b946afe3b95aafc22577eed2d6262", expand=False, url="https://files.pythonhosted.org/packages/3b/98/36187601a15e3d37e9bfcf0e0e1055532b39d044353b06861c3a519737a9/translationstring-1.4-py2.py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@2..7", when="@1.3-py2.7", type=("build", "run"))

# {"Sphinx(>=1.3.1);extra=='docs'": ['1.4'], "docutils;extra=='docs'": ['1.4'], "pylons-sphinx-themes;extra=='docs'": ['1.4']}