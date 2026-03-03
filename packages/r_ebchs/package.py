# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REbchs(RPackage):
	"""An Empirical Bayes Method for Chi-Squared Data

	We provide the main R functions to compute the posterior interval for the noncentrality parameter of the chi-squared distribution. The skewness estimate of the posterior distribution is also available to improve the coverage rate of posterior intervals. Details can be found in Du and Hu (2020) <doi:10.1080/01621459.2020.1777137>.  
	"""
	
	homepage = "https://github.com/dulilun/EBCHS"
	cran = "EBCHS" 

	version("0.1.0", md5="f94f64bda57e728be846bc11a9593262")

	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
