# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpera(RPackage):
	"""Online Prediction by Expert Aggregation

	Misc methods to form online predictions, for regression-oriented 
    time-series, by combining a finite set of forecasts provided by the user. See 
             Cesa-Bianchi and Lugosi (2006) <doi:10.1017/CBO9780511546921> for an overview. 
	"""
	
	homepage = "http://pierre.gaillard.me/opera.html"
	cran = "opera" 

	version("1.2.0", md5="9c14d860f231d09b94456d1f4295d9e4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-ramcharts", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-piper", type=("build", "run"))
	depends_on("r-alabama", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
