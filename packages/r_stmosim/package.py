# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStmosim(RPackage):
	"""Quantile-Quantile Plot with Several Gaussian Simulations

	Plots a QQ-Norm Plot with several Gaussian simulations.
	"""
	
	cran = "StMoSim" 

	version("3.1.1", md5="ddee143f347911943773f61c80e2a881")

	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
