# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparsetscgm(RPackage):
	"""Sparse Time Series Chain Graphical Models

	Computes sparse vector autoregressive 				coefficients and precision matrices for time series 		chain graphical models. Fentaw Abegaz and Ernst Wit (2013)	<doi:10.1093/biostatistics/kxt005>.
	"""
	
	cran = "SparseTSCGM" 

	version("4.0", md5="bbc110d01624f0416044853c6a0ec7c5")

	depends_on("r@3.3.2:", type=("build", "run"))
	depends_on("r-glasso", type=("build", "run"))
	depends_on("r-longitudinal", type=("build", "run"))
	depends_on("r-huge", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
