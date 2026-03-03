# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLogistf(RPackage):
	"""Firth's Bias-Reduced Logistic Regression

	Fit a logistic regression model using Firth's bias reduction method, equivalent to penalization of the log-likelihood by the Jeffreys 
	prior. Confidence intervals for regression coefficients can be computed by penalized profile likelihood. Firth's method was proposed as ideal
	solution to the problem of separation in logistic regression, see Heinze and Schemper (2002) <doi:10.1002/sim.1047>. If needed, the bias reduction can be turned off such that ordinary
	maximum likelihood logistic regression is obtained. Two new modifications of Firth's method, FLIC and FLAC, lead to unbiased predictions and are now available
	in the package as well, see Puhr et al (2017) <doi:10.1002/sim.7273>.
	"""
	
	homepage = "https://cemsiis.meduniwien.ac.at/en/kb/science-research/software/statistical-software/firth-correction/"
	cran = "logistf" 

	version("1.26.0", md5="084dbd52a2c19a3d90819daad164d508")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mice", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-formula-tools", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
