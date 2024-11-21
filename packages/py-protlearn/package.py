# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyProtlearn(PythonPackage):
	"""A Python package for extracting protein sequence features"""
	
	homepage = "https://github.com/tadorfer/protlearn"
	pypi = "protlearn/protlearn-0.0.3-py3-none-any.whl" 

	version("0.0.3", sha256="5288870261df1b3b0072a1997004d83a25d197db4f2589a0b219baeddde1cfb8", expand=False, url="https://files.pythonhosted.org/packages/88/1f/1c85f75779664f65bdaac78a515bcf86ea0c8926c74fa356c138b447dfbc/protlearn-0.0.3-py3-none-any.whl")
	version("0.0.2", sha256="84444917e1536b5db28b907707cd5fb70e1424917709362faa7356bb05b28958", expand=False, url="https://files.pythonhosted.org/packages/68/9d/a576a59ecdcecddb56465dcda7119c2e0e75ef16987c2a3f1fc1e8d44694/protlearn-0.0.2-py3-none-any.whl")
	version("0.0.1", sha256="a9d7e6b1d0936614301e7a5e80ce6a3c2f71c5fff663c58838d051cc2fb250c7")

	depends_on("python@3:", type=("build", "run"))
	depends_on("py-numpy@1.22", type="run")
	depends_on("py-pandas", type="run")
	depends_on("py-scikit-learn", type="run")
	depends_on("py-xgboost", type="run")
	depends_on("py-mlxtend", type="run")
	depends_on("py-biopython", type="run")
