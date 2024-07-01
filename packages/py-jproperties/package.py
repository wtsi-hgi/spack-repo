# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyJproperties(PythonPackage):
	"""Java Property file parser and writer for Python"""
	
	homepage = "https://github.com/Tblue/python-jproperties"
	pypi = "jproperties/jproperties-2.1.1-py2.py3-none-any.whl" 

	version("1.0.1", sha256="f51d9c0875ae4602930f18e198c69ce2bd1d7008a71f7628316abec56e73db83", expand=False, url="https://files.pythonhosted.org/packages/c1/ae/4d682c901b9e6b8ead960ffd82c514123fa3f39a9689f85626f27ba3d937/jproperties-1.0.1-py2-none-any.whl")
	version("2.0.0", sha256="e1b1fd274e8c99cf393cb957b8b8ad7e67cb14d6022d7653e0709d8bc7437d65", expand=False, url="https://files.pythonhosted.org/packages/8a/f4/30e0414495acf4b4224d948edb035d7fcde72afad36207f10c8055918aa6/jproperties-2.0.0-py3-none-any.whl")
	version("2.1.0", sha256="84116a04e06e85d84c4bc7bfc45e23d0c956c2efc038f57c47cafffdc0cdad0f", expand=False, url="https://files.pythonhosted.org/packages/17/e5/9aee9f1347d4dee6e6e97f0a8e064261475787fa03a67ec274c2e32d4edb/jproperties-2.1.0-py3-none-any.whl")
	version("2.1.1", sha256="4dfcd7cab56d9c79bce4453f7ca9ffbe0ff0574ddcf1c2a99a8646df60634664", expand=False, url="https://files.pythonhosted.org/packages/1e/b5/822b214d287ca45f7fbe5de3daa31a96c83e46b9511158d63709d057f66e/jproperties-2.1.1-py2.py3-none-any.whl")

	depends_on("py-six", type=("build", "run"))

# {'six(~=1.10)': ['2.0.0'], 'six(~=1.12)': ['2.1.0'], 'six(~=1.13)': ['2.1.1']}