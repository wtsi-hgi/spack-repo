# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGwex(RPackage):
	"""Multi-Site Stochastic Models for Daily Precipitation and
Temperature

	Application of multi-site models for daily precipitation and temperature data. 
  This package is designed for an application to 105 precipitation and 26 temperature gauges located in Switzerland.
  It applies fitting procedures and provides weather generators described in the following references:
  - Evin, G., A.-C. Favre, and B. Hingray. (2018) <doi:10.5194/hess-22-655-2018>.
  - Evin, G., A.-C. Favre, and B. Hingray. (2018) <doi:10.1007/s00704-018-2404-x>.
	"""
	
	cran = "GWEX" 

	version("1.1.3", md5="342d948c8e61eb6f61923f0a6776f27e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-envstats", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-fgarch", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-renext", type=("build", "run"))
	depends_on("r-lmomco", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
