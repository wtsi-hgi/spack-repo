# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMfgarch(RPackage):
	"""Mixed-Frequency GARCH Models

	Estimating GARCH-MIDAS (MIxed-DAta-Sampling) models (Engle, Ghysels, Sohn, 2013, <doi:10.1162/REST_a_00300>) and related statistical inference, accompanying the paper "Two are better than one: Volatility forecasting using multiplicative component GARCH models" by Conrad and Kleen (2020, <doi:10.1002/jae.2742>). The GARCH-MIDAS model decomposes the conditional variance of (daily) stock returns into a short- and long-term component, where the latter may depend on an exogenous covariate sampled at a lower frequency. 
	"""
	
	homepage = "https://github.com/onnokleen/mfGARCH/"
	cran = "mfGARCH" 

	version("0.2.1", md5="c5f13c41f8acf2a34bc77222a9e4fd54")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-maxlik", type=("build", "run"))
