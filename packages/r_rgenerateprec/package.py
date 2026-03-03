# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgenerateprec(RPackage):
	"""Tools to Generate Daily-Precipitation Time Series

	The method 'generate()' is extended for spatial multi-site
    stochastic generation of daily precipitation. It generates precipitation
    occurrence in several sites using logit regression (Generalized Linear
    Models) and the approach by D.S. Wilks (1998) <doi:10.1016/S0022-1694(98)00186-3> . 
	"""
	
	homepage = "https://github.com/ecor/RGENERATEPREC"
	cran = "RGENERATEPREC" 

	version("1.2.9", md5="f283ea4acdcfcff3f99a49789ddbe8fb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
	depends_on("r-rgenerate", type=("build", "run"))
	depends_on("r-blockmatrix", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rmawgen", type=("build", "run"))
