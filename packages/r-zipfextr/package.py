# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZipfextr(RPackage):
	"""Zipf Extended Distributions

	Implementation of four extensions of the Zipf distribution: the Marshall-Olkin 
  Extended Zipf (MOEZipf) Pérez-Casany, M., & Casellas, A. (2013) <arXiv:1304.4540>, the Zipf-Poisson Extreme (Zipf-PE), the 
  Zipf-Poisson Stopped Sum (Zipf-PSS) and the Zipf-Polylog distributions. 
  In log-log scale, the two first extensions allow for top-concavity 
  and top-convexity while the third one only allows for top-concavity. 
  All the extensions maintain the linearity associated with the Zipf model in the tail.
	"""
	
	homepage = "https://github.com/ardlop/zipfextR"
	cran = "zipfextR" 

	version("1.0.2", md5="5ced3986629fbd390be8afca9701d981")

	depends_on("r@2.0.1:", type=("build", "run"))
	depends_on("r-vgam@0.9.8:", type=("build", "run"))
	depends_on("r-tolerance@1.2:", type=("build", "run"))
	depends_on("r-copula@0.999.18:", type=("build", "run"))
