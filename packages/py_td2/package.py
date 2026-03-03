# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyTd2(PythonPackage):
	"""A tool to find protein coding ORFs"""
	
	homepage = "https://github.com/Markusjsommer/TD2"
	pypi = "TD2/td2-1.0.6-py3-none-any.whl" 

	version("1.0.0", sha256="b2a1e7e5b060b179beb3843176aa759bf7e15014f9e4a413f024b197d448dee8", expand=False, url="https://files.pythonhosted.org/packages/f6/f9/c52c232ea9f0677a8dcc8372c808f2db059730d017e5081a1c0ce151398c/TD2-1.0.0-py3-none-any.whl")
	version("1.0.1", sha256="4c2109e948c39b5cb62429d80bf19a7d8d47c7f7e7ab7495e48e08ca3beee4ff", expand=False, url="https://files.pythonhosted.org/packages/ff/a4/ab6be14acf5c1f585afc4881d8fc05f1aa2ba8985326d9af761acf9feaa4/td2-1.0.1-py3-none-any.whl")
	version("1.0.2", sha256="7a283ed289109bcf8dbff08663eedd8f90c3eb38c0d4b221f6f6a40d2628e17a", expand=False, url="https://files.pythonhosted.org/packages/59/7f/c557088b575b11b930a810c4b08d7947c231bfbd6083e23691ab6d4f35d7/td2-1.0.2-py3-none-any.whl")
	version("1.0.3", sha256="0991035b6ec5b023a32ff24d019ea2e0e217410777fa8dd6d934c6658c96018e", expand=False, url="https://files.pythonhosted.org/packages/9c/12/08401c017e913b8fd32b212039af4a257aad486f53600624d391560eb554/TD2-1.0.3-py3-none-any.whl")
	version("1.0.5", sha256="97c642931c91685bef259ad89328aa62481b306e049cf6948ae9de30da767a05", expand=False, url="https://files.pythonhosted.org/packages/c3/e0/adcb22d02f8881bdfce4a3c89003203115487946a2015cb5350d7c8884f3/TD2-1.0.5-py3-none-any.whl")
	version("1.0.6", sha256="091231466030a757a9c98b64e4db63704f3b4c37a521120053440050029ccad0", expand=False, url="https://files.pythonhosted.org/packages/ab/bc/6cb935774ae1b624faff92638a3422f0f12aeaf5f61ff820adbbd36464fc/td2-1.0.6-py3-none-any.whl")

	depends_on("python@3.9:3.13", type=("build", "run"))
	depends_on("py-psauron", type=("build", "run"))
	depends_on("py-typing-extensions", type=("build", "run"))
	depends_on("py-tqdm", type=("build", "run"))
	depends_on("py-scipy", type=("build", "run"))
	depends_on("py-pandas", type=("build", "run"))
	depends_on("py-wheel", type=("build", "run"))
	depends_on("py-psutil", type=("build", "run"))
	depends_on("py-setuptools", type="build")
