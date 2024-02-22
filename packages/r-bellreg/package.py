# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBellreg(RPackage):
	"""Count Regression Models Based on the Bell Distribution

	Bell regression models for count data with overdispersion. The implemented models account for ordinary and zero-inflated regression models under both frequentist and Bayesian approaches. Theoretical details regarding the models implemented in the package can be found in Castellares et al. (2018) <doi:10.1016/j.apm.2017.12.014> and Lemonte et al. (2020) <doi:10.1080/02664763.2019.1636940>.
	"""
	
	homepage = "https://github.com/fndemarqui/bellreg"
	cran = "bellreg" 

	version("0.0.2", md5="12ba45331b72e0dee38aeaf4866d387f")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-extradistr", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-magic", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-numbers", type=("build", "run"))
	depends_on("r-lambertw", type=("build", "run"))
	depends_on("r-loo", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-rstantools@2:", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
