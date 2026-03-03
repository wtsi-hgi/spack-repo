# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGasmodel(RPackage):
	"""Generalized Autoregressive Score Models

	Estimation, forecasting, and simulation of generalized
    autoregressive score (GAS) models of Creal, Koopman, and Lucas (2013)
    <doi:10.1002/jae.1279> and Harvey (2013) <doi:10.1017/cbo9781139540933>.
    Model specification allows for various data types and distributions,
    different parametrizations, exogenous variables, joint and separate modeling
    of exogenous variables and dynamics, higher score and autoregressive orders,
    custom and unconditional initial values of time-varying parameters, fixed
    and bounded values of coefficients, and missing values. Model estimation is
    performed by the maximum likelihood method.
	"""
	
	homepage = "https://github.com/vladimirholy/gasmodel"
	cran = "gasmodel" 

	version("0.6.0", md5="6ab45eed4dd728cb10ccba0a784b86e6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-arrangements", type=("build", "run"))
	depends_on("r-circstats", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mvnfast", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
