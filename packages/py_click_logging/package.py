# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyClickLogging(PythonPackage):
	"""Logging integration for Click"""
	
	homepage = "https://github.com/Toilal/click-logging"
	pypi = "click-logging/click_logging-1.0.1-py2.py3-none-any.whl" 

	version("1.0.0", sha256="ae2fa94e7bb7a2774a8692776f4d83d4dbd549cc595d591643701faf628a1aa9", expand=False, url="https://files.pythonhosted.org/packages/2c/5c/355fac9a04182d6e41a874e13e1c92dc3d7e4ae03523df6864c0fff6e6b9/click_logging-1.0.0-py2.py3-none-any.whl")
	version("1.0.1", sha256="3ce04f9fa93120343f5d727108f2066b59bd9c5aac2d770a02f37c69186dbf23", expand=False, url="https://files.pythonhosted.org/packages/f3/82/31f403a7b19b8fed3c71011e8065d2dc670e13b2195133da11606d797736/click_logging-1.0.1-py2.py3-none-any.whl")

	depends_on("py-commitizen", type=("build", "run"))
	depends_on("py-pre-commit", type=("build", "run"))
	depends_on("py-python-semantic-release", type=("build", "run"))
	depends_on("py-flake8", type=("build", "run"))
	depends_on("py-pytest", type=("build", "run"))
	depends_on("py-coveralls", type=("build", "run"))
	depends_on("py-coverage", type=("build", "run"))
	depends_on("py-click", type=("build", "run"))

# {'click': ['1.0.0', '1.0.1'], "coverage;extra=='ci'": ['1.0.0', '1.0.1'], "coveralls;extra=='ci'": ['1.0.0', '1.0.1'], "pytest;extra=='dev'": ['1.0.0', '1.0.1'], "flake8;extra=='dev'": ['1.0.0', '1.0.1'], "python-semantic-release;extra=='dev'": ['1.0.0', '1.0.1'], "pre-commit;extra=='dev'": ['1.0.0', '1.0.1'], "commitizen;extra=='dev'": ['1.0.0', '1.0.1']}