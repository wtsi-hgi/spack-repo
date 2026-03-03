# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnvoutliers(RPackage):
	"""Methods for Identification of Outliers in Environmental Data

	Three semi-parametric methods for detection of outliers in environmental data based on kernel regression and subsequent analysis of smoothing residuals. The first method (Campulova, Michalek, Mikuska and Bokal (2018) <DOI: 10.1002/cem.2997>) analyzes the residuals using changepoint analysis, the second method is based on control charts (Campulova, Veselik and Michalek (2017) <DOI: 10.1016/j.apr.2017.01.004>) and the third method (Holesovsky, Campulova and Michalek (2018) <DOI: 10.1016/j.apr.2017.06.005>) analyzes the residuals using extreme value theory (Holesovsky, Campulova and Michalek (2018) <DOI: 10.1016/j.apr.2017.06.005>).
	"""
	
	cran = "envoutliers" 

	version("1.1.0", md5="a79d8dda13ce5f2e22bb8df100e9ba4d")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-changepoint", type=("build", "run"))
	depends_on("r-ecp", type=("build", "run"))
	depends_on("r-ismev", type=("build", "run"))
	depends_on("r-lokern", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
