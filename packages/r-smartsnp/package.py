# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmartsnp(RPackage):
	"""Fast Multivariate Analyses of Big Genomic Data

	Fast computation of multivariate analyses of small (10s to 100s markers) to big (1000s to 100000s) genotype data. Runs Principal Component Analysis allowing for centering, z-score standardization and scaling for genetic drift, projection of ancient samples to modern genetic space and multivariate tests for differences in group location (Permutation-Based Multivariate Analysis of Variance) and dispersion (Permutation-Based Multivariate Analysis of Dispersion).
	"""
	
	cran = "smartsnp" 

	version("1.1.0", md5="2ea72ac278a264238bc06de3c3ebd08a")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-bootsvd", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-vroom", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
