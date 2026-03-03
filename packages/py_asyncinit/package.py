# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyAsyncinit(PythonPackage):
	"""Class decorator to enable async __init__"""
	
	homepage = "https://github.com/kchmck/pyasyncinit"
	pypi = "asyncinit/asyncinit-0.2.4-py3-none-any.whl" 

	version("0.2.0", sha256="695df57099b6ebf2f4e746a7af6832aa8fa459976cca229ffc5401a4e49c8eb1", expand=False, url="https://files.pythonhosted.org/packages/19/d8/64fa0e2fce474eef12c9276e6182e6a292765821c540758fedae6218b12f/asyncinit-0.2.0-py2.py3-none-any.whl")
	version("0.2.1", sha256="a0a78b6526763b727d055ab615b0b49fc3b318896c97bbba98b70e02d3c26631", expand=False, url="https://files.pythonhosted.org/packages/08/07/ac1d6dac5b910211d5bf426795baaeb7965af6a089f86e39f092d011680a/asyncinit-0.2.1-py3-none-any.whl")
	version("0.2.2", sha256="6e82addb3911e2243271a34f31944f1a7ca5ffeff59420587983cebe05f0dd19", expand=False, url="https://files.pythonhosted.org/packages/5d/70/d83b8ffaf97bfd425a52e838dd3ff053e7f1e3c9f810d6f98aff29d8f943/asyncinit-0.2.2-py3-none-any.whl")
	version("0.2.3", sha256="c9ca71891a8ae9d9a6efd7070fc1d1f8afa7b38fd873a47f351ea7c9092583d8", expand=False, url="https://files.pythonhosted.org/packages/df/ac/c9bc8619f35ce7e6f062dde759bc8301344d13ed72c1a81b19a336159d84/asyncinit-0.2.3-py3-none-any.whl")
	version("0.2.4", sha256="9f11291943488abd15a1463dad98452e3bd6b39e8e6d45bc7cc008a09825b11e", expand=False, url="https://files.pythonhosted.org/packages/b4/12/a73bd1bcba7f99738d1f644ed17b526f84e97aaabda301800435ca202570/asyncinit-0.2.4-py3-none-any.whl")

	depends_on("python@3.5:", type=("build", "run"))
	depends_on("py-pytest", type=("build", "run"))
	depends_on("py-pylint", type=("build", "run"))

# {"pylint(~=2.1);extra=='dev'": ['0.2.4'], "pytest(~=3.6);extra=='dev'": ['0.2.4']}