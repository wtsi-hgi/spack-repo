# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPyramids(PythonPackage):
	"""Pyramids Parser: English Language Semantic Extraction"""
	
	homepage = "https://github.com/hosford42/pyramids"
	pypi = "pyramids/pyramids-0.0.1-py3-none-any.whl" 

	version("0.0.1", sha256="fb6178539af808c8e4cc234c514b3569831254000d949002d9089f3cb6bc366e", expand=False, url="https://files.pythonhosted.org/packages/25/25/07f24630ec69c48effafc17181bf1c7752dd3d810259ff06efba8613b606/pyramids-0.0.1-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))

# {'pyramids-categories(>=1.0)': ['0.0.1']}