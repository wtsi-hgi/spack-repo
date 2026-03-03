# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHglmData(RPackage):
	"""Data for the 'hglm' Package

	This data-only package was created for distributing data used in the examples of the 'hglm' package.
	"""
	
	cran = "hglm.data" 

	version("1.0-1", md5="92b6b9dc273b49a9a608b189c363c18d")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
