# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeofourierfda(RPackage):
	"""Ordinary Functional Kriging Using Fourier Smoothing and Gaussian
Quadrature

	Implementation of the ordinary functional kriging method 
    proposed by Giraldo (2011) <doi:10.1007/s10651-010-0143-y>. This
    implements an alternative method to estimate the trace-variogram using
    Fourier Smoothing and Gaussian Quadrature. 
	"""
	
	cran = "geoFourierFDA" 

	version("0.1.0", md5="5f28ccfdcab651a067eca977820f3d5f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-orthopolynom", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
