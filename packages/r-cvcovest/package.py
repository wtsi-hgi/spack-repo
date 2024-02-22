# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCvcovest(RPackage):
	"""Cross-Validated Covariance Matrix Estimation

	An efficient cross-validated approach for covariance matrix
    estimation, particularly useful in high-dimensional settings. This
    method relies upon the theory of high-dimensional loss-based covariance
    matrix estimator selection developed by Boileau et al. (2022)
    <doi:10.1080/10618600.2022.2110883> to identify the optimal estimator
    from among a prespecified set of candidates.
	"""
	
	homepage = "https://github.com/PhilBoileau/cvCovEst"
	cran = "cvCovEst" 

	version("1.2.2", md5="6fca3066d2cb7daf8aded3fcc6939764")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-origami", type=("build", "run"))
	depends_on("r-coop", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rmtstat", type=("build", "run"))
