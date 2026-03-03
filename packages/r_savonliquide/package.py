# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSavonliquide(RPackage):
	"""Accessibility Toolbox for 'R' Users

	Provides a toolbox that allows the user to implement accessibility related concepts. 
	"""
	
	homepage = "https://github.com/feddelegrand7/savonliquide"
	cran = "savonliquide" 

	version("0.2.0", md5="a399b9cace0f81230afd59d6667e81a4")

	depends_on("r-glue", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
