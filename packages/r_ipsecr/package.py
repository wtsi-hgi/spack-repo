# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIpsecr(RPackage):
	"""Spatially Explicit Capture-Recapture by Inverse Prediction

	Estimates the density of a spatially distributed animal population 
  sampled with an array of passive detectors, such as traps. Models incorporating 
  distance-dependent detection are fitted by simulation and inverse prediction 
  as proposed by Efford (2004) <doi:10.1111/j.0030-1299.2004.13043.x>.
	"""
	
	homepage = "https://github.com/MurrayEfford/ipsecr/"
	cran = "ipsecr" 

	version("1.4.1", md5="63658ded531dd92d04d78d0d49147dd7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-secr@4.5.8:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
