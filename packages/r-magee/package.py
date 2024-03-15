# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMagee(RPackage):
	"""Mixed Model Association Test for GEne-Environment Interaction

	Use a 'glmmkin' class object (GMMAT package) from the null model to perform generalized linear mixed model-based single-variant and variant set main effect tests, gene-environment interaction tests, and joint tests for association, as proposed in Wang et al. (2020) <DOI:10.1002/gepi.22351>.
	"""
	
	cran = "MAGEE" 

	version("1.3.2", md5="29eb11b0e7f407c790b29815145b1d6d")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-gmmat", type=("build", "run"))
	depends_on("r-compquadform", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
