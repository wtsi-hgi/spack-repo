# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDcm2(RPackage):
	"""Calculating the M2 Model Fit Statistic for Diagnostic
Classification Models

	A collection of functions for calculating the M2 model fit
    statistic for diagnostic classification models as described by Liu et al.
    (2016) <DOI:10.3102/1076998615621293>. These functions provide multiple
    sources of information for model fit according to the M2 statistic,
    including the M2 statistic, the *p* value for that M2 statistic, and the
    Root Mean Square Error of Approximation based on the M2 statistic.
	"""
	
	homepage = "https://github.com/atlas-aai/dcm2"
	cran = "dcm2" 

	version("1.0.2", md5="3af43306a223aa43be1675b2ea6e5767", url="https://cran.r-project.org/src/contrib/dcm2_1.0.2.tar.gz")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr@0.8.4:", type=("build", "run"))
	depends_on("r-glue@1.4.2:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-modelr@0.1.8:", type=("build", "run"))
	depends_on("r-purrr@0.3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tibble@2.1.3:", type=("build", "run"))
	depends_on("r-tidyr@1.1.4:", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.9.800.1:", type=("build", "run"))
