# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyRootutils(PythonPackage):
	"""Simple package for easy project root setup"""
	
	homepage = "https://github.com/ashleve/rootutils"
	pypi = "rootutils/rootutils-1.0.7-py3-none-any.whl" 

	version("1.0.5", sha256="af018100a930937b8b59613e4f7f9184efd34d3383f9817eeba8e712d7b24810", expand=False, url="https://files.pythonhosted.org/packages/1f/f8/2b3c7d8cbf5104ce7cd3f89f5121368d9fd368ca5ab66ac5188ad0641bdf/rootutils-1.0.5-py3-none-any.whl")
	version("1.0.6", sha256="f20a98c30fe693b17e88fcc63c8b885909f4ac9d695e048b7f48716bfc21b458", expand=False, url="https://files.pythonhosted.org/packages/31/16/d6cf39fd75bcde30e82b206726129cf7e3acb697bdc3c06096d4fd32a9dd/rootutils-1.0.6-py3-none-any.whl")
	version("1.0.7", sha256="89f1994e6d0f499db7aca7f90edc146801cb33c8565a15c7cee4a4e4fc8c6eef", expand=False, url="https://files.pythonhosted.org/packages/19/17/1e8ba0be5b52aa7a18f0df7bd6ab31345a3a4f515d6beac6a765fcacaaa3/rootutils-1.0.7-py3-none-any.whl")

	depends_on("python@3.7.0:", type=("build", "run"))
	depends_on("py-python-dotenv", type=("build", "run"))
