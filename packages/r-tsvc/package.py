# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsvc(RPackage):
	"""Tree-Structured Modelling of Varying Coefficients

	Fitting tree-structured varying coefficient models (Berger et al. (2019), <doi:10.1007/s11222-018-9804-8>). Simultaneous detection of covariates with varying coefficients and effect modifiers that induce varying coefficients if they are present. 
	"""
	
	cran = "TSVC" 

	version("1.5.3", md5="eb4c142f03bf3b8879c28a7318693397")

	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
