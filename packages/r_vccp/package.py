# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVccp(RPackage):
	"""Vine Copula Change Point Detection in Multivariate Time Series

	Implements the Vine Copula Change Point (VCCP) methodology for the estimation of the number and location of multiple change points in the vine copula structure of multivariate time series. The method uses vine copulas, various state-of-the-art segmentation methods to identify multiple change points, and a likelihood ratio test or the stationary bootstrap for inference. The vine copulas allow for various forms of dependence between time series including tail, symmetric and asymmetric dependence. The functions have been extensively tested on simulated multivariate time series data and fMRI data. For details on the VCCP methodology, please see Xiong & Cribben (2021).
	"""
	
	cran = "vccp" 

	version("0.1.1", md5="2a3af70d200461dc2f71106202f9d2ca")

	depends_on("r-vinecopula", type=("build", "run"))
	depends_on("r-mosum", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
