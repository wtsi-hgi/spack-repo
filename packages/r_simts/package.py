# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimts(RPackage):
	"""Time Series Analysis Tools

	A system contains easy-to-use tools as a support for time series analysis courses. In particular, it incorporates a technique called Generalized Method of Wavelet Moments (GMWM) as well as its robust implementation for fast and robust parameter estimation of time series models which is described, for example, in Guerrier et al. (2013) <doi: 10.1080/01621459.2013.799920>. More details can also be found in the paper linked to via the URL below.
	"""
	
	homepage = "https://github.com/SMAC-Group/simts"
	cran = "simts" 

	version("0.2.2", md5="8fbcbf0e6fa49e3fe672e9f489e8b830")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-robcor", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
