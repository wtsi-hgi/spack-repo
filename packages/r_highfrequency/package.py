# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHighfrequency(RPackage):
	"""Tools for Highfrequency Data Analysis

	Provide functionality to manage, clean and match highfrequency
    trades and quotes data, calculate various liquidity measures, estimate and
    forecast volatility, detect price jumps and investigate microstructure noise and intraday
    periodicity. A detailed vignette can be found in the open-access paper 
    "Analyzing Intraday Financial Data in R: The highfrequency Package" 
    by Boudt, Kleen, and Sjoerup (2022, <doi:10.18637/jss.v104.i08>). 
	"""
	
	homepage = "https://github.com/jonathancornelissen/highfrequency"
	cran = "highfrequency" 

	version("1.0.1", md5="244f765a2cc6e90bde862262f0557b4d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-data-table@1.12:", type=("build", "run"))
	depends_on("r-rcpproll", type=("build", "run"))
	depends_on("r-quantmod", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
