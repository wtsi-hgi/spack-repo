# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFnets(RPackage):
	"""Factor-Adjusted Network Estimation and Forecasting for
High-Dimensional Time Series

	Implements methods for network estimation and forecasting of high-dimensional time series 
    exhibiting strong serial and cross-sectional correlations under a factor-adjusted vector autoregressive model.
    See Barigozzi, Cho and Owens (2024+) <doi:10.1080/07350015.2023.2257270> for further descriptions of FNETS methodology and 
    Owens, Cho and Barigozzi (2024+) <arXiv:2301.11675> accompanying the R package.
	"""
	
	cran = "fnets" 

	version("0.1.6", md5="406bd50d58738a492afbf7b1ca3904d6")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
