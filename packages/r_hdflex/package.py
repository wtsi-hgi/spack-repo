# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdflex(RPackage):
	"""High-Dimensional Aggregate Density Forecasts

	Provides a forecasting method that maps vast numbers of
    (scalar-valued) signals of any type into an aggregate density forecast
    in a time-varying and computationally fast manner. The method proceeds
    in two steps: First, it transforms a predictive signal into a density
    forecast. Second, it combines the generated candidate density
    forecasts into an ultimate density forecast. The methods are explained
    in detail in Adaemmer et al. (2023) <doi:10.2139/ssrn.4342487>.
	"""
	
	cran = "hdflex" 

	version("0.2.1", md5="03eaa4d5725ce594ac16072a3e803e6d")
	version("0.2.0", md5="d048397823ca71b8db32a19c8457c46d")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-checkmate@2.3.1:", type=("build", "run"))
	depends_on("r-dplyr@1.1.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-roll@1.1.6:", type=("build", "run"))
	depends_on("r-stringr@1.5.1:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
