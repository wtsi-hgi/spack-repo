# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSoilhypfit(RPackage):
	"""Modelling of Soil Water Retention and Hydraulic Conductivity
Data

	Provides functions for efficiently estimating properties of the Van Genuchten-Mualem model for soil hydraulic parameters from possibly sparse soil water retention and hydraulic conductivity data by multi-response parameter estimation methods (Stewart, W.E., Caracotsios, M. Soerensen, J.P. (1992) "Parameter estimation from multi-response data" <doi:10.1002/aic.690380502>). Parameter estimation is simplified by exploiting the fact that residual and saturated water contents and saturated conductivity are conditionally linear parameters (Bates, D. M.  and Watts, D. G. (1988) "Nonlinear Regression Analysis and Its Applications" <doi:10.1002/9780470316757>). Estimated parameters are optionally constrained by the evaporation characteristic length (Lehmann, P., Bickel, S., Wei, Z. and Or, D. (2020) "Physical Constraints for Improved Soil Hydraulic Parameter Estimation by Pedotransfer Functions" <doi:10.1029/2019WR025963>) to ensure that the estimated parameters are physically valid. Common S3 methods and further utility functions allow to process, explore and visualise estimation results.
	"""
	
	cran = "soilhypfit" 

	version("0.1-7", md5="2ae7aea9cc07924df6eb50bd159fe9c6")

	depends_on("r-nloptr@1.2.1:", type=("build", "run"))
	depends_on("r-snowfall", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-quadprog@1.5.7:", type=("build", "run"))
	depends_on("r-rmpfr@0.7.2:", type=("build", "run"))
	depends_on("r-soilhyp@0.1.3:", type=("build", "run"))
	depends_on("gmp@4.2.3:", type=("build", "link", "run"))
	depends_on("mpfr@3.0.0:", type=("build", "link", "run"))
