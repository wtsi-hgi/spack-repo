# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaintData(RPackage):
	"""Model and Analyse Interval Data

	Implements methodologies for modelling interval data by Normal
    and Skew-Normal distributions, considering appropriate parameterizations of
    the variance-covariance matrix that takes into account the intrinsic nature of
    interval data, and lead to four different possible configuration structures.
    The Skew-Normal parameters can be estimated by maximum likelihood, while Normal
    parameters may be estimated by maximum likelihood or robust trimmed maximum
    likelihood methods.
	"""
	
	cran = "MAINT.Data" 

	version("2.7.1", md5="971a95408a463bb820b724709f47fabd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-misctools", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-rrcov", type=("build", "run"))
	depends_on("r-pcapp", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-sn@1.3:", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.9.500.2:", type=("build", "run"))
