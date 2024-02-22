# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForecomp(RPackage):
	"""Size-Power Tradeoff Visualization for Equal Predictive Ability
of Two Forecasts

	Offers a set of tools for visualizing and analyzing size and power properties of the test for equal predictive accuracy, the Diebold-Mariano test that is based on heteroskedasticity and autocorrelation-robust (HAR) inference. A typical HAR inference is involved with non-parametric estimation of the long-run variance, and one of its tuning parameters, the truncation parameter, trades off a size and power. Lazarus, Lewis, and Stock (2021)<doi:10.3982/ECTA15404> theoretically characterize the size-power frontier for the Gaussian multivariate location model. 'ForeComp' computes and visualizes the finite-sample size-power frontier of the Diebold-Mariano test based on fixed-b asymptotics together with the Bartlett kernel. To compute the finite-sample size and power, it works with the best approximating ARMA process to the given dataset. It informs the user how their choice of the truncation parameter performs and how robust the testing outcomes are.
	"""
	
	homepage = "https://github.com/mcmcs/ForeComp"
	cran = "ForeComp" 

	version("0.9.0", md5="71d0a35db81cd48854e5be8ecc890f23")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-astsa", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
