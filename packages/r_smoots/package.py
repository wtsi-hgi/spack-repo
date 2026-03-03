# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmoots(RPackage):
	"""Nonparametric Estimation of the Trend and Its Derivatives in TS

	The nonparametric trend and its derivatives in equidistant time 
    series (TS) with short-memory stationary errors can be estimated. The 
    estimation is conducted via local polynomial regression using an 
    automatically selected bandwidth obtained by a built-in iterative plug-in 
    algorithm or a bandwidth fixed by the user. A Nadaraya-Watson kernel 
    smoother is also built-in as a comparison. With version 1.1.0, a linearity 
    test for the trend function, forecasting methods and backtesting 
    approaches are implemented as well.
    The smoothing methods of the package are described in Feng, Y., Gries, T., 
    and Fritz, M. (2020) <doi:10.1080/10485252.2020.1759598>.
	"""
	
	homepage = "https://wiwi.uni-paderborn.de/en/dep4/feng/"
	cran = "smoots" 

	version("1.1.4", md5="061ab5c29f788afb83625f9c822df6d3")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-future@1.22.1:", type=("build", "run"))
	depends_on("r-future-apply@1.8.1:", type=("build", "run"))
	depends_on("r-progressr@0.8:", type=("build", "run"))
	depends_on("r-progress@1.2.2:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
