# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsbtools(RPackage):
	"""Statistics Norway's Miscellaneous Tools

	Functions used by other packages from Statistics Norway are gathered. General data manipulation functions, and functions for hierarchical computations are included (Langsrud, 2020) <doi:10.13140/RG.2.2.27313.61283>. The hierarchy specification functions are useful within statistical disclosure control.
	"""
	
	homepage = "https://github.com/statisticsnorway/SSBtools"
	cran = "SSBtools" 

	version("1.5.0", md5="4108506fe5e3cbe62ebe7c2e9e521a88")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
