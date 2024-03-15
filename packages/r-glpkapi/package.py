# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlpkapi(RPackage):
	"""R Interface to C API of GLPK

	R Interface to C API of GLPK, depends on GLPK Version >= 4.42.
	"""
	
	cran = "glpkAPI" 

	version("1.3.4", md5="0a926d3332c28d9c0af760cb753a9c19")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("glpk@4.42:", type=("build", "link", "run"))
