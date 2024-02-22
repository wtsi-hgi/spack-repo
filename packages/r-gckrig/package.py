# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGckrig(RPackage):
	"""Analysis of Geostatistical Count Data using Gaussian Copulas

	Provides a variety of functions to analyze and model
    geostatistical count data with Gaussian copulas, including
 1) data simulation and visualization; 
 2) correlation structure assessment (here also known as the Normal To Anything); 
 3) calculate multivariate normal rectangle probabilities; 
 4) likelihood inference and parallel prediction at predictive locations.
 Description of the method is available from: Han and DeOliveira (2018) <doi:10.18637/jss.v087.i13>.
	"""
	
	cran = "gcKrig" 

	version("1.1.8", md5="d5ed36daf2dfd5603415e9a104ffd9a2")

	depends_on("r@3.2.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
