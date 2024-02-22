# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJinjar(RPackage):
	"""Template Engine Inspired by 'Jinja'

	Template engine powered by the 'inja' C++ library. Users
    write a template document, using syntax inspired by the 'Jinja' Python
    package, and then render the final document by passing data from R.
    The template syntax supports features such as variables, loops,
    conditions and inheritance.
	"""
	
	homepage = "https://davidchall.github.io/jinjar/"
	cran = "jinjar" 

	version("0.3.1", md5="237ac5482e6751f92ea9a652e75a1589")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
