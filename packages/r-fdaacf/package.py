# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFdaacf(RPackage):
	"""Autocorrelation Function for Functional Time Series

	Quantify the serial correlation across lags of a given functional 
    time series using the autocorrelation function and a partial autocorrelation
    function for functional time series proposed in 
    Mestre et al. (2021) <doi:10.1016/j.csda.2020.107108>.
    The autocorrelation functions are based on the L2 norm of the lagged covariance 
    operators of the series. Functions are available for estimating the 
    distribution of the autocorrelation functions under the assumption 
    of strong functional white noise.
	"""
	
	homepage = "https://github.com/GMestreM/fdaACF"
	cran = "fdaACF" 

	version("1.0.0", md5="4eb311ba303202f5c08b82d3fc7c0637")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-compquadform", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-vars", type=("build", "run"))
