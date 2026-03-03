# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNlrr(RPackage):
	"""Non-Linear Relative Risk Estimation and Plotting

	Estimate the non-linear odds ratio and plot it against a continuous exposure.
	"""
	
	cran = "nlrr" 

	version("0.1", md5="5c8db2a48f4cea06f169d0cf7ea80f84")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
