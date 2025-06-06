# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyBrewer2mpl(PythonPackage):
	"""Connect colorbrewer2.org color maps to Python and matplotlib"""
	
	homepage = "https://github.com/jiffyclub/brewer2mpl/wiki"
	pypi = "brewer2mpl/brewer2mpl-1.4.1-py2.py3-none-any.whl" 

	version("1.0", sha256="a74c8d49cc06a8aaa4d1b8a19bf7dd86d4f41deb13e49a9d124b9a1f458d4106")
	version("1.1", sha256="3c917795250f9055e196989f9dd0f479ae7f784c5eaffab52e81bee91ee6e2fa")
	version("1.2", sha256="7cdcea4bfa2ca1dfa86f074e0ef21a8177ab8bd2a5b6a2aa56d6aef986191bb9")
	version("1.3", sha256="aa5ed96fee8c0b161d36282c0ba0422f6ab94763f3c3adc73beaf4a0125ca6f7")
	version("1.3.1", sha256="608fd0b718a3f9dd4ec3e3063d9e5c8d90992d6a7ed2066c0bb08674d4771756")
	version("1.3.2", sha256="298291cc3c6fd3110886c868007714bd54ba3032398fc71607156db3efdcbd14")
	version("1.4", sha256="12d48f942a2f382adc5fc3572714634addbb43bcc43fadd6a00ee0e6957da413", expand=False, url="https://files.pythonhosted.org/packages/c4/3f/0d15b58cec201c5ed4d543858e317abb9fdb15ae59d6b38da4cec554268f/brewer2mpl-1.4-py2.py3-none-any.whl")
	version("1.4.1", sha256="f89a795efc810fdbec359902d388980711604cc32907445ba1bc45f699d3fe81", expand=False, url="https://files.pythonhosted.org/packages/84/57/00c45a199719e617db0875181134fcb3aeef701deae346547ac722eaaf5e/brewer2mpl-1.4.1-py2.py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
