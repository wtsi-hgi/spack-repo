# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLatrend(RPackage):
	"""A Framework for Clustering Longitudinal Data

	A framework for clustering longitudinal datasets in a standardized way. 
    The package provides an interface to existing R packages for clustering longitudinal univariate trajectories, facilitating reproducible and transparent analyses. 
    Additionally, standard tools are provided to support cluster analyses, including repeated estimation, model validation, and model assessment. 
    The interface enables users to compare results between methods, and to implement and evaluate new methods with ease.
    The 'akmedoids' package is available from <https://github.com/MAnalytics/akmedoids>.
	"""
	
	homepage = "https://github.com/philips-software/latrend"
	cran = "latrend" 

	version("1.6.0", md5="20aadfc95af2c6b0f2c459333f1eb676")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-assertthat@0.2.1:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-data-table@1.12:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rmarkdown@1.18:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
