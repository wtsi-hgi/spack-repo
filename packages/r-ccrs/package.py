# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCcrs(RPackage):
	"""Correct and Cluster Response Style Biased Data

	Functions for performing Correcting and Clustering response-style-biased preference data (CCRS). The main functions are correct.RS() for correcting for response styles, and ccrs() for simultaneously correcting and content-based clustering. The procedure begin with making rank-ordered boundary data from the given preference matrix using a function called create.ccrsdata(). Then in correct.RS(), the response style is corrected as follows: the rank-ordered boundary data are smoothed by I-spline functions, the given preference data are transformed by the smoothed functions. The resulting data matrix, which is considered as bias-corrected data, can be used for any data analysis methods. If one wants to cluster respondents based on their indicated preferences (content-based clustering), ccrs() can be applied to the given (response-style-biased) preference data, which simultaneously corrects for response styles and clusters respondents based on the contents. Also, the correction result can be checked by plot.crs() function.
	"""
	
	cran = "ccrs" 

	version("0.1.0", md5="3ea06c9d98a37be0210facce65375e00")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cds", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-limsolve", type=("build", "run"))
	depends_on("r-lsbclust", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
