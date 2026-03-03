# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGb(RPackage):
	"""Generalize Lambda Distribution and Generalized Bootstrapping

	A collection of algorithms and functions 
  for fitting data to a generalized lambda distribution 
  via moment matching methods, and generalized 
  bootstrapping.
	"""
	
	cran = "gb" 

	version("2.3.3", md5="991ad82242f17e95ad2b3594e617eec0")

	depends_on("r@2.5:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
