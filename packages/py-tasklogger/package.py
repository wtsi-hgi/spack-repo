# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyTasklogger(PythonPackage):
	"""tasklogger"""
	
	homepage = "https://github.com/scottgigante/tasklogger"
	pypi = "tasklogger/tasklogger-1.2.0-py3-none-any.whl" 

	version("0.0", sha256="34c45abcceff0cb3e82b952ce794fda5a1817ce86d3882b401ef9fa973f109bd")
	version("0.1", sha256="187eb37de37ff83bef9010887a0be60d9b9692376b8f5cfc702c8d3f77193d47")
	version("0.2", sha256="c6a6de70aa5ff69b4107218c7c0604c6567529a8dcafabe085330f38a34d082b")
	version("0.2.1", sha256="50a3a20c9d675dc0e40f8a7d532bf845526ffa98a21ed0cd5ed957fcd40e54c1")
	version("0.2.2", sha256="f37f9c147383614817fe601fccc66c3b9e0754bdd06e0ac84598ff92e0f79cf2")
	version("0.3.0", sha256="8f50603b229827ec0cb46fa0be5e87a2bf1c640d5842d7aab450789efbd2e603")
	version("0.4.0", sha256="4ac7488643608199078f7cb58901da1c4e677d262e954d714ca154d9e62a4a97", expand=False, url="https://files.pythonhosted.org/packages/52/e1/26655e9216d678dbdb8d9dc1cf7005644837cf623fa66b851e7fc3c104d7/tasklogger-0.4.0-py3-none-any.whl")
	version("0.4.1", sha256="03345a4b82d5d10043f6056d180c7fb468ad39d89e21092fef57883a486d63bc", expand=False, url="https://files.pythonhosted.org/packages/27/02/6c7a14d210876a0df60e4deeef1fc6213cb166b53e35b47fe5bd5fbfe193/tasklogger-0.4.1-py3-none-any.whl")
	version("0.4.2", sha256="868384ed3a2acbd7b2a4bb30095c5a4cda96e5d904aa723cb4045f63d66db94c", expand=False, url="https://files.pythonhosted.org/packages/2e/4d/9790904bb5ec98dbdeb81b9e52c15f125a3f88103d03d26dbff9cfce3f9c/tasklogger-0.4.2-py3-none-any.whl")
	version("1.0.0", sha256="70eef6ec022de885af774c84575d36d9e9006c7844724e75db7ff7ecb5998039", expand=False, url="https://files.pythonhosted.org/packages/5d/6b/cb2a724eff19829a0ada0217f403f54fca1e48c7de6fc3383e0a8b8fa121/tasklogger-1.0.0-py3-none-any.whl")
	version("1.1.0", sha256="ba45b3488abc08a53639e8b5b38d9cfca2911daf664010c1929dfb7b2e98aeb0", expand=False, url="https://files.pythonhosted.org/packages/2a/ba/d9b56be2de592e106013930718ba3d3bb0154ae55a3a4ab59197324dd60e/tasklogger-1.1.0-py3-none-any.whl")
	version("1.1.2", sha256="6c9f9bf82b0866a2c75427f0f52e70087355789a20d46caa712f2b92c51e0891", expand=False, url="https://files.pythonhosted.org/packages/08/84/a55b3a5a0e11c3545377642f5e5acb724e3535aa21ef4574a2ae77c8fa83/tasklogger-1.1.2-py3-none-any.whl")
	version("1.2.0", sha256="b320fcabbb6bbd88e63c65cd994d75038c2cde45b58eb28941c3848710855524", expand=False, url="https://files.pythonhosted.org/packages/d6/f5/24855d6d8862ad03ae4dbb8f3ec06baf930a276c92af603b3d9bf32600d0/tasklogger-1.2.0-py3-none-any.whl")

	depends_on("python@3.6:", type=("build", "run"))
	depends_on("py-coveralls", type=("build", "run"))
	depends_on("py-coverage", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))
	depends_on("py-nose2", type=("build", "run"))
	depends_on("py-deprecated", type=("build", "run"))
